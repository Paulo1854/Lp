maiorP=0
menorP=0
maiorI=0
menorI=0
maiorA=0
menorA=0
for i in range(2):
    p=int(input("inform o peso "))
    i=int(input("informe a idade "))
    a=int(input("informe a altura"))
    if p > maiorP:
        maiorP = p
        maior+=1
    if p < menorP:
        menorP= p
    if i > maiorI:
        maiorI = i
    if i < menorI:
        menorI = i
    if a > maiorA:
        maiorI = a
    if a > menorI:
        menorI = a          

    print("pesso maior",maior)  
