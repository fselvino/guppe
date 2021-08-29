"""
Recenbendo dados dos usuários
input() -> Todo dado recebido via input é do tipo String
Em Python, string é tudo que estiver entre:
-Aspas simples
-Aspas duplas
-Aspas simples triplas
-Aspas duplas triplas
Exemplos

    -Aspas simples -> 'Angelina Jolie'
    -Aspas dulas -> "Angelina Jolie"
    -Aspas simples triplas -> '''Angelina Jolie'''
"""
# -Aspas duplas tripas -> """Angelina Jolie"""


# Entrada de dados
# print('Qual é seu nome? ')
# nome = input()  # -> Entrada

nome = input('Qual seu nome? ')

# Exemplo de print 'antigo' 2.x
# print('Seja bem-vindo(a) %s' % nome)

# Exemplo de print 'moderno' criado a partir das versões 3.x
# print(' Seja bem-vindo(a) {0} '.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem-vindo(a) {nome}')

# print('Qual sua idade? ')
idade = int(input('Qual sua idade? '))


# Processamento

# Saida de dados
# Exemplo de print 'antigo' 2.x
# print('A %s tem %s anos' % (nome,  idade))


# Exemplo de print 'moderno' criado a partir das versões 3.x
# print('A {0} tem {1} anos'. format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f'A {nome} tem {idade} anos')  # f no inicio significa format

"""
# int(idade) => cast
Cast é a 'conversão de um tipo de dado para outro
"""
print(f'A {nome} nasceu em {2021 - idade} anos')


