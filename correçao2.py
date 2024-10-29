total=0
i=0
joao=0
jose=0
maria=0
nulo=0
branco=0 
while(i<6):
 canditado=int(input("informe seu canditado"))
 if canditado==0:
     break
 if canditado == 1:
     jose=+1
 if canditado==2:
     joao=+1
 if canditado==3:
     nulo=+1  
 if canditado==4:
    branco=+1
total+=jose+joao+nulo+branco    
 
    
