#Atividade_1
def soma_tres_numeros(a,b,c):
    return a + b + c
a=int(input("digite um numero:"))
b=int(input("digite outro numero: "))
c=int(input("digite outro numero: "))
resultado=soma_tres_numeros(a,b,c)
print(resultado)
#Atividade_2
horas=float(input("digite seu horario em brasilia: "))
def horas_de_b(horas):
    horas=horas%12
if (horas>+12):
    print("P.H" , horas,)
if (horas<=12):
    print("A.m" , horas,)

#Atividade_3
import random

def jogar_craps():
    r = random.randint(2, 12)
    print(f"voce tirou {r}")

    if resultado in [7, 11]:
        print("voce tirou um numero natural pabens")
    elif resultado in [2, 3, 12]:
        print("creps")
    else:
        ponto = r
        print(f"o ponto roletado é {ponto} agora voce vai ter que tira {ponto} novamente.")
        while True:
            resultado = random.randint(2, 12)
            print(f"tirou {r}")
            if resultado == ponto:
                print("parabens voce tiro o ponto novamente voce ganhou")
                break
            elif resultado == 7:
                print("tiro 7 jau era")
                break


if __name__ == "__main__":
    jogar_craps()
