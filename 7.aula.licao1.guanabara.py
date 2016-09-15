print ("#################################")
print ("---DEPARTAMENTO DE TRANSITO---")
print ("#################################")
anoAtual = int(input("Ano Atual (AAAA): "))
anoNasc = int(input("Ano de Nascimento (AAAA): "))
idade = anoAtual - anoNasc
if (idade >= 18):
    print ("#########STATUS#########")
    print ("IDADE:" ,idade, "anos")
    print ("APTO A FAZER O EXAME")
else:
    print ("#########STATUS#########")
    print ("IDADE:" ,idade, "anos")
    print ("INAPTO A FAZER O EXAME")
