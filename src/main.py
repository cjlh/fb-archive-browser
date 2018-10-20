#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
from datetime import datetime

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QWidget, \
    QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QListWidgetItem, \
    QStyleFactory, QSizePolicy
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont, QIcon
from PyQt5.QtCore import pyqtSlot, Qt

import ui_mainwindow
import ui_aboutdialog


class ConversationPreview(object):
    def __init__(self, title, preview_message, timestamp_ms):
        self.title = title
        # Fix FB message encoding for emojis and strip any whitespace
        self.preview_message = parse_fb_message(preview_message)
        self.timestamp_ms = timestamp_ms


class Conversation(object):
    def __init__(self, participants, path, media_path, title,
                 is_still_participant, thread_type, timestamp_ms,
                 preview_message):
        self.participants = participants
        self.path = path
        self.media_path = media_path
        self.title = title
        self.is_still_participant = is_still_participant
        self.thread_type = thread_type
        self.timestamp_ms = timestamp_ms
        # Fix FB message encoding for emojis and strip any whitespace
        self.preview_message = \
            preview_message.encode('latin1').decode('utf-8').strip()


class AboutQDialog(QDialog):
    def __init__(self):
        super(AboutQDialog, self).__init__()
        ui = ui_aboutdialog.Ui_Dialog()
        ui.setupUi(self)


class ConversationsQMainWindow(QMainWindow):
    def __init__(self, conversations):
        super(ConversationsQMainWindow, self).__init__()

        ui = ui_mainwindow.Ui_MainWindow()
        self.ui = ui
        ui.setupUi(self)

        # File menu
        ui.actionExit.triggered.connect(self.triggered_actionExit)
        # Help menu
        ui.actionAbout.triggered.connect(self.triggered_actionAbout)

        conversationsStyleSheet = """
            QListWidget {
                outline: none;
            }

            QListWidget::item:selected,
            QListWidget::item:focus {
                background-color: #EEEEEE;
                border: none;
            }
        """
        ui.conversationsList.setStyleSheet(conversationsStyleSheet)

        # Trigger when a conversation is selected
        ui.conversationsList.itemSelectionChanged.connect(
            self.selected_conversation)

        default_search_icon_path = \
            "./icons/search.svg"
        ui.actionSearch.setIcon(QIcon.fromTheme(
            "system-search", QIcon(default_search_icon_path)))

        self.populate_conversations_list(conversations)

    @pyqtSlot()
    def triggered_actionAbout(self):
        dialog = AboutQDialog()
        dialog.exec_()

    @pyqtSlot()
    def triggered_actionExit(self):
        self.close()

    @pyqtSlot()
    def selected_conversation(self):
        conversation = \
            self.ui.conversationsList.currentItem().data(Qt.UserRole)
        self.load_conversation(conversation)

    def populate_conversations_list(self, conversations):
        for conversation in conversations:
            widget = ConversationsListQWidget(self.ui,
                                              conversation.title,
                                              conversation.preview_message,
                                              conversation.timestamp_ms)

            widget.setSizePolicy(QSizePolicy.Ignored,
                                 QSizePolicy.MinimumExpanding)

            item = QListWidgetItem(self.ui.conversationsList)

            item.setData(Qt.UserRole, conversation)
            item.setSizeHint(widget.sizeHint())

            self.ui.conversationsList.addItem(item)
            self.ui.conversationsList.setItemWidget(item, widget)

    def load_conversation(self, conversation):
        with open(conversation.path + "/message.json") as f:
            messages_data = json.load(f)
        self.ui.messagesList.clear()
        for message in messages_data["messages"]:
            message_content = parse_fb_message(message.get("content", ""))
            self.ui.messagesList.addItem(message_content)


