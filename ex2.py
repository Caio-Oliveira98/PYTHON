a = [
    [1,2],
    [1,2]
]
escalar = 2

b= [
    [0,0],
    [0,0]

 ]
for linha in range(2):
    for coluna in range(2):
        b[linha][coluna] = a[linha][coluna] * escalar
for linha in b:
    print(linha)
    