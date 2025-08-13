#A função input() permite a entrada de dados pelo usuario
#Ex:
input('Texto que aparece para o usuario: ')

# Por padrão o input salva os dados inseridos como texto
nome = input('Digite o seu nome: \n')
print(type(nome))# A função Type() mostra o tipo de dado

# para salvar como inteiro usamos a função int(input())
idade = int(input('Digite a sua idade:\n'))
print(type(idade))

#Para salvar como decimal usamos a função float(input())
altura = float(input('Digite a sua altura:\n'))
print(type(altura))

peso = float(input('Digite o seu peso?\n'))
print(type(peso))

#Desafio
aresta = float(input('Digite o valor da aresta '))
volume = aresta**3
print(volume)
# Corrigido
# f - string ajuda a formatar o texto
#quando for exibir a variavel, calcular ou formatar
#print(f'volume:{aresta**3:.2f}') #:.2 define o numero de casas decimais.

#Desafio
tabuada= int(input('Digite o numero multiplicador'))
#Corrigido
#print(f' {tabuada} x1 = {tabuada*1}')
#print(f' {tabuada} x2 = {tabuada*2}')
#print(f' {tabuada} x3 = {tabuada*3}')
#print(f' {tabuada} x4 = {tabuada*4}')
#print(f' {tabuada} x5 = {tabuada*5}')
#print(f' {tabuada} x6 = {tabuada*6}')
#print(f' {tabuada} x7 = {tabuada*7}')
#print(f' {tabuada} x8 = {tabuada*8}')
#print(f' {tabuada} x9 = {tabuada*9}')
#print(f' {tabuada} x10 = {tabuada*10}')

#Desafio
ano = int(input('Digite o seu ano de nascimento: '))
idade = 2025 - ano
print(idade)

'''
Corrigido
ano_nascimento = int(input('Digite o seu ano de nascimento: '))
ano_atual = 2025
print(f'Idade: {ano_atual - ano_nascimento}')
'''

# Usando a Biblioteca
import datetime # Traz todas as funções
from datetime import date # Traz apenas a função ou funções especificas, nesse caso a data
ano_nascimento = int(input('Informe o seu ano de nascimento:'))
ano_atual= date.today().year # year - month - day / Busca a data da sua máquina PC
print(f'Idade: {ano_atual - ano_nascimento}')
