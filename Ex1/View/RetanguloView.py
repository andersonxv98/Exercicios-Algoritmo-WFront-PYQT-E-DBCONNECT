from PyQt6.QtGui import QAction, QValidator, QDoubleValidator
from PyQt6.QtWidgets import *


from Controllers.NgControll import  valorRetangulo
from Controllers.PDOController import PDOcontroller

from View.Login import LoginClass


class RetanguloViewClass(QMainWindow):
    def __init__(self):

        super().__init__()
        validator = QDoubleValidator()
        self.lb_b_retangulo = QLabel("base")
        self.tb_b_retanqgulo = QLineEdit()
        self.tb_b_retanqgulo.setValidator(validator)
        self.lb_a_retangulo = QLabel("altura")
        self.tb_a_retangulo = QLineEdit()
        self.tb_a_retangulo.setValidator(validator)

        self.lb_area = QLabel("area")
        self.lb_perimetro = QLabel("perimetro")
        self.lb_diagonal = QLabel("Diagonal")

        self.button = QPushButton("Calcular")
        self.button.clicked.connect(self.ChamaController)

        self.button2 = QPushButton("Salvar")
        self.button2.clicked.connect(self.SalvaOnDB)

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.lb_b_retangulo)
        self.layout.addWidget(self.tb_b_retanqgulo)
        self.layout.addWidget(self.lb_a_retangulo)
        self.layout.addWidget(self.tb_a_retangulo)

        self.layout.addWidget(self.button)
        self.layout.addWidget(self.lb_perimetro)
        self.layout.addWidget(self.lb_area)
        self.layout.addWidget(self.lb_diagonal)

        self.layout.addWidget(self.button2)


        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
        self.base= 0
        self.altura =0
        self.perimetro=0
        self.area=0
        self.diagonal =0




    def ChamaController(self):
        print("Entrou na função chamacontroller")
        val_base = self.tb_b_retanqgulo.text()
        val_Altura = self.tb_a_retangulo.text()
        print(val_base)
        print(val_Altura)
        retang = valorRetangulo(val_base, val_Altura)
        perimetro = retang.perimetro
        area = retang.area
        diagonal = retang.diagonal
        self.base = val_base
        self.altura = val_Altura
        self.perimetro = perimetro
        self.area = area
        self.diagonal = diagonal
        print("ultimo print: ",perimetro, area, diagonal)
        self.lb_area.setText("Area: " +str(area))
        self.lb_perimetro.setText("Perimetro: "+str(perimetro))
        self.lb_diagonal.setText("Diagonal: "+str(diagonal))
        #self.lb_diagonal.setText(diagonal)

    def SalvaOnDB(self):
        base= self.base
        altura = self.altura
        perimetro = self.perimetro
        area = self.area
        diagona = self.diagonal
        print("base: ",base,"  ALtura: ", altura, "   Diagonal : ", diagona)
        e = PDOcontroller()
        f = e.GetPDOCon()
        f.RegisRetangulDb(base, altura, perimetro, area, diagona)

