import os
os.system('cls')

print('= isera o seu salario: =')
vetor_salario = []
vetor_nome = []
maior_salario = 0
menor_salario= 9999
for i in range(5):
    salario =input(f'digite o salario do {i+1}º salario: ')
    vetor_salario.append(salario)

maior_salario = max(vetor_salario)
menor_salario = min(vetor_salario)

print('mostrar salario')
for posicao , salario in enumerate(vetor_salario, start=1):
    print(f'{posicao}º: {salario}')

print(f'maior_numero: {maior_salario}')
print(f'menor_numero: {menor_salario}')