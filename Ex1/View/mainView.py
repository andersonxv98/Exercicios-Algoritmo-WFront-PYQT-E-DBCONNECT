from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QTabWidget

from Dependencies.viewDependencies import *
from View.CirculoVIew import CirculoViewClass
from View.DialogView import DialogoClass
from View.RetanguloView import RetanguloViewClass
from View.SECONDWINDOW.NewWindow import novaWindClass
from View.SECONDWINDOW.WindowPrincipal import WindClass


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
        _tab = DialogoClass()
        tabs.addTab(_tab, "Diálogo")
        _tab = WindClass()
        tabs.addTab(_tab, "Nova windows segundo o GU}I")




        self.setCentralWidget(tabs)
