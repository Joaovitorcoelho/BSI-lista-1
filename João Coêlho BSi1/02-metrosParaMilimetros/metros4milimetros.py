
from calc import calculo
def main():

    print ("digite o valor que será convertido de metros para milimetros")

    valor1 = int (input("\n Digite o Valor em metros "))

    
    resultado = calculo(valor1)
    print (f"\n{resultado} milimetros ")


if __name__ == "__main__":
    main()