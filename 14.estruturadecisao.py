# MEDIA DE APROVEITAMENTO
# ENTRE 9.0 E 10.0 a
nome = input ("Informe seu nome ")
n1 = float(input("Informe sua primeira nota "))
n2 = float(input("Informe sua segunda nota "))
media = (n1 + n2) / 2
if (media >= 9 and media <=10):
    print (nome, "Voce foi aprovado com")
    print ("Conceito A, pois suas notas foram", n1, "e",n2, "e sua media foi:",media)
elif (media >=7.5 and media < 9):
    print (nome, "Voce foi aprovado ")
    print ("Conceito B, pois suas notas foram", n1, "e",n2, "e sua media foi:",media)
elif (media >= 6 and media < 7.5):
    print (nome, "Voce foi aprovado ")
    print ("Conceito C, pois suas notas foram", n1, "e",n2, "e sua media foi:",media)
elif (media >= 4 and media < 6):
    print (nome, "Voce foi reprovado ")
    print ("Conceito D, pois suas notas foram", n1, "e",n2, "e sua media foi:",media)
elif (media < 4 and media > 0):
    print (nome, "Voce foi reprovado ")
    print ("Conceito E, pois suas notas foram", n1, "e",n2, "e sua media foi:",media)
else:
    print ("Valor Invalido ")
