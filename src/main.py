import os
import sys
import json

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QWidget, \
    QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QListWidgetItem, \
    QStyleFactory
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont, QIcon

from ui_mainwindow import Ui_MainWindow


class ConversationPreview(object):
    def __init__(self, title, preview_message):
        self.title = title
        self.preview_message = preview_message


class Conversation(object):
    def __init__(self, participants, path, media_path, title,
                 is_still_participant, thread_type):
        self.participants = participants
        self.path = path
        self.media_path = media_path
        self.title = title
        self.is_still_participant = is_still_participant
        self.thread_type = thread_type


class ConversationsQMainWindow(QMainWindow):
    def __init__(self, conversations):
        super(ConversationsQMainWindow, self).__init__()

        ui = Ui_MainWindow()
        ui.setupUi(self)

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

        default_search_icon_path = \
            "./icons/search.svg"
        ui.actionSearch.setIcon(QIcon.fromTheme(
            "system-search", QIcon(default_search_icon_path)))

        populate_conversations_list(ui, conversations)


class ConversationsListQWidget(QWidget):
    def __init__(self, title, recent_message, parent=None):
        super(ConversationsListQWidget, self).__init__(parent)

        self.row = QVBoxLayout()

        title_length = 24
        if (len(title) > title_length):
            title = title[0:title_length - 3] + "..."

        title_font = QFont("Sans Serif", 10)
        title_label = QLabel(title)
        title_label.setFont(title_font)
        self.row.addWidget(title_label)

        preview_length = 28
        if (len(recent_message) > preview_length):
            recent_message = recent_message[0:preview_length - 3] + "..."

        preview_font = QFont("Sans Serif", 9)
        preview_label = QLabel(recent_message)
        preview_label.setFont(preview_font)
        preview_label.setStyleSheet("QLabel {color: #555555;}")
        self.row.addWidget(preview_label)

        self.setLayout(self.row)


def get_fb_dir():
    data_dir = "../data"
    fb_dir = None
    for dirname in next(os.walk(data_dir))[1]:
        if (dirname[0:9] == "facebook-"):
            fb_dir = data_dir + "/" + dirname
    return fb_dir


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

        # No title if conversation is with a deleted user
        title = messages_data.get("title", "Facebook User")

        preview_message_dict = messages_data["messages"][0]
        preview_message = preview_message_dict.get("content", "(No messages)")

        conversations.append(ConversationPreview(title, preview_message))
    return conversations


def populate_conversations_list(ui, conversations):
    for conversation in conversations:
        widget = ConversationsListQWidget(conversation.title,
                                          conversation.preview_message)

        item = QListWidgetItem(ui.conversationsList)
        item.setSizeHint(widget.sizeHint())

        ui.conversationsList.addItem(item)
        ui.conversationsList.setItemWidget(item, widget)


if (__name__ == "__main__"):
    app = QApplication(sys.argv)

    fb_dir = get_fb_dir()
    if (fb_dir is None):
        print("Facebook archive directory not found.")
        exit()

    print("Facebook directory:", fb_dir)

    conversations = get_conversations_list(fb_dir)
    print("Loaded conversations list.")

    window = ConversationsQMainWindow(conversations)
    window.show()

    sys.exit(app.exec_())
