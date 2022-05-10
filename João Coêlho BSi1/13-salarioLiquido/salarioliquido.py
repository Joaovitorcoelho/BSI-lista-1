from calc import calculo
def main():

    
    salariohora = float(input("\n Digite o quanto você ganha por hora "))

    horames = float(input("\n Digite quantas horas você trabalha no mês "))


    
    salariorecebido = calculo(salariohora,horames)
    print (f"\nO seu salário do mês será {round(salariorecebido,2)} reais ")


if __name__ == "__main__":
    main()