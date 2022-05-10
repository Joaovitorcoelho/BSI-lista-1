from calc import calculo
import math
def main():

    
    metros_pintar = int(input("\n Digite quantos metros você vai pintar "))

    litros_metro = 3
    litros_lata = 18
    resultado = calculo(metros_pintar,litros_lata,litros_metro)
    print (f"\nVocê vai gastar {math.ceil(resultado)} latas ")
 

if __name__ == "__main__":
    main()