from pickletools import float8
from calc import calculo
def main():

    
    prova1 = float(input("\n Digite qual nota você tirou na primeira prova "))

    prova2 = float(input("\n Digite qual nota você tirou na segunda prova "))

    exercicio1 = float(input("\n Digite qual nota você tirou no primeiro exercicio "))

    exercicio2 = float(input("\n Digite qual nota você tirou no segundo exercicio "))

    
    resultado = calculo(prova1,prova2,exercicio1,exercicio2)
    print (f"\nA sua nota será {float(resultado)} ")


if __name__ == "__main__":
    main()