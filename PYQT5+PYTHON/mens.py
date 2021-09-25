from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *



from mensagem import Ui_Dialog


class TelaPrimeira(QDialog):

    def __init__(self, *args, **argvs):
        super().__init__(*args, **argvs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.botao)
        self.ui.checkBox.clicked.connect(self.botao_checkbox)


    def botao(self):
        return self.insira_mensagem()

    def insira_mensagem(self):
        mensagem = self.ui.lineEdit.text()
        caixaa = self.ui.checkBox.text()

        if mensagem == "":
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Espaço em branco")

            iniciar = msg.exec_()

        elif mensagem:
            msg = QMessageBox()
            msg.setWindowTitle("Mensagem")
            msg.setText(mensagem)

            iniciar_mensagem = msg.exec_()

        else:
            print("Tente novamente mais tarde")


    def botao_checkbox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Caixa de erro")
        msg.setText("A caixa de erro e esta")
        msg.Icon(QMessageBox.Critical)
        msg.setIcon(QMessageBox.Critical)

        inicio = msg.exec_()
if __name__ == "__main__":
    import os, sys
    app = QApplication(sys.argv)
    window = TelaPrimeira()
    window.show()
    sys.exit(app.exec_())