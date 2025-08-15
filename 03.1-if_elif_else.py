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
  
'''
Desafio
2. Valor da Parcela
Faça um algoritimo que receba um valor de uma compra e receba o número de prestações, apresente o valor das prestações sem juros.
'''
valor_compra = float(input('Digite o valor da compra:\n'))
qtd_parcela = int(input('Digite o número de parcelas:\n'))
print(f'O valor da compra R${valor_compra} parcelada em {qtd_parcela:.2f} vezes')

'''
Desafio
3. Maior entre dois números
Crie um programa que peça ao usuário para digitar dois números. O programa deve comparar os dois números e exibir uma mensagem indicando qual deles é o maior
'''
num1 = float(input('Digite o primeiro número:\n'))
num2 = float(input('Digite o segundo número:\n'))
if num1 > num2:
  print(f'O maior número é {num1}')
else:
  print(f' O maior número é {num2}')

#Outro jeito de fazer sem i if
#print(f'O maior número é {max(num1,num2)}')

# EXEMPLO DE USO COM ELIF

# Notas Escolares
nota = 8
if nota >=7:
  print('Aprovado')
elif nota <5:# O Elif sempre deve estar no meio do if e o else
  print('Reprovado')
else:
  print('Recuperação')


# Pagamento Simples
#If para começar uma ação, Elif para para outra oção da ação e else para terminar a ação referente ao If. Entre o if e o Else pode ter várias Elif
menu = input('1 - Pagamento\n 2- sair:\n')
if menu == '1':
  pagamento = input('1 - Cartão Débito\n 2 - Cartão de Crédito\n 3 - Boleto\n 4 - Pix\n')
  if pagamento =='1':
    print('Cartão de Débito')
  elif pagamento =='2':
    print('Cartão de Crédito 2x')
  elif pagamento=='3':
    print('Boleto')
  elif pagamento =='4':
    print('Pix')
  else:
    print('Opção Inválida!')
elif menu =='2':
  print('Saiu')
else:
  print('opção Inválida!')

'''
Desafio
4. Maior entre dois números
Crie um programa que peça ao usuário para digitar dois números. O programa deve comparar os dois números e exibir uma mensagem indicando qual deles é o maior ou se são iguais
'''
num1 = float(input('Digite o primeiro número:\n'))
num2 = float(input('Digite o segundo número:\n'))
if num1 > num2:
  print(f'O maior número é {num1}')
elif num2 > num1:
  print(f' O maior número é {num2}')
else:
  print(f'Esses números são iguais ')

#Outro jeito de fazer sem i if
#print(f'O maior número é {max(num1,num2)}')

'''
Desafio

5. Calculadora
Exiba um menu de oprações para o usuário:
Soma (+)
Subtração (-)
Multiplicação (*)
Divisão (/)
Sair (0)
'''
'''
numeroa=float(input('Digite o primeiro número '))
numerob = float(input('Digite o segundo número '))
op1=input('Digite o operador desejável, (+), (-), (*) e (/)\n')
if op1 == '+':
  print(f'O resultado é:\n {numeroa+numerob:.2f}')
elif op1== '-':
  print(f'O resultado é:\n {numeroa-numerob:.2f}')
elif op1== '*':
  print(f'O resultado é:\n {numeroa*numerob:.2f}')
elif op1== '/':
  print(f'O resultado é:\n {numeroa/numerob:.2f}')
else:
  print(f'SAIR')
  Aqui dará um erro na divisão por zero, pois no python não é possível.
  '''
numeroa=float(input('Digite o primeiro número '))
numerob = float(input('Digite o segundo número '))
op1=input('Digite o operador desejável, (+), (-), (*) e (/)\n')
if op1 == '+' or op1 == 'soma':
  print(f'O resultado é:\n {numeroa+numerob:.2f}')
elif op1== '-'or op1 == 'subtração':
  print(f'O resultado é:\n {numeroa-numerob:.2f}')
elif op1== '*'or op1 == 'multiplicação':
  print(f'O resultado é:\n {numeroa*numerob:.2f}')
elif op1== '/'or op1 == 'divisão':
  if numeroa == 0: 
    print(f'O Resultado não é possível:\n ')
  elif numerob == 0:
    print(f'O resultado é:\n {numeroa/numerob:.2f}')
else:
  print(f'SAIR')
