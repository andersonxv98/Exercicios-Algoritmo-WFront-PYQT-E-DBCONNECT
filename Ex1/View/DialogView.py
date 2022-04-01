from PyQt6.QtGui import QKeyEvent, QInputEvent
from PyQt6.QtWidgets import QMainWindow, QPushButton, QDialog

from View.insiderDialog import DialogCustom


class DialogoClass(QMainWindow):
    def __init__(self):
        super(DialogoClass, self).__init__()

        self.setWindowTitle("Violência Nunca é a Resposta")

        butao = QPushButton("YAMETTTE!!!!")
        butao.clicked.connect(self.ClicouNoBotao)


        self.setCentralWidget(butao)

    def ClicouNoBotao(self,s):
        print("Clicou", s)

        dialogWindow = DialogCustom()

        dialogWindow.exec()