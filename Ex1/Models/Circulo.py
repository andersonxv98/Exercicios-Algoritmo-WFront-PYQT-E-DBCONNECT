class CirculoCLass:
    def __init__(self, raio):

        self.raio = raio
        self.perimetro = 0
       # self.area  = self.CalculoArea()
        #self.perimetro = self.CalculoPerimetro()
        #self.diagonal = self.CalculoDiagonal()

    def CalculoPerimetro(self):
        if(type(self.raio)== str):
            return "Valor inadequado informado"
        perimetro = 2 * (3.141529) * self.raio
        self.perimetro= perimetro
        return perimetro