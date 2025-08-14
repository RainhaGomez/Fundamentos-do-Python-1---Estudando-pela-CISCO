# O resultado "if da condição" tem de ser True para execultar os print() que estão abaixo dele e com a tabulação(espaços).
nota = 7
if nota > 5: # If condição: 5 não é maior que 5, ela é igual. Mudamos para a nota 7
  print('Aporvado')
  print(f'Sua Nota é {nota} :) ')

numero = int(input('Digite um numero maior que 10\n '))
if numero > 10:
  print('Número Aceito')

nota1 = float(input('Digite a nota do Primeiro Bimestre: '))
nota2 = float(input('Digite a nota do Segundo Bimestre: '))
if (nota1+nota2) /2 > 5: # Tem de por o () para que seja feita o calculo deste primeiro
  print('Aprovado')
else: # Se não -- nunca terá a mesma condição do if
  print('Reprovado')

#  Usando o If Condição mais que 1 vez no código, tudo fora do If é resto.
menu = input('1 Pagamento\n 2 - Sair\n')
if menu == '1':
  pagamento = input('1 Cartão\n 2 Boleto\n')
  if pagamento == '1':
    print('Pagamento por Cartão')
  else:
    print('Pagamento por Boleto')
else:
  print('Sair!')

'''
Desafio
1. verificação de Números Positivos ou Negativos
Escreva um programa que solicite ao usuário um número qualquer. O programa deve verificar se o número é positivo ou negativo. Considere o zero como número positivo
'''
numero = float(input('Digite um Número: '))
if numero >= 0:
  print('Número Positivo')
else:
  print('Número Negativo')
  
