# -*- coding: utf-8 -*-

from datetime import *

def datetime_data_e_hora():
    """
    Para manipular data e hora vamos utilizar o **datetime.now()**
    com ele poderemos manipular datas e tambem tudo referente
    a horas, minutos e segundos.
    """
    # Variavel **a** recebe o datetime.
    a = datetime.now()

    # Data e hora completos
    print("Data, horas e microssegundos: ", a.now())

    # Mostra o dia
    print ("Dia: ", a.day)
    print ("Dia atual =%d somando mais 2 dias = %d" % (a.day + 2))

    # Mostra o mes
    print ("Mes: ", a.month)

    # Mostra o ano
    print ("Ano: ", a.year)

    # Mostra a hora
    print ("Hora: ", a.hour)

    # Mostra os minutos
    print ("Minutos: ", a.minute)

    # Mostra os segundos
    print ("Segundos: ", a.second)

    # Mostra os micro segundos
    print ("Microssegundos: ", a.microsecond)

    # Concatenando
    print ("Dia, Mes e Ano: ", a.day, a.month, a.year)

    # Formatando
    print ("datetime formatado: ", a.strftime ("%A %d %B %Y"))
    print ("datetime formatado: ", a.strftime ("%d-%m-%Y %H:%M%S"))
    print ("datetime formatado: ", a.strftime ("%d/%m/%y"))
    print ("datetime formatado: ", a.strftime ("%H:%M%S"))

    print(" 0 {1} e {0:%d}, o {2} e {0:%B}. " . format (a, 'dia', 'mes'))
    """
    '{}' . format() - O format nos permite colocar um determinado conteudo dentro dos colchetes.
    {0} - Faz referencia ao item que esta na posiçao 0 do format (variavel a).
    {0:%d} - Item na posiçao/chave 0 (zero) e desta posiçao queremos %d (valor dia)
    {0:%B} - Item na posiçao/chave 0 (zero) e desta posiçao queremos %B (valor mes)
    {1} - Faz referencia ao item que esta na posiçao 1 do format (string dia)
    {2} - Faz referencia ao item que esta na posiçao 2 do format (string mes).
    """
if __name__ == '__main__':
    datetime_data_e_hora()
