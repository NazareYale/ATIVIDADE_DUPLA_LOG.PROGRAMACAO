import os
os.system('cls')
idades = []

print("=== LEITURA E VALIDAÇÃO DE IDADES ===\n")
for i in range(5):
    while True:
        idade = int(input(f"Digite a idade da {i + 1}ª pessoa (0 a 120): "))
        if 0 <= idade <= 120:
            idades.append(idade)
            break
        print(" -> Idade inválida! Digite um valor entre 0 e 120.\n")


maior_idade = idades[0]
menor_idade = idades[0]
maiores_de_idade = 0


for idade in idades:
    if idade > maior_idade:
        maior_idade = idade
    if idade < menor_idade:
        menor_idade = idade
    if idade >= 18:
        maiores_de_idade += 1


print("\n" + "=" * 35)
print(f"Vetor de idades cadastradas: {idades}")
print(f"Maior idade: {maior_idade} anos")
print(f"Menor idade: {menor_idade} anos")
print(f"Quantidade de maiores de idade (>= 18): {maiores_de_idade}")
print("=" * 35)