negativo=0
ppositivos=0
for i in range(5):
    v=int(input("digite um numer:" ))
    if v > negativo:
      ppositivos=ppositivos+v
    else:
      negativo=negativo+1
print(f"a quantidade de numeros negativos {negativo}")