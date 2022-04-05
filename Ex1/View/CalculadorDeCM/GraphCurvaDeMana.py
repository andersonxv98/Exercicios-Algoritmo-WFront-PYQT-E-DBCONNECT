import symbol

import pyqtgraph as pg
from PyQt6 import QtCore



class Grafico(pg.PlotWidget):
    def __init__(self):
        super().__init__()
        self.setBackground("#363636")
        self.setTitle("CURVA DE MANA O MELHOR MODO DE COLOCAR sEUS INIMIGOS PRA CHORAR", color="#2BFFAC", size="10pt" )
        #self.graphWidget.setTitle("<span style=\"color:blue;font-size:30pt\">Your Title Here</span>")
        styles = {'color': '#2BFFAC', 'font-size': '20px'}
        self.setLabel('left', 'Quantidade De Cards', **styles, name="Qtt")
        self.setLabel('bottom', 'Custo Geral Da CArta', **styles, name="CM")
        self.addLegend()
        self.showGrid(x=True, y=True)
        self.setXRange(0,9, padding=0)

    def Plotar(self, arr_customana, arr_qttcustomana):


        #pen = pg.mkPen(color="#2BFFAC", width=4, style=QtCore.Qt.PenStyle.DashDotDotLine)



        #["GRAFICO EM LINHAS"]
        #plt = self.plot(arr_customana, arr_qttcustomana, tittle = "titutlo",name="GastoDeMana",pen=pen, symbol='o', symbolSize=10, symbolBrush='#35CCF5')
        #plt = self.plot(arr_customana, arr_qttcustomana, tittle="titutlo", name="GastoDeMana", pen=pen, symbol='o', symbolSize=10, symbolBrush='#35CCF5')


        #CRAFICO em coluna
        bargraph = pg.BarGraphItem(x=arr_customana, height=arr_qttcustomana, width=0.6, brush='g', style="default")

        self.addItem(bargraph)
        self.setOpacity(0.3)
        return self