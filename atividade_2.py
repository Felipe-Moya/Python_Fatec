nota1 = float(input("Digite a primeira nota(0 à 10): "))
nota2 = float(input("Digite a segunda nota(0 à 5): "))
nota3 = float(input("Digite a quarta nota(0 à 5): "))

if nota1 > 10 or nota1 < 0:
    print(" Valores inválidos ")

elif nota2 > 5 or nota2 < 0:
    print(" Valores inválidos ")

elif nota3 > 5 or nota3 < 0:
    print(" Valores inválidos ")

else:
    media = (nota1 + (nota2 + nota3) * 2)/3
    print(f"A média final é {media:.1f}")
