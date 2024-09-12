lista_nomes = ['Caio', 'João', 'Leonardo', 'Cleber', 'Rodrigo']
nome_a_verificar = 'Caio'
esta_presente = nome_a_verificar in lista_nomes
if esta_presente:
    print(f"O nome '{nome_a_verificar}' está presente na lista.")
else:
     print(f"O nome '{nome_a_verificar}' não está presente na lista.")
