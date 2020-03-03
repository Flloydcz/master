#Input sam o sobe je text, je mu třeba říct aby input bral jako číslo.
#INT je nedesetiné číslo
#float je i desetiné číslo
strana = float(input("číslo cype:"))
cislo_je_spravne = strana > 0
#tato funkce je if True, probehne bez dalsi definice jen pokud je to if True
if cislo_je_spravne:
    print('Obvod čtverce se stranou' , strana, 'je', (4 * strana))
    print('Obsah čtverce se stranou' , strana, 'je', (strana * strana))
else:
    print("Číslo musí být kladné cype")
print ("Dík a čau")
#pravda = 1 < 3
#print(pravda)
#nepravda = 1 == 3
#print(nepravda)