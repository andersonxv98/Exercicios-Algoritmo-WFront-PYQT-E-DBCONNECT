from Models.Deck import DeckModel


class CartaModel():
    def __init__(self, vermelho, branco, verde, azul, preto, non):
        super().__init__()
        self.vermelho = vermelho
        self.branco = branco
        self.verde = verde
        self.azul = azul
        self.preto = preto
        self.non = non
        self.valorGeralDessaCarta =(vermelho + branco + verde + azul +preto +non)

