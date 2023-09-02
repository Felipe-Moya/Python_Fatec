horario = input("Digite o horário que você estará sendo atendido: (0h até 7h59) - 1 , (8h até 15h59) - 2 , (16h - 23h59) - 3: "
)
qtd_minutos = float(input("Digite os minutos da ligação: "))

if horario == "1":
   valor = qtd_minutos * 0.155645
   print(f"O valor total a ser pago é de:R$ {valor:.2f}")
elif horario == "2":
    valor = qtd_minutos * 0.245645
    print(f"O valor total a ser pago é de:R$ {valor:.2f}")
elif horario == "3":
    valor = qtd_minutos * 0.354656
    print(f"O valor total a ser pago é de:R$ {valor:.2f}")
else:
    print("Valor inválido")
