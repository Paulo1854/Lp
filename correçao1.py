cont1=0
cont2=0
cont3=0
i=1
while(i>0):
    n=int(input("digite um numero"))
    if(n>0)and(n<25):
        cont1+=1
    if (n>=51)and(n<=75):
        cont2+=1  
    if (n>=76)and(n<=100):
        cont3+=1  
    if(n<0):
      break
print("itervalo de 0 a 25 é ",cont1)
print("itervalo de 50 a 75 é ",cont2)
