def calculo (numero):
    centenas,dezenas = divmod(numero,100)
    dezenas,unidades = divmod(dezenas,10)


    return centenas, dezenas, unidades
