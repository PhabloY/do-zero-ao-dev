# C: \Users\user\OneDrive\Área de Trabalho\curso_python\do-zero-ao-dev
# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os

caminho = os.path.join('/Users', 'user', 'OneDrive', 'Área de Trabalho',
                       'curso_python', 'do-zero-ao-dev')
