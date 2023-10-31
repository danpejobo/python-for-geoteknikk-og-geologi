# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 10:45:23 2023

@author: dpe
"""

#----------------------------------------------------------------------------#

# dette er en kommentar

"""Detter er også en kommentar. Denen brukes ofte i forbindelse med noe som 
heter doc-string, en beskrivelse til funksjoner"""

#----------------------------------------------------------------------------#

# 1. Skrive ut en beskjed

# Første kode man ofte skrive på kurs
print("Hei, verden!")

#----------------------------------------------------------------------------#

# 2. variabler

# I python trenger man ikke beskrive datatypene

#string (str)
navn = 'Ola Normann'

#integer (int)
alder = 30

#for desimaltall må man bruke punktum - prøv å skifte til komma
brøk = 6.6

#printe ut resultatene
print (navn, '\t-->', type(navn))
print (alder, '\t\t-->', type(alder))
print (brøk, '\t\t-->', type(brøk))

#----------------------------------------------------------------------------#

# 3. Grunnleggende operasjoner

a = 5
b = 3
sum = a + b
print(sum)

#----------------------------------------------------------------------------#

# 4. Lister

# En samling av verdier som kan inneholde tall, strenger eller andre objekter.

jordtyper = ["sand", "leire", "grus"]
print(jordtyper, '-->', type(jordtyper))

# Finne størrelsen på en liste er ofte nødvendig ved å iterere gjennom den
# lenght() <-- innebygd funksjon som returnerer et tall

length = len(jordtyper)
print(length)

#----------------------------------------------------------------------------#

# 5. Betingelser

# Lik: a == b
# Ikke Lik: a != b
# Mindre enn: a < b
# Mindre eller lik: a <= b
# Større enn: a > b
# større eller lik: a >= b

temperatur = 20
if temperatur > 25:
    print("Det er varmt!")
elif temperatur == 22:
		print("Det er passelig temperatur!")
else:
    print("Det er kjølig.")

#----------------------------------------------------------------------------#

# 6. Løkker

# Utfører en handling flere ganger!

for i in range(3):
    print("Dette er iterasjon", i+1)

for element in jordtyper:
    if element == "grus":
        print(element)

# enumerate() <-- returnerer en tuple med en index og verdien, veldig handy 
# når man må ha både indeks og verdien

for idx, element in enumerate(jordtyper):
    print (idx, element)
    
#----------------------------------------------------------------------------#

# 7. ØVELSE

# Gitt listene:

strøk = [225, 133, 100, 150, 90]
fall = [40, 35, 66, 20, 15]
bergart = ["granitt", "skifer", "sandstein", "gneis", "dioritt"]

# ved å iterere gjennom listene print bergartene som har fallmålinger mindre enn 35 grader
for idx, elem in enumerate(fall):
    if elem < 35:
        print(bergart[idx])