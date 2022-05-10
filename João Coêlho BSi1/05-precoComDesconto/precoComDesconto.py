
from calc import calculo
def main():

    

    valor1 = float(input("\n Digite o preço do produto "))
    valor2 = float(input("\n Digite a porcentagem de descont do produto "))
    
    resultado = calculo(valor1,valor2)
    print (f"\nO preço do produto será {resultado} Reais")


if __name__ == "__main__":
    main()