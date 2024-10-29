#1
'''a=float(input("digite sua altura: "))
g=str(input("voce é homem ou mulher : "))
if(g =='homem'):
 s=(a*72.7)-58
 print("o pesso ideal para sua altura",s)
else:
 m=(a*62.1)-44,7
print("o pesso ideal para sua altura",m)'''
#2
'''s=int(input("informe quanto voce ganha por hora: "))
m=int(input("informe quantas horas voce trabalha por més: "))
c=s*m
print("voce ganha",c)'''
#3
'''n=str(input("digite seu nome: "))
ler=len(n)
if ler >= 3 : 
 i=int(input("informe sua idade: "))
if i < 150 : 
  s=int(input("informe seu salrio: "))
if s > 0 : 
 sx=(input("informe seu sexo: "))
if sx == 'masculino'or 'feminino':
  es=(input('informe seu estado civil: '))
  if es == 'solteiro':
    print('valido')   
    if es == 'casado':
     print('valido')
     if es == 'viuvo':   
      print('valido')
      if es == 'divorciado':
       print('valido')'''
#4
'''def fibonacci():
    a ,b=0, 1
    while b <= 700:  
        print(b, end="'") 
        a ,b=b ,a + b
fibonacci()'''
#5
'''n=int(input("digited um numero: "))
if n > 1:
    for i in range(2,n):
        if n % i == 0:
            print("nao é primo")
            break
        else:
            print("primo")  
            break          
else:
    print("nao é um numero primo")'''
#6
'''mais=0
menos=10000
cmenos=None
cmais=0
for i in range(2):
    numero=int(input("digite seu numero:"))
    altura=float(input("digite sua altura: "))
    if altura > mais:
        mais=altura 
        cmais = numero
    if altura < menos:
        menos=altura
        cmenos = numero
print(f"aluno mais alto",{mais},{cmais})
print(f"aluno mais baixo",{menos},{cmenos})'''
#7
gabarito={"a","b","c","d","e","e","d","c","b","a"}
total_de_acertos=0
total_de_erros=0
total_de_alunos=0
soma_notas=0
while True:
    pergunta1=input("responde a questão 1:")
    pergunta2=input("responde a questão 2:")
    pergunta3=input("responde a questão 3:")
    pergunta4=input("responde a questão 4:")
    pergunta5=input("responde a questão 5:")
    pergunta6=input("responde a questão 6:")
    pergunta7=input("responde a questão 7:")
    pergunta8=input("responde a questão 8:")
    pergunta9=input("responde a questão 9:")
    pergunta10=input("responde a questão 10:")
    if pergunta1 == 'a':
     total_de_acertos+=1
     soma_notas+=1
    else:
     total_de_erros+=1
    if pergunta2 == 'b':
     total_de_acertos+=1
     soma_notas+=1
    else:
     total_de_erros+=1   
    if pergunta3 == 'c':
     total_de_acertos+=1
     soma_notas+=1
    else:
     total_de_erros+=1
    if pergunta4 == 'd':
     total_de_acertos+=1
     soma_notas+=1
    else: 
     total_de_erros+=1  
    if pergunta5 == 'e':
     total_de_acertos+=1
     soma_notas+=1
    else:
     total_de_erros+=1 
    if pergunta6 == 'e':
     total_de_acertos+=1
     soma_notas+=1
    else:
       total_de_erros+=1
    if pergunta7 == 'd':
     total_de_acertos+=1
     soma_notas+=1
    else:
     total_de_erros+=1  
    if pergunta8 == 'c':
     total_de_acertos+=1
     soma_notas+=1
    else:
     total_de_erros+=1    
    if pergunta9 == 'b':
     total_de_acertos+=1
     soma_notas+=1
    else:
     total_de_erros+=1 
    if pergunta10 == 'a':
     total_de_acertos+=1
     soma_notas+=1
    else:
     total_de_erros+=1
    print(f"total de erros",{total_de_erros})
    print(f"total de acertos",{total_de_acertos}) 
    print(f"soma total",{soma_notas})
    for cntina in range(1):
     cntina=input("quer continua: ")
    if cntina == "não":
     break

    






    



 
 


