impa = 0
par = 0
for i in range(10):
   valor=int(input("informe um  valor")) 
   if valor % 2 == 0:
      print("par")
      par=par+1
   else:
     print("impa")
print(par)
print(impa)