import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QWidget, \
    QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QListWidgetItem
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont

from ui_mainwindow import Ui_MainWindow


class ConversationsListQWidget(QWidget):
    def __init__(self, name, bottom_text, parent=None):
        super(ConversationsListQWidget, self).__init__(parent)

        self.row = QVBoxLayout()

        name_font = QFont("Sans Serif", 10)
        name_label = QLabel(name)
        name_label.setFont(name_font)
        self.row.addWidget(name_label)

        bottom_text_font = QFont("Sans Serif", 9)
        bottom_text_label = QLabel(bottom_text)
        bottom_text_label.setFont(bottom_text_font)
        bottom_text_label.setStyleSheet("QLabel {color: #555555;}")
        self.row.addWidget(bottom_text_label)

        self.setLayout(self.row)


app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

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

entries = [
    ("Person One", "Some first text..."),
    ("Person Two", "Some second text..."),
    ("Person Three", "Some third text..."),
    ("Person Four", "Some fourth text...")
]

for e in entries:
    widget = ConversationsListQWidget(e[0], e[1])

    item = QListWidgetItem(ui.conversationsList)
    item.setSizeHint(widget.sizeHint())

    ui.conversationsList.addItem(item)
    ui.conversationsList.setItemWidget(item, widget)

window.show()
sys.exit(app.exec_())
