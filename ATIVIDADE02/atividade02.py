import os
os.system('cls')


vetor_temperaturas = []
QUANTIDADE_DIAS = 7

print('Solicitando temperaturas:')
for dia in range(1, 8):
    temperatura = float(input(f'Digite a temperatura do dia {dia}º: '))
    vetor_temperaturas.append(temperatura)


media = sum(vetor_temperaturas) / QUANTIDADE_DIAS
maior = max(vetor_temperaturas)
menor = min(vetor_temperaturas)


print('\nTemperaturas registradas:')
for dia, temperatura in enumerate(vetor_temperaturas, start=1):
    print(f'Dia {dia}: {temperatura:.1f} °C')


print('\nDados registrados:')
print(f'Média da semana: {media:.1f} °C')
print(f'Maior temperatura: {maior:.1f} °C')
print(f'Menor temperatura: {menor:.1f} °C')
