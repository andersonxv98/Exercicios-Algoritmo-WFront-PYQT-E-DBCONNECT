
from View.Login import LoginClass
from View.mainView import MainWindow


class Layout():
    def __init__(self):
        super().__init__()


        self.MainWindExer = MainWindow()
        self.lg = LoginClass(self.MainWindExer, None)
        self.Loginview = LoginClass(self.MainWindExer, self.lg)

    def activ_tab_1(self):
        self.Loginview.show()
        #self.MainWindExer.show()

    def activ_tab_2(self):
        self.MainWindExer.show()
