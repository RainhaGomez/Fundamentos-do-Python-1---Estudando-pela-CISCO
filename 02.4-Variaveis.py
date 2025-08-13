# Declarando variaveis
nome = 'Nebulosa'
idade = 30
altura = 1.67

#O nome da variável não pode ter espaço, incluindo: Espaço e !@#$#$%¨&*()+{}[] com a exceção do _
nome completo = 'nebulosa do Guaruja'

#CamelCase (Variavel com nome composto)
#Consiste em deixar a primeira letra de cada palavra maiuscula
NomeCompleto = 'nebulosa do guaruja'

#sneak_case (Variavel com nome composto)
#Consiste em separar as palavras com _
nome_completo = 'nebulosa do guaruja'

#Como usar(chamar) as variaveis
print('nome: ', nome)
print('idade: ', idade)
print('altura: ', altura)

print('nome: ', nome, 'Idade:', idade,'Altura: ',altura)

peso = 85.55
imc = peso/ altura**2
print(imc)

# Transformando graus celsius em Fahrenheit
# f = c° * 1.8 +32
f = 15 * 1.8 + 32
print(f, 'F°')

# Transformando Fahrenheit em Kelvin
k = (59 - 32) + 5/9 + 273.15
print(k, 'K°')

'''
DESAFIO
1. Área do Retângulo:
- Calcule a área utilizando a fórmula: area= base*altura
- base: 7.86
- altura: 2.14
Exiba o resultado na tela.
'''
base = 7.86
Altura = 2.14
area = base * Altura
print(area)

# Variaveis do mesmo nome se sobrepõem
teste = 123
teste = 'teste'
teste = True
print(teste)

'''
Conversor de Moedas:
- Converta para dólares utilizando uma cotação fixa(defina a cotação no seu código).
- Eviba o valor em dólares
'''
dolar = 5.40
real = 5.73
valor_final = dolar * real
print(valor_final)
