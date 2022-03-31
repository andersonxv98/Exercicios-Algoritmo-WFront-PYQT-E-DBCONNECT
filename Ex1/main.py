import sys
from Dependencies.mainDependencies import *
from View.Layout import Layout


app = QApplication(sys.argv)

window = Layout()
window.activ_tab_1()

app.exec()
#Lembrar de Implementarr a Classe DAO -> DB