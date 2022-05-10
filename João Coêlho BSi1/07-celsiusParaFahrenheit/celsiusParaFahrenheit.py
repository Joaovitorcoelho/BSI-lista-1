
from calc import calculo
def main():

    print("Digite a temperatura em Celsius e ela será convertida para Fahrenheit")

    f = float(input("\n Digite a temperatura em Celsius "))

    
    resultado = calculo(f)
    print (f"\nA temperatura convertida será {resultado} graus Fahrenheit")


if __name__ == "__main__":
    main()