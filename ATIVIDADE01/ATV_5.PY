import os
os.system('cls')

vetor_notas = []
QUANTIDADE_NOTAS = 5
acima_media = 0

for i in range(QUANTIDADE_NOTAS):
    notas = float(input(f'Digite a sua {i+1}º nota: '))
    vetor_notas.append(notas)

media = sum(vetor_notas) / QUANTIDADE_NOTAS

if media >= 7:
    acima_media += 1

print(f'A sua nota é: {notas}')
print(f'A sua média é: {media}')
print(f'As notas acima da média são: {acima_media}')