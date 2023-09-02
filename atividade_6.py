distancia = float(input("Digte a distância percorrida em km: "))
q_combustivel = float(input("Coloque a quantidade de combustivel em litros: "))
ql = distancia / q_combustivel

print(
f"Distância: {distancia} km \n"
f"Combustível: {q_combustivel} litros \n"
f"O desempenho do veículo é: {ql} km/litros"
)
