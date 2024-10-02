#Fibonacci. crie uma função que recebe um número n e retorna o n-ésimo número da sequência de Fibonacci.


def fibonacci(n):
    a = 0
    b = 1
    valor = 0

    if n == 1:
        return valor
    if n == 2:
        valor = b
        return valor
    for i in range(2, n):
        valor = a + b
        a = b
        b = valor
    return valor
print(fibonacci(10))


#Exercício 2
"""a = int(input("Digite a: "))
b = int(input("Digite b: "))
c = int(input("Digite c: "))"""
def maior_de_tres(a, b, c):
    if a > b and a > c:
        return "a"
    if b > a and b > c:
        return "b"
    else:
        return "c"

#exercício Soma dos Dígitos

def soma_dos_digitos (a):
    soma = 0
    for i in str(a):
        soma += int(i)
    return soma
print(soma_dos_digitos(12))


#Exercício fatorial
def fatorial (n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

n=7
resultado = fatorial(n)
print(resultado)


#exercício palíndromo

def palindromo (n):
    return n == n[::-1]

n = input("Digite uma palavra: ")
if palindromo(n):
    print(f"{n} é um palíndromo.")
else:
    print(f"{n} não é um palíndromo")