from calc import calculo
import math
def main():

    
    ovos = float(input("\n Digite a quantidade de ovos que você possui "))

    ovosqtd = calculo(ovos)
    print (f"\nVocê tem {math.ceil(ovosqtd)} duzias de ovos ")


if __name__ == "__main__":
    main()