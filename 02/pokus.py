from random import randrange
cislo = randrange(2)
#print(cislo)

if cislo == 0 :
    tah_pocitace = "kámen"
elif cislo == 1 :
    tah_pocitace = "nůžky"
else :
    tah_pocitace = "papír"

#tah_pocitace = 'kámen'
tah_cloveka = input('kámen, nůžky, nebo papír? ')
print(tah_pocitace)

if tah_cloveka == 'kámen':
    if tah_pocitace == 'kámen':
        print('Plichta.')
    elif tah_pocitace == 'nůžky':
        print('Vyhrála jsi!')
    elif tah_pocitace == 'papír':
        print('Počítač vyhrál.')
elif tah_cloveka == 'nůžky':
    if tah_pocitace == 'kámen':
         print('Počítač vyhrál.')
    elif tah_pocitace == 'nůžky':
        print('Plichta.')
    elif tah_pocitace == 'papír':
        print('Vyhrála jsi!')
elif tah_cloveka == 'papír':
    if tah_pocitace == 'kámen':
        print('Vyhrála jsi!')
    elif tah_pocitace == 'nůžky':
        print('Počítač vyhrál.')
    elif tah_pocitace == 'papír':
        print('Plichta.')
else:
    print('Nerozumím.')