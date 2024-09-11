matriz1= [
         [1,2,3],  
         [4,5,6], 
         [7,8,9]
]

matriz2= [
         [9,8,7],
         [6,5,4],
         [3,2,1]          
]

matriz3 = [
          [0,0,0],
          [0,0,0],
          [0,0,0]
]

for linha in range(3):
    for coluna in range(3):
        matriz3 [linha][coluna] = matriz1[linha][coluna] + matriz2[linha][coluna]
for linha in matriz3:
    print(linha)