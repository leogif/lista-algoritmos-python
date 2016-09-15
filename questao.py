#import MySQLdb

#con = MySQLdb.connect ('servidor', 'root', 'progmetal')
#con = con.select_db('flashdead')

# n para nome
n = input ("Informe seu nome ")
# m para matéria
m = input ("Informe a matéria ")

print ("Seu nome é",n, "e sua idade é:",m)
# b1 para 1º Bimestre e assim sucessivamente
b1 = float(input("Informe sua nota no 1º Bimestre "))
b2 = float(input("Informe sua nota no 2º Bimestre "))
b3 = float(input("Informe sua nota no 3º Bimestre "))
b4 = float(input("Informe sua nota no 4º Bimestre "))

# media recebe a soma de quoeficientes dividido pela quantidade de quoeficientes
media = (b1 + b2 + b3 + b4 ) / 4

# se media maior que 5.9 no caso 6 esta aprovado
if media > 5.9:
    print (n,"parabéns você foi aprovado na materia",m, "sua média foi:",media)
# entao se media maior ou igual a 4 e media menor ou igual a 5.9 esta em recuperação
elif media >= 4 and media <=5.9:
    print (n,"você esta de recuperação na matéria",m)
# entao se media menor que 4, reprovação
elif media < 4:
    print (n,"você esta reprovado na matéria",m)


