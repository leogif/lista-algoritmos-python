print("""Digite o dia da semana que voce nasceu \n#1-DOM;2-SEG;3-TER;4-QUA;5-QUI;6-SEX;7-SAB#""")
dia = int(input("informe um dia da semana"))
if (dia == 1):
    print ("domingo")
elif (dia == 2):
    print ("segunda")
elif (dia == 3):
    print ("terca")
elif (dia == 4):
    print ("quarta")
elif (dia == 5):
    print ("quinta")
elif (dia == 6):
    print ("sexta")
elif (dia == 7):
    print ("sabado")
else:
    print("###VALOR INVALIDO###")
