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
