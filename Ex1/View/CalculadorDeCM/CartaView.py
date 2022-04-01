from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout

from Controllers.ControllDeck import ControllDeck
from Models.Deck import DeckModel
from View.CalculadorDeCM.visaoGeralDeckView import DeckViewGeral


class CartaView(QMainWindow):
    def __init__(self):
        super(CartaView, self).__init__()

        self.vet_lb = {
            "lb_vermelho" : QLabel("Vermelho"),
            "lb_branco" : QLabel("Branco"),
            "lb_verde" : QLabel("Verde"),
            "lb_azul" : QLabel("Azul"),
            "lb_preto"  : QLabel("Preto"),
            "lb_non" : QLabel("Incolor")
            }

        self.vet_tb = {
            "Campovermelho": QLineEdit(),
            "Campobranco" : QLineEdit(),
            "Campoverde" : QLineEdit(),
            "Campoazul" : QLineEdit(),
            "Campopreto" : QLineEdit(),
            "Camponon" : QLineEdit()
        }
        #print(self.vet_lb.values())
        simpl = self.vet_tb.values()

        self.layout = QVBoxLayout()


        arrae = []
        for value in self.vet_tb.values():
            arrae.append(value)

        print(arrae)
        i = 0
        for lb in self.vet_lb.values():
            self.layout.addWidget(lb)
            self.layout.addWidget(arrae[i])
            i+= 1

        self.butao = QPushButton("Inserir No Deck")
        self.butao.clicked.connect(self.InsereNoDeck)

        self.layout.addWidget(self.butao)




        self.Deck = DeckModel()
        self.Controller = ControllDeck(self.Deck)

        self.vet_lb = {
            "MINIMO:  ": QLabel("Minimo de Terrenos"),
            "lb_vermelho": QLabel("Terrenos Vermelho"),
            "lb_branco": QLabel("Terrenos Branco"),
            "lb_verde": QLabel("TErrenos Verde"),
            "lb_azul": QLabel("Terrenos Azul"),
            "lb_preto": QLabel("Terrenos Preto"),
            "lb_non": QLabel("Terrenos Incolor")
        }

        # print(self.vet_lb.values())

        self.layout4 = QHBoxLayout()
        self.layout5 = QVBoxLayout()
        self.layout6 = QVBoxLayout()
        self.vet_segundolado = {
            "TOTAL CARTAS": QLabel("TOTAL DE CARTAS"),

            "TERRENOS": QLabel("TOTAL DE TERRENOS"),

            "NTERRENOS": QLabel("N Terrenos"),

        }

        for lb2 in self.vet_segundolado.values():
            lb2.setFont(QFont("Times", 20))
            self.layout4.addWidget(lb2)

        for lb in self.vet_lb.values():
            self.layout5.addWidget(lb)

        self.layout6.addLayout(self.layout4)
        self.layout6.addLayout(self.layout5)

        self.layout.addLayout(self.layout6)



        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def InsereNoDeck(self):
        controllDeck = self.Controller
        print("Inserindo no deck")
        vermelho =  self.vet_tb["Campovermelho"].text()
        branco = self.vet_tb["Campobranco"].text()
        verde = self.vet_tb["Campoverde"].text()
        azul = self.vet_tb["Campoazul"].text()
        preto = self.vet_tb["Campopreto"].text()
        non = self.vet_tb["Camponon"].text()

        controllDeck.ConstructCarta(vermelho, branco, verde, azul, preto, non)
        self.AtualizaFront()

    def AtualizaFront(self):
        view = self.Controller.QttGeraldeLands
        print("VEt_SEgundooskdaosk:  ", self.vet_segundolado["NTERRENOS"])

        self.vet_segundolado["NTERRENOS"].setText(str(view))