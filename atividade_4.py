real = float(input("Digite quantos reais você quer converter: "))
dolar = float(input("Digite o valor atual do Dólar: "))

conversao = real / dolar

print(f"Pela cotação atual do Dólar o valor R${real} é ${conversao:.2f}: ")
