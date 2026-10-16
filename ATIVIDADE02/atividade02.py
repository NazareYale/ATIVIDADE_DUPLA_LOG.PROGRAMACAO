import os
os.system('cls')

import os
os.system('cls')

vetor_temperatura = []
vetor_dias = []

while True:
    print('''
codigo              dias                temperatura
1                   segunda               0
2                   terça                 20
3                   quarta                18
4                   quinta                15
5                    sexta                 5
6                    sabado               30
7                     domingo             40
''')
    opcao = int(input('digite a opçao desejada: '))

    match opcao:
        case '1':
            dias = 'segunda'
            temperatura = 0
        case '2':
            dias = 'terça'
            temperatura = 20
        case '3':
            dias ='quarta'
            temperatura = 18
        case '4':
            dias = 'quinta'
            temperatura = 15
        case '5':
            dias = 'sexta'
            temperatura = 5
        case '6':
            dias = 'sabado'
            temperatura =30
        case '7':
            dias = 'domingo'
            temperatura =40
        case _:
            print('opcao invalida')

    if opcao >= 1 and opcao <= 5:
        vetor_dias.append(dias)
        vetor_temperatura.append(temperatura)