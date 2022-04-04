
class DeckModel():
    def __init__(self):
        super(DeckModel, self).__init__()
        self.List_nonlands = []
        self.List_lands = []
        self.arr_custoMana = {
            1 : 0,
            2 : 0,
            3 : 0,
            4 : 0,
            5 : 0,
            6 : 0,
            7: 0,
            8 : 0,
            9 : 0,
        }

    def AddonListNonLands(self, Carta):
        self.List_nonlands.append(Carta)
        print(self.List_nonlands)
        return

    def Count_List_nonland(self):
        return  self.List_nonlands.__len__()

    def Count_num_Mana_especificaVermelho(self):
        soma_vermelho = 0
        for card_nonLand in self.List_nonlands:
            soma_vermelho +=card_nonLand.vermelho
        print("TOtal de mana Vermelha: ",soma_vermelho)
        return soma_vermelho

    def Count_num_Mana_especificaBranco(self):
        soma_Branco = 0
        for card_nonLand in self.List_nonlands:
            soma_Branco += card_nonLand.branco
        print("TOtal de mana Branco: ", soma_Branco)
        return soma_Branco

    def Count_num_Mana_especificaVerde(self):
        soma_verde = 0
        for card_nonLand in self.List_nonlands:
            soma_verde += card_nonLand.verde
        print("TOtal de mana VErde: ", soma_verde)
        return soma_verde

    def Count_num_Mana_especificaAzul(self):
        soma_Azul = 0
        for card_nonLand in self.List_nonlands:
            soma_Azul += card_nonLand.azul
        print("TOtal de mana Azul: ", soma_Azul)
        return soma_Azul

    def Count_num_Mana_especificaPreto(self):
        soma_Preto = 0
        for card_nonLand in self.List_nonlands:
            soma_Preto += card_nonLand.preto
        print("TOtal de mana Preto: ", soma_Preto)
        return soma_Preto

    def Count_num_Mana_especificaIncolor(self):
        soma_Incolor = 0
        for card_nonLand in self.List_nonlands:
            soma_Incolor += card_nonLand.non
        print("TOtal de mana Incolor: ", soma_Incolor)
        return soma_Incolor

    def Count_num_CustoMana(self):
        for card_nonLand in self.List_nonlands:
            valor = card_nonLand.valorGeralDessaCarta
        for key in self.arr_custoMana.keys():
            if(valor == key):
                self.arr_custoMana[key] += 1

        print("Arras_Custo de mana : ", self.arr_custoMana)
        return self.arr_custoMana