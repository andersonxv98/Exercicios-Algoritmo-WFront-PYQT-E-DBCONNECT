class RetanguloClass:
    def __init__(self, wbase, altura):

        self.wbase = wbase
        self.altura = altura
        self.area = 0
        self.perimetro = 0
        self.diagonal = 0

    def CalculoDiagonal(self):
        diagonal = (((self.wbase**2) + (self.altura** 2)) // 2)
        self.diagonal = diagonal
        return diagonal

    def CalculoArea(self):
        result = self.wbase * self.altura
        self.area = result
        return  result

    def CalculoPerimetro(self):
        perimetro = 2 * (self.wbase + self.altura)
        self.perimetro = perimetro
        return perimetro