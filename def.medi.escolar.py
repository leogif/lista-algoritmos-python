nome = input ("Informe seu nome ")
b1 = float(input("Qual foi sua nota no 1º? "))
b2 = float(input("Qual foi sua nota no 2º? "))
b3 = float(input("Qual foi sua nota no 3º? "))
b4 = float(input("Qual foi sua nota no 4º? "))

def media_escolar():
    media = (b1 + b2 + b3 + b4) / 4
    if (media > 6.9):
        print(nome,"Parabens você esta aprovado. Média:",media)
    elif (media >= 5 and media <=6.9):
        print(nome,"você esta em recuperação. Média: ",media)
    else:
        print(nome,"você foi reprovado. Média:",media)

if __name__ == "__main__":
    media_escolar()
           
