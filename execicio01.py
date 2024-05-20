# Esse exercício tem a finalidade de Solicitar 
# Dados de um usuario e exibilo na tela.

# Esse trecho de codigo solicita informações 
# Do usuario e armazena em variaveis.

print('--------------------------------------------------------')
nome = input('Informe seu nome: ')
sobrenome = input('Informe seu sobrenome: ')
idade = int(input('Informe sua idade: '))
datanas = (2024 - idade)
altura =float(input('Informe sua altura: '))
print('--------------------------------------------------------')

# Nessa parte o programa vai exibir os dados
# Solicitado 

print('Prazer: ',nome+sobrenome)
print('Sua idade é:',idade)
print('Sua data de nascimento é: ',datanas)
print('Você tem: ',altura,'De altura')
print('---------------------------------------------------------')



