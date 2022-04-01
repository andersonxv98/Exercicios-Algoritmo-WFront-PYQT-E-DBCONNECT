
class DeckModel():
    def __init__(self):
        super(DeckModel, self).__init__()
        self.List_nonlands = []
        self.List_lands = []

    def AddonListNonLands(self, Carta):
        self.List_nonlands.append(Carta)
        print(self.List_nonlands)
        return

    def Count_List_nonland(self):
        return  self.List_nonlands.__len__()