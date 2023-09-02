preco_f = float(input("Digite o preço dado pelo fabricante do carro: "))
imposto = preco_f * 0.35
margem_r = preco_f * 0.1

preco_v = preco_f + imposto + margem_r

print("""
Valor dos impostos do carro: R$ {}
Valor da margem do revendedor: R$ {}
Preço da venda do carro: R$ {} 
""".format(imposto, margem_r, preco_v))
