# PORCENTAGENS
vinte = 1.20
quinze = 1.15
dez = 1.10
cinco = 1.05


nome = input("Informe seu nome ")
print(nome, "Infome o valor do seu salário atual")
# ATUAL SALARIO
Asalario = int(input(" "))

if Asalario > 0 and Asalario <= 280:
    # NOVO SALARIO
    Nsalario = (Asalario * vinte)
    # VALOR DO AUMENTO
    Vaumento = Nsalario - Asalario
    print(nome,"Este era o valor do seu salario antes do reajuste: ",Asalario)
    print("este e o valor aplicado por percentual para aumento de salario",vinte)
    print(nome, "voce recebeu um aumento de ", Vaumento)
    print("Este e o valor do seu salario atual: ", Nsalario)

elif (Asalario > 280 and Asalario <=700):
    Nsalario = Asalario * quinze
    Vaumento = Nsalario - Asalario
    print(nome,"Este era o valor do seu salario antes do reajuste: ",Asalario)
    print("este e o valor aplicado por percentual para aumento de salario",quinze)
    print("voce recebeu um aumento de ", Vaumento)
    print("Este e o valor do seu salario atual: ", Nsalario)

elif (Asalario > 700 and Asalario <= 1500):
    Nsalario = Asalario * dez
    Vaumento = Nsalario - Asalario
    print(nome,"Este era o valor do seu salario antes do reajuste: ",Asalario)
    print("este e o valor aplicado por percentual para aumento de salario",dez)
    print("voce recebeu um aumento de ", Vaumento)
    print("Este e o valor do seu salario atual: ", Nsalario)

elif (Asalario >1500):
    Nsalario = Asalario * cinco
    Vaumento = Nsalario - Asalario
    print(nome,"Este era o valor do seu salario antes do reajuste: ",Asalario)
    print("este e o valor aplicado por percentual para aumento de salario",quinze)
    print("voce recebeu um aumento de ", Vaumento)
    print("Este e o valor do seu salario atual: ", Nsalario)

else:
    print("Valor Invalido")
