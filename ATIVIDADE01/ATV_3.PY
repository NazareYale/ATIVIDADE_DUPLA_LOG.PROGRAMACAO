import os
os.system('cls')

vetor_numeros = []
QUANTIDADE_LOOPS = 10
maiores = 0

for i in range(QUANTIDADE_LOOPS):
    numeros = float(input(f'Digite o {i+1}º número: '))
    vetor_numeros.append(numeros)


soma = sum(vetor_numeros)

if numeros >= 11:
    maiores += 1


print(f'Os números do vetor são: {vetor_numeros}')
print(f'A soma dos números é: {soma}')
print(f'Os números maiores que 10 são: {maiores}')
#Arrumar a soma dos maiores que 10
