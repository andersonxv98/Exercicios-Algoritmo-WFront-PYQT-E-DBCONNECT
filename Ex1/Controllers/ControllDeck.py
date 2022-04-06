from math import ceil

from Models.Carta import CartaModel
from View.CalculadorDeCM.GraphCurvaDeMana import Grafico
from View.CalculadorDeCM.visaoGeralDeckView import DeckViewGeral


class ControllDeck():
    def __init__(self, Deck):
        super().__init__()
        self.card = None
        self.deck = Deck
        self.QttGeraldeNonLands = 0
        self.curvaGeral = 0
        self.soma_manaGeral = 0
        self.totalManaVermelha =0
        self.totalManaBranca = 0
        self.totalManaVerde= 0
        self.totalManaAzul = 0
        self.totalManaPreta = 0
        self.totalManaIncolor = 0

        self.arr_customana = []
        self.arr_qttcustomana =[]
        self.total_de_cartas = 0
        self.lands_corrigido = 0



 #construtor


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
        self.QttGeraldeNonLands = val
        print(val)

    def AtualizaValoresNaView(self):
        n_totaldelandsGeral = self.QttGeraldeNonLands
        self.CalculaQtdGeralDeLands()
        return  n_totaldelandsGeral

    def BuscaMana(self):
        soma_manaVermelha = self.deck.Count_num_Mana_especificaVermelho()
        soma_manaBranca=  self.deck.Count_num_Mana_especificaBranco()
        soma_manaVerde =  self.deck.Count_num_Mana_especificaVerde()
        soma_manaAzul = self.deck.Count_num_Mana_especificaAzul()
        soma_manaPreta = self.deck.Count_num_Mana_especificaPreto()
        soma_manaIncolor = self.deck.Count_num_Mana_especificaIncolor()

        self.totalManaVermelha = soma_manaVermelha
        self.totalManaBranca = soma_manaBranca
        self.totalManaVerde = soma_manaVerde
        self.totalManaAzul  = soma_manaAzul
        self.totalManaPreta = soma_manaPreta
        self.totalManaIncolor = soma_manaIncolor

        self.soma_manaGeral  = soma_manaPreta + soma_manaVerde + soma_manaBranca + soma_manaAzul +soma_manaVermelha + soma_manaIncolor
        print("SOMA MANA TOTAL: ", self.soma_manaGeral)

    def CalculaQtdGeralDeLands(self):
        lands =(self.soma_manaGeral / self.QttGeraldeNonLands) * 10
        lands_corrigido = ceil(lands)
        
        total_de_cartas = lands_corrigido + self.QttGeraldeNonLands

        print("total de cartas: ",total_de_cartas)
        print("total de terrenos: ",lands_corrigido)
        self.total_de_cartas = total_de_cartas
        self.lands_corrigido = lands_corrigido
        vermelho, branco, verde, azul, preto = self.CalculaQtdEespecificadeTerrenoSP(lands_corrigido)
        return  vermelho, branco, verde, azul, preto
    def CalculaQtdEespecificadeTerrenoSP(self, landsCorrigido):
       correcaoMana = self.soma_manaGeral - self.totalManaIncolor
       percent_vermelho =(self.totalManaVermelha /correcaoMana)
       percent_branco =(self.totalManaBranca /correcaoMana)
       percent_verde =(self.totalManaVerde /correcaoMana )
       percent_azul = (self.totalManaAzul / correcaoMana)
       percent_preto= (self.totalManaPreta/correcaoMana)


       terrVemelho = percent_vermelho * landsCorrigido
       terrBranco = percent_branco  * landsCorrigido
       terrVerde =  percent_verde   * landsCorrigido
       terrAzul = percent_azul    * landsCorrigido
       terrPreto = percent_preto  * landsCorrigido

       arr_lands = [terrVemelho ,terrBranco , terrVerde, terrAzul, terrPreto]
       if (landsCorrigido < (ceil(terrVemelho) + ceil(terrBranco) + ceil(terrVerde) + ceil(terrAzul) + ceil(terrPreto))):

           print(arr_lands)
           print(max(arr_lands))
           arm = max(arr_lands)
           indice  =arr_lands.index(max(arr_lands))
           arr_lands[indice] = arm - 1
          
           print(arr_lands)

       print("n terrnos vermelhos: ", ceil(arr_lands[0]), "valor sem tratamento: ", arr_lands[0])
       print("n terrnos Branco: ", ceil(arr_lands[1]), "valor sem tratamento: ", arr_lands[1])
       print("n terrnos VErde: ", ceil(arr_lands[2]), "valor sem tratamento: ", arr_lands[2])
       print("n terrnos Azul: ", ceil(arr_lands[3]), "valor sem tratamento: ", arr_lands[3])
       print("n terrnos Preto: ", ceil(arr_lands[4]), "valor sem tratamento: ", arr_lands[4])
       return  arr_lands[0], arr_lands[1], arr_lands[2], arr_lands[3], arr_lands[4]

    def EnviarValoresParaGrafico(self):
        arr_brutoCustoMana = self.deck.Count_num_CustoMana()
        print(arr_brutoCustoMana)
        self.arr_qttcustomana = []
        self.arr_customana = []
        for value in arr_brutoCustoMana.values():
            self.arr_qttcustomana.append(value)
        for key in arr_brutoCustoMana.keys():
            self.arr_customana.append(key)

        print(self.arr_qttcustomana)
        print(self.arr_customana)

        x, y =(self.arr_customana, self.arr_qttcustomana)

        return x, y

    def ResetDeck(self):
        self.deck.LimparDeck()
        self.card = None

        self.QttGeraldeNonLands = 0
        self.curvaGeral = 0
        self.soma_manaGeral = 0
        self.totalManaVermelha = 0
        self.totalManaBranca = 0
        self.totalManaVerde = 0
        self.totalManaAzul = 0
        self.totalManaPreta = 0
        self.totalManaIncolor = 0

        self.arr_customana = []
        self.arr_qttcustomana = []
        self.total_de_cartas = 0
        self.lands_corrigido = 0