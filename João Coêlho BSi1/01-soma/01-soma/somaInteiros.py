
from calc import calculo
def main():

    print ("digite dois valores")

    valor1 = int (input("\n Primeiro número"))
    valor2 = int (input("\n Segundo número"))
    
    resultado = calculo(valor1,valor2)
    print (f"\n{valor1} + {valor2} = {resultado}")


if __name__ == "__main__":
    main()