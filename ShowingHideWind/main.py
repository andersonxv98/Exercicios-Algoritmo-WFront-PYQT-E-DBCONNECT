import sys

from PyQt6.QtWidgets import *

from Views.MainView import MainView

app = QApplication(sys.argv)

window = MainView()
window.show()

app.exec()