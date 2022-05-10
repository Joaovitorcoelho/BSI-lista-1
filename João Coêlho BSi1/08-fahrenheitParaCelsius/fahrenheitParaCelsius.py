
from calc import calculo
def main():

    print("Digite a temperatura em Fahrenheit e ela será convertida para Celsius")

    f = float(input("\n Digite a temperatura em Fahrenheit "))

    
    resultado = calculo(f)
    print (f"\nA temperatura convertida será {resultado} graus Celsius")


if __name__ == "__main__":
    main()