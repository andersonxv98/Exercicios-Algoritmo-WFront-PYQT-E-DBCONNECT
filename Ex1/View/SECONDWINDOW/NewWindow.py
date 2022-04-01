from PyQt6.QtGui import QWindow
from PyQt6.QtWidgets import QVBoxLayout, QLabel, QWidget, QMainWindow, QDialog


class novaWindClass(QDialog):
    def __init__(self):
        super().__init__()
        self.layourt  = QVBoxLayout()
        self.label =QLabel("ISSO AQUI É UMA NOVA JANELA")
        self.layourt.addWidget(self.label)
        self.setLayout(self.layourt)


    def Intanciou(self):
        print("Instancioou")
        self.show()
