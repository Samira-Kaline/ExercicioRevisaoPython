cont = 0
print('Telefonou para a vitima?')
reposta = raw_input()
if(reposta=='Sim'):
    cont+=1
    
print('Esteve no local do crime?')
reposta = raw_input()
if(reposta=='Sim'):
    cont+=1
    
print('Mora perto da vitima?')
reposta = raw_input()
if(reposta=='Sim'):
    cont+=1
    
print('Devia para vitima?')
reposta = raw_input()
if(reposta=='Sim'):
    cont+=1
    
print('Ja trabalhou com a vitima?')
reposta = raw_input()
if(reposta=='Sim'):
    cont+=1
    
if(cont==2):
    print('Suspeita')
    
elif(cont==3 or cont==4):
    print('Cúmplice')
    
elif(cont==5):
    print('Assassino')
    
else:
    print('Inocente')
