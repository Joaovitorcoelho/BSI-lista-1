
from calc import calculo
def main():

    

    valor1 = float(input("\n Digite o seu salario atual "))
    valor2 = float(input("\n Digite a sua porcentagem de aumento "))
    
    resultado = calculo(valor1,valor2)
    print (f"\nO seu salário será {resultado} Reais")


if __name__ == "__main__":
    main()