import os
os.system('cls')

print('= iserindo numero na vetor A: =')
vetor_A = []
vetor_B = []
vetor_C = []

for i in range(5):
    numero =input(f'digite o numero do {i+1}º numero: ')
    vetor_A.append(numero)

print('\n= exibidno numeros do vetor: =')
for indice , numero in enumerate (vetor_A, start=1):
    print(f'{indice}º: {numero}')
os.system('cls')
print()

print('= iserindo numero na vetor B: =')
for i in range(5):
    numero =input(f'digite o numero do {i+1}º numero: ')
    vetor_B.append(numero)

print('\n= exibindo números do vetor: =')
for indice , numero in enumerate (vetor_B, start=1):
    print(f'{indice}º: {numero}')

print('=  vetor C: =')

for i in range(5):
    soma = vetor_A[i] + vetor_B[i]
    vetor_C.append(soma)

print("\n" + "=" * 35)
print(f"Vetor A: {vetor_A}")
print(f"Vetor B: {vetor_B}")
print(f"Vetor C (A + B): {vetor_C}")
print("=" * 35)




# # Inicialização dos vetores
# vetor_A = []
# vetor_B = []
# vetor_C = []

# print("=== LEITURA DO VETOR A ===")
# for i in range(5):
#     num = int(input(f"Digite o {i + 1}º número para o Vetor A: "))
#     vetor_A.append(num)

# print("\n=== LEITURA DO VETOR B ===")
# for i in range(5):
#     num = int(input(f"Digite o {i + 1}º número para o Vetor B: "))
#     vetor_B.append(num)

# # Geração do Vetor C somando as posições correspondentes
# for i in range(5):
#     soma = vetor_A[i] + vetor_B[i]
#     vetor_C.append(soma)

# # Exibição dos três vetores
# print("\n" + "=" * 35)
# print(f"Vetor A: {vetor_A}")
# print(f"Vetor B: {vetor_B}")
# print(f"Vetor C (A + B): {vetor_C}")
# print("=" * 35)
