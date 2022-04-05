from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout

from Controllers.ControllDeck import ControllDeck
from Models.Deck import DeckModel
from View.CalculadorDeCM.GraphCurvaDeMana import Grafico
from View.CalculadorDeCM.GraphCurvaDeManaLine import GraficoLine


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

        self.butaoclear = QPushButton("LimparDeck")
        self.butaoclear.clicked.connect(self.LimparDeck)

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
        self.graphic = Grafico()
        self.graphicLine = GraficoLine()
        self.vet_segundolado = {
            "TOTAL CARTAS": QLabel("TOTAL DE CARTAS"),
            "espcamento": QLabel("|"),
            "TERRENOS": QLabel("TOTAL DE TERRENOS"),
            "espcamento2": QLabel("|"),
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
        self.layout.addWidget(self.graphic)
        self.layout.addWidget(self.graphicLine)
        self.layout.addWidget(self.butaoclear)

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
        view = self.Controller.QttGeraldeNonLands


        self.Controller.BuscaMana()

        vermelho, branco, verde, azul, preto=  self.Controller.CalculaQtdGeralDeLands()



        print("vermelho: ", vermelho)
        print("branco: ", branco)
        print("verde: ", verde)
        print("azul: ", azul)

        print("VEt_SEgundooskdaosk:  ", self.vet_segundolado["NTERRENOS"])

        totalTerrenos = self.Controller.lands_corrigido
        totaldeCartas = view + totalTerrenos

        self.vet_segundolado["NTERRENOS"].setText("Cartas não terrenos: " +str(view))
        self.vet_segundolado["TOTAL CARTAS"].setText("Total de Cartas No Deck: "+str(totaldeCartas))
        self.vet_segundolado["TERRENOS"].setText("Total de Terrenos: "+str(totalTerrenos))
        self.vet_lb["lb_vermelho"].setText("Terrenos Vermelhos: "+ str(vermelho))
        self.vet_lb["lb_branco"].setText("Terrenos Branco: " + str(branco))
        self.vet_lb["lb_verde"].setText("Terrenos verde: " + str(verde))
        self.vet_lb["lb_azul"].setText("Terrenos azul: " + str(azul))
        self.vet_lb["lb_preto"].setText("Terrenos Preto: "+ str(preto))

        self.PlotGrafico()

    def PlotGrafico(self):
        x, y, = self.Controller.EnviarValoresParaGrafico()
        self.graphic.clear()

        self.graphic.Plotar(x, y)
        self.graphicLine.Plotar(x,y)

    def LimparDeck(self):
        self.Controller.ResetDeck()
        self.graphic.clear()
        self.vet_segundolado["NTERRENOS"].setText("Cartas não terrenos: " )
        self.vet_segundolado["TOTAL CARTAS"].setText("Total de Cartas No Deck: " )
        self.vet_segundolado["TERRENOS"].setText("Total de Terrenos: " )
        self.vet_lb["lb_vermelho"].setText("Terrenos Vermelhos: " )
        self.vet_lb["lb_branco"].setText("Terrenos Branco: " )
        self.vet_lb["lb_verde"].setText("Terrenos verde: " )
        self.vet_lb["lb_azul"].setText("Terrenos azul: " )
        self.vet_lb["lb_preto"].setText("Terrenos Preto: " )


