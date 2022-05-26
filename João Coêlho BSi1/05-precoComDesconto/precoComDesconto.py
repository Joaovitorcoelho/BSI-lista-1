
from calc import calculo
def main():

    

    preco = float(input("\n Digite o preço do produto "))
    desconto = float(input("\n Digite a porcentagem de desconto do produto "))
    
    resultado = calculo(preco,desconto)
    print (f"\nO preço do produto será {resultado} Reais")


if __name__ == "__main__":
    main()
