vitorias = float(input("Digite a quantidade de vitórias: "))
empates = float(input("Digite a quantidade de empates: "))
compt = float(input("Digite o total de competições: "))
v_p = vitorias * 3
total = v_p + empates
aproveitamento = (vitorias/compt) * 100

print(f"O aproveitamento é de {aproveitamento:.2f} % \n"
      f"O total de pontos da equipe é: {total:.0f}")
