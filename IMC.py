peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura * altura)
Classificacao = str

print(f"Seu IMC é {imc:.1f}")

if imc < 18.5:
    print(f"Classificacao = MAGREZA")
elif imc <= 24.9:
    print(f"Classificacao = NORMAL")
elif imc <= 29.9:
    print(f"Classificacao = OBESIDADE")
else:
    print(f"Classificacao = OBESIDADE GRAVE")