class ConversationsListQWidget(QWidget):
    def __init__(self, ui, title, recent_message, timestamp_ms, parent=None):
        super(ConversationsListQWidget, self).__init__(parent)

        self.row = QVBoxLayout()
        # self.row.maximumSize = ui.conversationsList.maximumSize()

        title = truncate(title, 15)
        recent_message = truncate(recent_message, 30)

        heading_row = QHBoxLayout()
        heading_row.maximumSize = ui.conversationsList.maximumSize()

        title_font = QFont("Sans Serif", 10)
        title_label = QLabel(title)
        title_label.setFont(title_font)
        heading_row.addWidget(title_label)
        heading_row.setStretchFactor(title_label, 1)

        time_font = QFont("Sans Serif", 10)
        time_string = timestamp_ms_to_timestring(timestamp_ms)
        time_label = QLabel(time_string)
        time_label.setFont(time_font)
        heading_row.addWidget(time_label)
        heading_row.setStretchFactor(time_label, 0)

        self.row.addItem(heading_row)

        preview_font = QFont("Sans Serif", 9)
        preview_label = QLabel(recent_message)
        preview_label.setFont(preview_font)
        preview_label.setStyleSheet("QLabel {color: #555555;}")
        self.row.addWidget(preview_label)

        self.setLayout(self.row)


def truncate(s, length):
    if (length < 3):
        raise ValueError("Maximum string length must be at least 3")
    if (len(s) > length):
            return s[0:length - 3] + "..."
    else:
        return s


def parse_fb_message(message):
    return message.encode('latin1').decode('utf-8').strip()


def get_fb_dir():
    data_dir = "../data"
    fb_dir = None
    for dirname in next(os.walk(data_dir))[1]:
        if (dirname[0:9] == "facebook-"):
            fb_dir = data_dir + "/" + dirname
    return fb_dir


def timestamp_ms_to_timestring(timestamp_ms):
    as_date = datetime.fromtimestamp(timestamp_ms / 1000.0)
    return as_date.strftime("%d %b %y")


def get_conversations_list(fb_dir):
    messages_dir = fb_dir + "/messages"
    special_dirs = ["stickers_used"]
    conversations = []
    for dirname in next(os.walk(messages_dir))[1]:
        # For each conversation, there is an all-lowercase directory containing
        # the messages.json file. When a conversation contains media there is
        # a separate directory with the same name, except that the directory's
        # name is in PascalCase. So we check that the current directory is
        # all-lowercase.
        if (dirname.lower() != dirname or dirname in special_dirs):
            continue

        path = messages_dir + "/" + dirname
        with open(path + "/message.json") as f:
            messages_data = json.load(f)

        participants = [d["name"] for d in messages_data["participants"]]
        media_path = messages_data.get("thread_path", "")

        # No title if conversation is with a deleted user
        title = messages_data.get("title", "Facebook User")

        is_still_participant = messages_data["is_still_participant"]
        thread_type = messages_data["thread_type"]

        preview_message_dict = messages_data["messages"][0]
        preview_message = preview_message_dict.get("content", "(No messages)")
        timestamp_ms = preview_message_dict.get("timestamp_ms", "0")
        """
        conversations.append(ConversationPreview(title, preview_message,
                                                 timestamp_ms))
        """
        conversations.append(Conversation(participants, path, media_path,
                                          title, is_still_participant,
                                          thread_type, timestamp_ms,
                                          preview_message))
    return conversations


def get_ordered_conversations_list(fb_dir):
    conversations = get_conversations_list(fb_dir)
    ordered_conversations = sorted(conversations,
                                   key=lambda k: k.timestamp_ms,
                                   reverse=True)
    return ordered_conversations


if (__name__ == "__main__"):
    app = QApplication(sys.argv)

    fb_dir = get_fb_dir()
    if (fb_dir is None):
        print("Facebook archive directory not found.")
        exit()

    print("Facebook directory:", fb_dir)

    conversations = get_ordered_conversations_list(fb_dir)
    print("Loaded conversations list.")

    window = ConversationsQMainWindow(conversations)
    window.show()

    sys.exit(app.exec_())
