python
# Questão 1: Fibonacci
# Este código verifica se um número pertence à sequência de Fibonacci.

def is_fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return f"{n} pertence à sequência de Fibonacci."
        a, b = b, a + b
    return f"{n} não pertence à sequência de Fibonacci."

# Exemplo de número
numero_exemplo = 13
print(is_fibonacci(numero_exemplo))

# Permitir que o usuário digite um número
numero_usuario = int(input("Digite um número: "))
print(is_fibonacci(numero_usuario))

# ---------------------------

# Questão 2: Contagem de Letras 'a'
# Este código verifica a quantidade de vezes que a letra 'a' (maiúscula ou minúscula) aparece em uma string.

def contar_a(string):
    contagem = string.lower().count('a')  # Conta 'a' em minúsculo
    return f"A letra 'a' aparece {contagem} vezes na string."

# Definindo uma string de exemplo
string_exemplo = "A aviação é uma área fascinante."
print(contar_a(string_exemplo))

# Permitir que o usuário digite uma string
string_usuario = input("Digite uma string: ")
print(contar_a(string_usuario))

# ---------------------------

# Questão 3: Soma com base no trecho de código
def calcular_soma(indice):
    soma = 0
    k = 1
    while k < indice:
        soma += k
        k += 1
    return soma

# Definindo o índice
indice = 12
resultado = calcular_soma(indice)
print(f"A soma dos números de 1 a {indice-1} é: {resultado}")

# ---------------------------

# Questão 4: Descobrir a lógica e completar os próximos elementos
# a) 1, 3, 5, 7, ___
proximo_a = 9

# b) 2, 4, 8, 16, 32, 64, ____
proximo_b = 128

# c) 0, 1, 4, 9, 16, 25, 36, ____
proximo_c = 49

# d) 4, 16, 36, 64, ____
proximo_d = 100

# e) 1, 1, 2, 3, 5, 8, ____
proximo_e = 13

# f) 2, 10, 12, 16, 17, 18, 19, ____
proximo_f = 20

# Imprimindo os resultados
print(f"a) próximo elemento: {proximo_a}")
print(f"b) próximo elemento: {proximo_b}")
print(f"c) próximo elemento: {proximo_c}")
print(f"d) próximo elemento: {proximo_d}")
print(f"e) próximo elemento: {proximo_e}")
print(f"f) próximo elemento: {proximo_f}")

# Questão 5: Interruptores e Lâmpadas
# Este problema é uma questão lógica e não um código.
# 1. Ligue o primeiro interruptor e deixe-o ligado por alguns minutos.
# 2. Desligue o primeiro interruptor e ligue o segundo.
# 3. Vá até a sala das lâmpadas.
# - A lâmpada que está acesa corresponde ao segundo interruptor.
# - A lâmpada que está apagada, mas quente, corresponde ao primeiro interruptor.
# - A lâmpada que está apagada e fria corresponde ao terceiro interruptor.
