from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QLayout

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
        self.layoutzero = QVBoxLayout()


        arrae = []
        for value in self.vet_tb.values():
            value.setMaximumWidth(100)
            arrae.append(value)

        print(arrae)
        i = 0
        for lb in self.vet_lb.values():
            lb.setFont(QFont("Times", 18))
            lb.adjustSize()
            lb.maximumWidth()
            self.layout.addWidget(lb)
            self.layout.addWidget(arrae[i])
            i+= 1

        self.butao = QPushButton("Inserir No Deck")
        self.butao.clicked.connect(self.InsereNoDeck)
        self.butao.setMaximumHeight(200)

        self.butaoclear = QPushButton("LimparDeck")

        self.butaoclear.clicked.connect(self.LimparDeck)






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
        self.layoutHorizontalTBandGraphs = QHBoxLayout()
        self.layoutfilhoGraphics = QVBoxLayout()

        self.layoutfilhoGraphics.addWidget(self.graphic)
        self.layoutfilhoGraphics.addWidget(self.graphicLine)


        self.layoutHorizontalTBandGraphs.addLayout(self.layout)
        self.layoutHorizontalTBandGraphs.addLayout(self.layoutfilhoGraphics)

        self.layoutzero.addLayout(self.layoutHorizontalTBandGraphs)
        self.layoutzero.addWidget(self.butao)



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

        self.vet_valoresBrutosView ={
            0 : QLabel("0"),
            1: QLabel("0"),
            2: QLabel("0"),
            3: QLabel("0"),
            4: QLabel("0"),
            5: QLabel("0"),
            6: QLabel("0")
        }



        self.layoutInfo = QHBoxLayout()


        for label in self.vet_valoresBrutosView.values():
            label.setFont(QFont("Times",16))
            self.layoutInfo.addWidget(label)

        for lb in self.vet_lb.values():

            lb.setFont(QFont("Times", 18))
            lb.adjustSize()
            self.layout5.addWidget(lb)


        self.layoutInfo.addLayout(self.layout5)

        self.layout6.addLayout(self.layout4)
        self.layout6.addLayout(self.layoutInfo)

        self.layoutzero.addLayout(self.layout6)

        self.layoutzero.addWidget(self.butaoclear)

        container = QWidget()
        container.setLayout(self.layoutzero)
        self.setCentralWidget(container)

    def InsereNoDeck(self):
        controllDeck = self.Controller
        print("Inserindo no deck")

        vet_aux = []
        for val in self.vet_tb.values():
            trueVal = 0
            try:
                trueVal = int(val.text())
            except:
                print("não foi possivel converter, valor padrão settado")
            vet_aux.append(trueVal)

        vermelho = vet_aux[0]
        branco =  vet_aux[1]
        verde =  vet_aux[2]
        azul =  vet_aux[3]
        preto =  vet_aux[4]
        non =  vet_aux[5]

        if (sum(vet_aux)<=0):
            print("VALORES IGUAIS OU MENORES A ZERO COMO CUSTO DE MANA ERROR")
            return



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

        for i in range(self.vet_valoresBrutosView.__len__()):
            self.vet_valoresBrutosView[i].setText(str(y[i]))
        print("PRINTIN: ", x)
        print("PRINTIN: ", y)



        self.graphic.clear()
        self.graphicLine.clear()
        self.graphic.Plotar(x, y)
        self.graphicLine.Plotar(x,y)

    def LimparDeck(self):
        self.Controller.ResetDeck()
        self.graphic.clear()
        self.graphicLineç.clear()
        self.vet_segundolado["NTERRENOS"].setText("Cartas não terrenos: " )
        self.vet_segundolado["TOTAL CARTAS"].setText("Total de Cartas No Deck: " )
        self.vet_segundolado["TERRENOS"].setText("Total de Terrenos: " )
        self.vet_lb["lb_vermelho"].setText("Terrenos Vermelhos: " )
        self.vet_lb["lb_branco"].setText("Terrenos Branco: " )
        self.vet_lb["lb_verde"].setText("Terrenos verde: " )
        self.vet_lb["lb_azul"].setText("Terrenos azul: " )
        self.vet_lb["lb_preto"].setText("Terrenos Preto: " )
        for i in range(self.vet_valoresBrutosView.__len__()):
            self.vet_valoresBrutosView[i].setText(str(0))
        for val in self.vet_tb.values():
            val.setText('')

