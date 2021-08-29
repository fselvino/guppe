"""
PEP8 - Python Enhancement Proposal
São propostas de melhorias para a liguagem Python
The Zen of Python
import this
A ideia da PEP8 é que possamos escrever código python de forma Pythônica.

[1] - Utilize camel case para nomes de classes;
class Calculadora:
    pass


class CalculadoraCientifica:
    pass


[2] - Utilize nomes em minusculos, separados por underline para funções ou variáveis
def soma():
    pass


def soma_dois():
    pass

 numero = 5

numer_impar = 7

[3] - Utilize 4 espaços para indentação

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
- Separar funçoes e definiçoes de classe com duas linhas em braco
-Metodos dentro de uma classe devem se separados com uma úunica linha em branco

[5] - Imports
- Imports devem ser sempre feitos em linhas separadas

# Import Errado
import sys, os

# import Correto
import sys
import os

# Não há problemas em utlizar
from types import StringTypes, ListTypes

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer
from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstring e
# antes de constantes ou variáveis globais.

[6] - Espaços em expressões e instruções

# não faça:
funcao( algo[ 1 ], { outro: 2 } )

# Faça:
funcao(algo[1], {outro: 2})

# Não faça:
algo (1)

# Faça:
algo(1)

# Não faça:
dict ['chave'] = lista [indice]

# Faça:
dict['chave'] = lista[indice]

# Não faça:
x =             1
y =             3
variavel_loga = 5

# Faça:
x = 1
y = 5
variavel_loga = 7

[7] - Termine sempre um instrução com uma nova linha
"""
import this


