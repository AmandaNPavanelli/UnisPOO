# -*- coding: utf-8 -*-
############################################################
### Programa para calcular o IMC de uma pessoa com base
### nas suas medidas corporais: Altura e Peso
### Amanda Pavanelli, Salvador, BA, Brasil - Maio, 2021
############################################################
### Importando Bibliotecas Necessárias
from PyQt5 import QtCore, QtGui, QtWidgets

### Classe para cada pessoa que interagir com a calculadora
class Pessoa:
    def __init__(self, N, H, W):
        self.nome = N
        self.altura = H
        self.peso = W
        self.imc = (W)/(H*H)
        if self.imc < 17:
            self.cond = "muito abaixo do peso ideal."
        elif self.imc >= 17 and self.imc < 18.49:
            self.cond = "abaixo do peso ideal."
        elif self.imc >= 18.49 and self.imc < 24.99:
            self.cond = "no seu peso ideal."
        elif self.imc >= 24.99 and self.imc < 29.99:
            self.cond = "acima do peso ideal."
        elif self.imc >= 29.99 and self.imc < 34.99:
            self.cond = "com obesidade nível 1."
        elif self.imc >= 34.99 and self.imc < 39.99:
            self.cond = "com obesidade nível 2."
        elif self.imc >= 39.99:
            self.cond = "com obesidade mórbida."

### Criando o objeto para a janela interativa - GUI
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 480)
        MainWindow.setStyleSheet("background-color:rgb(127, 127, 127)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 410, 100, 35))
        self.pushButton.setStyleSheet("background-color:rgb(255, 170, 255)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 360, 151, 35))
        self.pushButton_2.setStyleSheet("background-color:rgb(255, 170, 255)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 360, 161, 35))
        self.pushButton_3.setStyleSheet("background-color:rgb(255, 170, 255)")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 140, 211, 51))
        self.lineEdit.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 210, 211, 51))
        self.lineEdit_2.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 290, 451, 51))
        self.lineEdit_3.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 150, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 70, 211, 51))
        self.lineEdit_4.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 220, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 80, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 10, 501, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

### Definindo as atividades dos buttons
        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton_3.clicked.connect(self.lineEdit_4.clear)
        self.pushButton_3.clicked.connect(self.lineEdit.clear)
        self.pushButton_3.clicked.connect(self.lineEdit_2.clear)
        self.pushButton_3.clicked.connect(self.lineEdit_3.clear)
        self.pushButton_2.clicked.connect(self.calculo)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

## Definindo os nomes impressos nos buttons
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Desligar"))
        self.pushButton_2.setText(_translate("MainWindow", "Calcular IMC"))
        self.pushButton_3.setText(_translate("MainWindow", "Limpar Dados"))
        self.label.setText(_translate("MainWindow", "ALTURA (cm)"))
        self.label_2.setText(_translate("MainWindow", "PESO (kg)"))
        self.label_3.setText(_translate("MainWindow", "NOME"))
        self.label_4.setText(_translate("MainWindow", "CALCULADORA DE IMC - VIVA MELHOR!"))

## Function para calcular o IMC do usuario
    def calculo(self):
        nome = self.lineEdit_4.text()
        hm = float(self.lineEdit.text())/100.0
        wg = float(self.lineEdit_2.text())
        ps = Pessoa(nome, hm, wg)
        self.lineEdit_3.setText("%s, seu imc = %.2f, você está %s" %(ps.nome, ps.imc, ps.cond))

## Executando a janela visual - GUI
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

### FIM
