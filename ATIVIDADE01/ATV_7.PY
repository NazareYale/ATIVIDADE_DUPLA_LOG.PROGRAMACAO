import os
os.system('cls')

#Leia 10 números inteiros em um vetor. Copie para um segundo vetor apenas os positivos, mostre-o e informe quantos elementos foram copiados.
vetor_numeros= []
vetor_secundario = []
QUANTIDADE_LOOPS = 10

for i in range(QUANTIDADE_LOOPS):
    numeros = int(input(f'Digite o {i+1}º número: '))

    if numeros < 0:
        vetor_numeros.append(numeros)
    else:
        vetor_secundario.append(numeros)
total_modificados = len(vetor_secundario)

print(f'Os números totais dos vetores são: 1º{vetor_numeros} / 2º{vetor_secundario}')
print(f'Os números negativos são: {vetor_numeros}')
print(f'Os números positivos são: {vetor_secundario}')
print(f'Números copiados do vetor principal para os positivos: {total_modificados} ')