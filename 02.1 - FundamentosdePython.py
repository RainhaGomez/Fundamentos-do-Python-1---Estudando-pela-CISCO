print('Olá, Mundo')

# Argumentos - Nessa situação temos dois argumentos ( Ola e Mundo separados por virgulas ) o Print pode ter N's
# argumentos como não ter argumentos. Print sem argumentos APENAS cria uma linha em branco.
print("Ola", "Mundo")

# \ - é um caracter de escape
# \n - Cria uma nova linha ou quebra de linha, ele deve estar dentro das aspas
print("A aranha pequenininha\nsubiu a tromba d'água.")
print()
print("abaixo veio a chuva\ne lavou a aranha.")

# \t - Cria uma tabulação ou seja adiciona 4 espaços
print("abaixo veio a chuva\te lavou a aranha.")

#/b - backspace ou apaga o ultimo caracter.
print("abaixo veio a chuva\be lavou a aranha.")

#Se você quiser colocar apenas uma barra invertida dentro de uma string, não se esqueça
# de sua natureza de escape - você precisa dobrá-la. Por exemplo, uma invocação como esta causará um erro:
print("\\")

#Argumentos de palavra chave
# end='(caracter ou texto de sua escolha)' - Junta a linha de baixo com a superior
print("Meu nome é", "Python.", end=" ")
print("Monty Python.")

# sep='(caracter ou texto de sua escolha) ' - troca a virgula por um novo separador sem ser o espaço.
print("A aranha", "pequenininha", "subiu", "a", "tromba", "d'água", sep="+")

# O argumento posisacional de palabra chave sempre deve ir ao final da função
# Erro de Sintaxe!
print("A aranha", sep='+' "pequenininha", "subiu", "a", "tromba", "d'água")