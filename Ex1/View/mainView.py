from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QTabWidget

from Dependencies.viewDependencies import *
from View.CirculoVIew import CirculoViewClass
from View.RetanguloView import RetanguloViewClass


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Conjunto de Exercicios em Um App")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.South)
        tabs.setMovable(True)
        f = QFont("Helvetica")
        tabs.setFont(f)

        _tab = RetanguloViewClass()
        tabs.addTab(_tab, "Retangulo")
        _tab = CirculoViewClass()
        tabs.addTab(_tab, "Circulo")





        self.setCentralWidget(tabs)
