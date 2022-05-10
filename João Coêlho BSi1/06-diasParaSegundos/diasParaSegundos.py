
from calc import calculo
def main():

    print("Digite uma data em dias com horas, minutos e segundos separadamente e ela será transformada em segundos")

    valor1 = int(input("\n Digite a quantidade de dias "))
    valor2 = int(input("\n Digite as horas "))
    valor3 = int(input("\n Digite os minutos "))
    valor4 = int(input("\n Digite os segundos "))
    
    resultado = calculo(valor1,valor2,valor3,valor4)
    print (f"\nO tempo que você digitou será {resultado} segundos")


if __name__ == "__main__":
    main()