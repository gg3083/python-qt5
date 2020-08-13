import sys
from PyQt5.QtWidgets import QApplication

from index import MyIndexWidows

#
# class MyIndexWidows(QMainWindow):
#     def __init__(self):
#         super(MyIndexWidows, self).__init__()
#         self.ui = Ui_IndexWindow()
#         self.ui.setupUi(self)
#
#     def open(self):
#         self.show()
#         self.container = MyContainerWidows()
#         self.container.hide()
#
#
# class MyContainerWidows(QMainWindow):
#     def __init__(self):
#         super(MyContainerWidows, self).__init__()
#         self.ui = Ui_ContainerWindow()
#         self.ui.setupUi(self)
#
#     def open(self):
#         self.show()
#         self.index = MyIndexWidows()
#         self.index.hide()


if __name__ == '__main__':

    app = QApplication(sys.argv)

    index = MyIndexWidows()

    index.show()

    # index.ui.pushButton.clicked.connect(index.getData)
    # container.ui.pushButton_3.clicked.connect(index.open)

    sys.exit(app.exec_())
