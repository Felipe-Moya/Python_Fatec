nota1 = float(input("Digite o valor da nota 1: "))
nota2= float(input("Digite o valor da nota 2: "))
nota3 = float(input("Digite o valor da nota 3: "))
nota4 = float(input("Digite o valor da nota 4: "))
if (nota1 or nota2 or nota3 or nota4) > 10:
    print("Notas inválidas!")
else:
    media_p = (nota1*1 + nota2 * 2 + nota3*3 + nota4*4)/ 10
    print(f"A sua nota final é de: {media_p} ")
