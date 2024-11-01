pedido_mais_caro=0
pedido_mais_baixo=float('inf')
quantidades_de_pedidos=0
total=0
totall=0
totalp=1

while True:
    p=input("Qual tamanho de pizza gostaria?:")
    if p == 'pequena': 
        print("O valor da pizza é de R$-20")
        totall=20
    elif p == 'media': 
        print("O valor da pizza média é de R$-30")
        totall=30
    elif p == 'grande': 
        print('O valor da pizza grande é de R$-40')
        totall=40

    g=input('Gostaria de adicionar ingredientes extras?:')
    if g == 'sim':
        print("Cada ingrediente extra vale R$ 5,00")
        print("Temos calabresa, mussarela, bacon, tomate, cebola, bacon")
        
    c=input("Gostaria de adicionar cebola?:")
    if c == "sim": 
        total+=5
        totalp+=1
    u=input("Gostaria de adicionar mussarela?:")
    if u == "sim": 
        total+=5
        totalp+=1
    ll=input("Gostaria de adicionar calabresa?:")
    if ll == "sim": 
        total+=5
        totalp+=1
    t=input("Gostaria de adicionar tomate?:")
    if t =="sim": 
        total+=5
        totalp+=1
    b=input("Gostaria de adicionar bacon?:")
    if b == "sim": 
        total+=5
        totalp+=1

    g=input("Gostaria de refrigerante?:")
    if g == "sim": 
        total+=8
        totalp+=1

    ssss=total+totall
    print("O valor da pizza é:", ssss)
    print("Total de ingredientes:", totalp)

    if ssss > pedido_mais_caro:
        pedido_mais_caro=ssss
    if ssss < pedido_mais_baixo:
        pedido_mais_baixo=ssss

    quantidades_de_pedidos+=1
    total=0
    totall=0
    totalp=1

    o=input("Gostaria de outra pizza?")
    if o == "não": 
        break

print("Pizza mais cara:", pedido_mais_caro)
print("Pizza mais barata:", pedido_mais_baixo)
print("Total de pedidos:", quantidades_de_pedidos)

