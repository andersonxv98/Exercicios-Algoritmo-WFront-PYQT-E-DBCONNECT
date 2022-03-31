from Models.Circulo import CirculoCLass

from Models.Retangulo import *

class valorRetangulo:
    def __init__(self, wbase, altura):
        super().__init__()
        self.base = wbase
        self.altura = altura
        self.perimetro =0
        self.area =0
        self.diagonal =0
        self.CalculoRetangulo()


    def CalculoRetangulo(self):
        print("entrou Calculo REtangulo controller")

        _ret = RetanguloClass(float(self.base), float(self.altura))
        print(_ret)
        perimetro = _ret.CalculoPerimetro()

        area = _ret.CalculoArea()
        diagonal =_ret.CalculoDiagonal()
        print(perimetro, area, diagonal)

        self.perimetro = perimetro
        self.area = area
        self.diagonal = diagonal



def CalculoCirculo(raio):
    print("entrou Calculo REtangulo controller")
    _ret = CirculoCLass(float(raio))
    print(_ret)
    perimetro = _ret.CalculoPerimetro()


    return perimetro
