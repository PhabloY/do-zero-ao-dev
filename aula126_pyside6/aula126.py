import sys
from PySide6.QtWidgets import QApplication, QPushButton, QGridLayout, QWidget

app = QApplication(sys.argv)

botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 40px;')
botao.show()  # Adiciona o widget na hierarquia e exibe na janela

botao2 = QPushButton('Botao 2')
botao.setStyleSheet('font-size: 40px;')
botao2.show()

botao3 = QPushButton('Botao 3')
botao.setStyleSheet('font-size: 40px;')
botao3.show()

central_widget = QWidget()

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

central_widget.show()
app.exec()
