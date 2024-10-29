par = 0
imp = 0
for i in range (10):
    num=int(input('digite um numero: '))
    if num % 2 == 0:
        par += 1
    elif num % 2 == 1:
        imp += 1
print("numeros pares",par)
print("numeros impar",imp)       