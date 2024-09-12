lista = ['oi', 'tudo', 'bem', 'com']
verificação = all(len(numero) > 3 for numero in lista)
if verificação:
    print('Todas as strings possuem mais do que 3 caracteres')
else:
    print('Não é possível confirmar se todas as strings possuem mais do que 3 caracteres')