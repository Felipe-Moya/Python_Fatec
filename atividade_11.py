print(" -- Iremos calcular o IPTU da cidade --  ")
vc = float(input("Digite o m² construído: "))
ac = float(input("Digite a área construída em m² : "))
mt = float(input("Digite o valor do terreno em m² : "))
at = float(input("Digite a área do terreno em m²: "))

predial = vc * ac
territorial = mt * at
iptu = predial + territorial

print("""
Valor do predial é :  {} m²
Valor do territorial é : {} m²
O valor do IPTU é : {} m²
""".format(predial, territorial, iptu))
