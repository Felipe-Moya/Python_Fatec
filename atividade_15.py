num1 = float(input("Digite os votos totais do candidato 1: "))
num2 = float(input("Digite os votos totais do candidato 2: "))
num3 = float(input("Digite os votos totais do candidato 3: "))
branco = float(input("Digite os votos totais em branco: "))

total = num1 + num2 + num3 + branco
percentual = (branco/total)*100
vot_val = num1 + num2  + num3
perc_1 = (num1/vot_val)*100
perc_2 = (num2/vot_val)*100
perc_3 = (num3/vot_val)*100

print(f"O total geral de votos foi: {total}\n"
      f"Total de votos nulos: {branco}\n"
      f"Percentual de votos em branco: {percentual:.2f} % \n")

print(f"Total de votos do candidato 1: {num1}\n"
      f"Percentual de votos do candidato 1: {perc_1:.2f} % \n")
print(f"Total de votos do candidato 2: {num2}\n"
      f"Percentual de votos do candidato 2: {perc_2:.2f} % \n")
print(f"Total de votos do candidato 3: {num3}\n"
      f"Percentual de votos do candidato 3: {perc_3:.2f} % \n")
