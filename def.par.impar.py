numero = int(input("Digite um Número: "))

def par_ou_impar():
    """
    Função verifica se o número digitado é par ou impar
    utilizando atribuição Condicional
    Neste exemplo são utilizadas 2 linhas de código.
    """
    s = "par" if numero % 2 == 0 else "impar"
    print("O numero digitado e", s)

def par_ou_impar_1():
    """
    Funçao verifica se o numero digitado e par ou impar
    utilizando o laco de decisao if, else e realizando o calculo
    da sobra da divisao (%) no proprio laco if.
    Neste exemplo sao utilizadas 4 linhas de codigo.
    """
    if numero % 2==0:
        print("O numero digitado e par ")
    else:
        print("O numero digitado e impar ")

def par_ou_impar_2():
    """
    Funçao verifica se o numero digitado e par ou impar
    utilizando o laco de decisao if, else e realizando o calculo
    da sobra da divisao (%) FORA do laço if.
    Neste exemplo sao utilizadas 5 linhas de codigo.    
    """
    teste = numero % 2
    if teste == 0:
        print("O numero digitado e par ")
    else:
        print("O numero digitado e impar ")

if __name__ == "__main__":
    par_ou_impar()
    par_ou_impar_1()
    par_ou_impar_2()
