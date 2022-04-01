from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel


class DialogCustom(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HELLO FROM THE OTHERSIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIDE")

        Qtbtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

        self.buttonbox = QDialogButtonBox(Qtbtn)
        self.buttonbox.accepted.connect(self.Aceitar)
        self.buttonbox.rejected.connect(self.Rejeitar)

        self.layout =QVBoxLayout()
        message = QLabel("VOce aceita Jesus Na sua vida??")

        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonbox)

        self.setLayout(self.layout)


    def Aceitar(self):
        print("curta e compartilhe para 10 pessoas")
        self.close()

    def Rejeitar(self):
        print("\só olhe")
        self.close()