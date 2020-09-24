import maya_v2
import math
import cv2
import numpy as np

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'CARLOS BUSTILLO - NUMEROS MAYAS'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)
        
        # Create a button in the window
        self.button = QPushButton('Crear Imagen', self)
        self.button.move(20,80)
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
    
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        
        #Corroborar que el numero ingresado es un entero
        try:
            entero = int(textboxValue)
            absoluto = abs(entero)
            #Corroborar que es un numero natural
            if entero == absoluto: 
                if entero > 159999:
                    QMessageBox.question(self, 'Error', "Escribiste un valor mayor al permitido", QMessageBox.Ok, QMessageBox.Ok)
                else:
                    QMessageBox.question(self, 'OK', "Espera mientras creamos la imagen", QMessageBox.Ok, QMessageBox.Ok)
                    maya_v2.mayaMain(entero)
                    QMessageBox.question(self, 'Listo', "Su imagen ha sido creada correctamente", QMessageBox.Ok, QMessageBox.Ok)
            else:
                QMessageBox.question(self, 'Error', "Esto no es un número natural", QMessageBox.Ok, QMessageBox.Ok)
        except ValueError:
            QMessageBox.question(self, 'Error', "Esto no es un número natural", QMessageBox.Ok, QMessageBox.Ok)
	
        self.textbox.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) 
