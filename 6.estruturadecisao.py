"""
maiorn1 = 0

mn1 = int(input("Informe o 1º número "))
mn2 = int(input("Informe o 2º número "))
mn3 = int(input("Informe o 3º número "))

if (mn1 >= mn2 or mn1 >= mn3):
     print (mn1, "é o maior número entre", mn2, "e", mn3)
else :
    elif (mn2 >= mn1 or mn2 >= mn3):
    print (mn2, "é o maior número entre", mn1, "e", mn3)
    elif (mn3 >= mn1 or mn3 >= mn2):
    print (mn3, "é o maior número entre", mn1, "e", mn2)



"""
n1 = int(input("Informe o 1º número "))
n2 = int(input("Informe o 2º numero "))
n3 = int(input("Informe o 3º numero "))

if(n1 > n2 or n1 > n3):
    print(n1, "e maior que ",n2, "e",n3)
elif(n2 > n1 or n2 > n3):
    print (n2,"e maior que",n3, "e",n1)
else:
    print(n1, "nao e maior que ",n2, "e",n3 )

#if (n > maior):
#       maior = n
#    s = s + n
#    cont = cont + 1
