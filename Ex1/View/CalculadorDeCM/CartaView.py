from PyQt6.QtWidgets import QMainWindow, QLineEdit, QLabel, QVBoxLayout, QWidget, QPushButton

from Controllers.ControllDeck import ControllDeck


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

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)


    def InsereNoDeck(self):
        controllDeck = ControllDeck()
        print("Inserindo no deck")
