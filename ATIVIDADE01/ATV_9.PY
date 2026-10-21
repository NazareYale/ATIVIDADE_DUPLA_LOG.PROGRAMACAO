import os
os.system('cls')

#Leia 6 números inteiros em um vetor. Substitua cada par por 0 e cada ímpar por 1. Mostre o vetor antes e depois.
vetor_amostra = [2, 3, 4, 5, 6, 7]

print(f'Vetor antes: {vetor_amostra}')

for i in range(len(vetor_amostra)):
    if vetor_amostra[i] % 2 == 0:
        vetor_amostra[i] = 0
    else:
        vetor_amostra[i] = 1

print(f'Vetor depois: {vetor_amostra}')