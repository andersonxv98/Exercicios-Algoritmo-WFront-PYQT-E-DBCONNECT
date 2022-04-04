

import pyqtgraph as pg
from PyQt6.QtGui import QWindow
from PyQt6.QtWidgets import QWidget
from pyqtgraph import PlotWidget


class Grafico(pg.PlotWidget):
    def __init__(self):
        super().__init__()


    def Plotar(self, arr_customana, arr_qttcustomana):

        plt = pg.plot(arr_customana,arr_qttcustomana, tittle = "titutlo", pen="r")
        return plt