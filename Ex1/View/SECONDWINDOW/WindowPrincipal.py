from PyQt6.QtWidgets import QPushButton, QMainWindow

from View.SECONDWINDOW.NewWindow import novaWindClass


class WindClass(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button = QPushButton("Push for Windows nunes")
        self.button.clicked.connect(self.AmostraissoAquiPranois)
        self.setCentralWidget(self.button)

    def AmostraissoAquiPranois(self):
        print("ENtrou no AMOSTRAISSO AQUIPRANOIS")
        novaWinderson = novaWindClass()
        novaWinderson.showFullScreen()
