
from calc import calculo
def main():

    

    valor1 = float(input("\n Digite a distancia que sera percorrida "))
    valor2 = float(input("\n Digite a Velocidade "))
    
    horas,minutos = calculo(valor1,valor2)
    print (f"\nO tempo que você vai levar será {int(horas)} : {int(minutos)} Horas")


if __name__ == "__main__":
    main()