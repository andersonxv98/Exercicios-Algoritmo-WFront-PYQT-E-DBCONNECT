from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtWidgets import *

from Controllers.NgControll import  CalculoCirculo
from Controllers.PDOController import PDOcontroller


class CirculoViewClass(QMainWindow):
    def __init__(self):
        validator = QDoubleValidator()
        super().__init__()
        self.lb_r_circulo = QLabel("Raio")

        self.tb_r_circulo = QLineEdit()
        self.tb_r_circulo.setValidator(validator)


        self.lb_perimetro = QLabel("perimetro")


        self.button = QPushButton("Calcular")
        self.button.clicked.connect(self.ChamaController)

        self.button2 = QPushButton("Salvar")
        self.button2.clicked.connect(self.GravarNoDb)

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.lb_r_circulo)
        self.layout.addWidget(self.tb_r_circulo)


        self.layout.addWidget(self.button)
        self.layout.addWidget(self.lb_perimetro)

        self.layout.addWidget(self.button2)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)


        self.raio = 0
        self.perimetro =0


    def ChamaController(self):
        print("Entrou na função chamacontroller")
        raio = self.tb_r_circulo.text()
        perimetro = CalculoCirculo(raio)
        print("ultimo print: ",perimetro)
        self.raio = raio
        self.perimetro = perimetro
        self.lb_perimetro.setText("Perimetro: "+str(perimetro))
        #self.lb_diagonal.setText(diagonal)

    def GravarNoDb(self):
        raio = self.raio

        perimetro = self.perimetro

        print("base: ", raio, "  ALtura: ", perimetro)
        e = PDOcontroller()
        f = e.GetPDOCon()
        f.RegistCirculoDb(raio,perimetro)