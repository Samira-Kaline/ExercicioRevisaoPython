nota1 = int(raw_input('Digite a primeira nota: '))
nota2 = int(raw_input('Digite a segunda nota: '))
nota3 = int(raw_input('Digite a terceira nota: '))

media = (nota1+nota2+nota3)/3

if(media>=7 and media<10):
    print('Aprovado')
    
elif(media<7):
    print('Reprovado')
    
else:
    print('Aprovado com Distincao')
    
