import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from ui_mainwindow import Ui_MainWindow

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

entries = ["test 1", "test 2", "test 3", "test 4"]
model = QStandardItemModel()
ui.conversationsList.setModel(model)
for e in entries:
    item = QStandardItem(e)
    model.appendRow(item)

window.show()
sys.exit(app.exec_())
