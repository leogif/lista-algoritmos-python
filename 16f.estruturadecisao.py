print("------------------------------------------------------------------------------")
print("###################DHPP####################")
print("#########DELEGADO AWAY GIL BROTHER#####")
print("####VOU BOTAR OS CABRITO PARA MAMA#####")
print("------------------------------------------------------------------------------")
n = input("Qual e o seu nome ? ")
print(n,"responda as perguntas com #1#Sim e #0#Nao")

print("Telefonou para a vitima ? ")
p1 = int(input(""))
if(p1 != 1 or p1 != 0):
    print("Sao aceitos somente 0 e 1")

print(n,"Voce esteve no local do crime ? ")
p2 = int(input(""))
if(p2 != 1 or p2 != 0):
    print("Sao aceitos somente 0 e 1")

print(n,"Voce mora perto da vitima ? ")
p3 = int(input(""))
if(p3 != 1 or p3 != 0):
    print("Sao aceitos somente 0 e 1")

print(n,"Voce devia para a vitima ? ")
p4 = int(input(""))
if(p4 != 1 or p4 != 0):
    print("Sao aceitos somente 0 e 1")

print(n,"voce ja trabalhou com a vitima ? ")
p5 = int(input(""))
if(p5 != 1 or p5 != 0):
    print("Sao aceitos somente 0 e 1")

resultado = (p1 + p2 + p3 + p4 + p5)

if (resultado == 2):
    print(n,"voce e Suspeito")
elif(resultado == 3 or resultado == 4):
         print(n,"voce e Cumplice")
elif(resultado == 5):
         print(n,"Voce e o Assassino")
else:
         print(n,"voce e inocente")
