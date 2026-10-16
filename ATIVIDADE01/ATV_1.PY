import os
os.system('cls')

vetor_numeros = []
QUANTIDADE_LOOPS = 5

for i in range(QUANTIDADE_LOOPS):
    numeros = int(input(f'Digite o {i+1}º número: '))
    vetor_numeros.append(numeros)

for posicao, numeros in enumerate(vetor_numeros, start=1):
    print(f'O seu {posicao}º número é: {numeros}')


print(f'Valor do vetor na quinta posição: {vetor_numeros[4]}')
print(f'Valor do vetor na quarta posição: {vetor_numeros[3]}')
print(f'Valor do vetor na terceira posição: {vetor_numeros[2]}')
print(f'Valor do vetor na segunda posição: {vetor_numeros[1]}')
print(f'Valor do vetor na primeira posição: {vetor_numeros[0]}')