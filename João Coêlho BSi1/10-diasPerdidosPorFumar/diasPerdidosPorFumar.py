from calc import calculo
def main():

    
    cigarros = int(input("\n Digite quantos cigarros você fuma por dia "))

    anos = int(input("\n digite a quantos anos você fuma "))

    min_cig = 10
    
    resultado = calculo(cigarros,anos,min_cig)
    print (f"\nVocê perdeu {int(resultado)} dias de vida")


if __name__ == "__main__":
    main()