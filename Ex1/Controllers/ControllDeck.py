from Models.Carta import CartaModel
from View.CalculadorDeCM.visaoGeralDeckView import DeckViewGeral


class ControllDeck():
    def __init__(self, Deck):
        super().__init__()
        self.card = None
        self.deck = Deck
        self.QttGeraldeLands = 0

    def ConstructCarta(self, vermelho, branco, verde, azul, preto, non):
        card = CartaModel(int(vermelho), int(branco), int(verde), int(azul), int(preto), int(non))
        self.card = card
        self.AddCardOnDeck()

    def AddCardOnDeck(self):
        self.deck.AddonListNonLands(self.card)
        self.CalculaSomaDasCartasNonLand()

    def CalculaSomaDaCurvaDeManaGeral(self):
       print("TESTER")


    def CalculaSomaDasCartasNonLand(self):
        val  = self.deck.Count_List_nonland()
        self.QttGeraldeLands = val
        print(val)

    def AtualizaValoresNaView(self):
        n_totaldelandsGeral = self.QttGeraldeLands
        return  n_totaldelandsGeral
