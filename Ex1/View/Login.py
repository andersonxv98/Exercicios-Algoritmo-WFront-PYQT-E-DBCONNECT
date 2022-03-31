from PyQt6.QtGui import QWindow
from PyQt6.QtWidgets import *

from Controllers.PDOController import PDOcontroller




class LoginClass(QMainWindow):
    def __init__(self, MainWindow, LoginWindow):
        super().__init__()

        self.MainWindow = MainWindow
        self.LoginWind = LoginWindow
        self.conn = ""
        self.lb_usuario = QLabel("Usuario")
        self.tb_usuario = QLineEdit()

        self.lb_senha = QLabel("Senha")
        self.tb_senha = QLineEdit()



        self.button = QPushButton("Logar")
        self.button.clicked.connect(self.LoginSeasson)

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.lb_usuario)
        self.layout.addWidget(self.tb_usuario)
        self.layout.addWidget(self.lb_senha)
        self.layout.addWidget(self.tb_senha)

        self.layout.addWidget(self.button)




        self.message = self.ConnDb
        self.lb_menssagem = QLabel(str(self.message))

        self.layout.addWidget(self.lb_menssagem)


        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
        self.parm = ""
        self.ConnDb()


    def ConnDb(self):
       _conn = PDOcontroller()
       menssage =  _conn.db

       self.conn= menssage
       return menssage

    def LoginSeasson(self):
        print("Entrou na função Conectar DB")
        usuario = self.tb_usuario.text()
        senha = self.tb_senha.text()

        print(usuario)
        print(senha)
        st = PDOcontroller()
        st.Login(usuario, senha)


        #/*print("print: ",result)
        #self.message = result
        self.hide()

        self.MainWindow.show()

