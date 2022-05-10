from calc import calculo
def main():

    
    numero = int(input("\n Digite um número menor que 1000 "))


    
    centenas, dezenas, unidades = calculo(numero)


    print (f"\n o número que você digitou tem {(centenas)} centenas, {(dezenas)} dezenas, {(unidades)} unidades ")
 

if __name__ == "__main__":
    main()