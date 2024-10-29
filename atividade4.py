n=int(input("informe um codigo"))
n1=float(input('digite o total de vendas; '))
if ( n<= 100):
    s=(n1/100)*0
    print(f"{s}%")
if (n1>100)and(n1<=350):
    y=(n1/100)*6
    print(f"{y}%")
if (n1>350):
    t=(n1*10)/100
    print(f"{t}%")