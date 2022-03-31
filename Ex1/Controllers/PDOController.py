

import mysql.connector

class PDOcontroller():
    def __init__(self):
        super().__init__()
        self.db = ""
        self.mdb = ""
        self.condb= self.Con()
    def Con(self):
        try:
           mydb = mysql.connector.connect(
               host="localhost",
               user="root",
               password="admin",
               database="pythonacobra"
           )
           print(mydb)
           self.db = mydb

           return self.db
        except:
            return  "não Conectado"

    def GetPDOCon(self):
        return self
    def Login(self,usuario, senha):
        query = "SELECT idusuario FROM usuario WHERE login = " + "'" + usuario + "'" + " and senha = " + "'" + senha + "'"
        ("Entrou na função login da classe PDO CONTROLLER")
        mycursor = self.db.cursor()

        mycursor.execute(query)

        myresult = mycursor.fetchall()

        for x in myresult:
            print("resultado da busca do db: ", x)
        mycursor.close()

    def RegisRetangulDb(self, base, altura, perimetro, area, diagonal):
        print("entrou na função regisretanguldb")
        query = "INSERT INTO pythonacobra.retangulo (base, altura, Perimetro, area, diagonal) VALUES (" + str(base) + ","+str(altura)+","+str(perimetro)+","+str(area)+","+str(diagonal)+")";
        s = self.condb
        mycursor = s.cursor()
        print(query)
        try:
            mycursor.execute(query)
            s.commit()
            mycursor.close()
            #mycursor.execute(query)
            print("Sucesso DB")
        except:
            print(query)
    def RegistCirculoDb(self, raio, perimetro):
        print("entrou na função regisretanguldb")
        query = "INSERT INTO pythonacobra.circulo (raio, perimetro) VALUES (" + str(raio)+","+str(perimetro)+")"
        s = self.condb
        mycursor = s.cursor()
        print(query)
        try:
            mycursor.execute(query)
            s.commit()
            mycursor.close()
            # mycursor.execute(query)
            print("Sucesso DB")
        except:
            print(query)

