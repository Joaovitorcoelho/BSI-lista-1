from calc import calculo
def main():

    
    dias = int(input("\n Digite quantos dias você alugou o carro "))

    quilometros = float(input("\n Digite quantos quilometros você rodou com o carro "))

    
    resultado = calculo(dias,quilometros)
    print (f"\nO valor que você tera que pagar será {resultado} reais")


if __name__ == "__main__":
    main()