# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 10:50:29 2023

@author: dpe
"""
#----------------------------------------------------------------------------#

# a. Variabler og Datatyper
tekst = "Dette er tekst! duh!"
heltall = 10
desimaltall = 20.5

#----------------------------------------------------------------------------#

# b. Operasjoner med Variabler
a = 5
b = 2
sum = a + b
print("Sum: ", sum)
differanse = a - b
print("Differanse: ", differanse)
produkt = a * b
print("Produkt: ", produkt)
kvotient = a / b
print("Kvotient: ", kvotient)
#integer division (floor division) 
int_div = a // b
print("Integer division: ", int_div)

#----------------------------------------------------------------------------#

# c. Strenger og deres metoder
tekst = "geologi OG geoteknikk er Spennende!"
print(tekst)
# Gjør strengen til store bokstaver
stor = tekst.upper()
print(stor)

# Gjør strengen til små bokstaver
liten = tekst.lower()
print(liten)

# Første bokstav i hvert ord til stor bokstav
tittel = tekst.title()
print(tittel)

# Sjekk om strengen starter med bestemte tegn
starter_med_geo = tekst.startswith("geo")
print(starter_med_geo)

# Finn indeksen til et bestemt ord/tegn i strengen
pos = tekst.find("Spennende")
print(pos)

# Det er et problem med "strenger", og det er hvis man bruker '\', som ofte brukes i fil-baner
filbane = 'c:\docs\new'
print(filbane)

# kan bruke raw string 'r' eller 'kansellere spesialtegn med en \'
filbane = r'c:\docs\new'
print(filbane)

filbane = 'c:\docs\\new-doubleslash'
print(filbane)

#----------------------------------------------------------------------------#

# d. Tall og deres metoder
tall = -5.543

# Få absolutt verdi av et tall
abs_tall = abs(tall)
print(abs_tall)

# Rund av et tall, med spesifisert antall desimaler
avrundet_tall = round(tall, 2)

# Konvertere et desimaltall til heltall (uten avrunding)
heltall = int(tall)

# Maksimum og minimum av en sekvens
max_tall = max(1, 2, 3, 4, 5)
print(max_tall)
min_tall = min(1, 2, 3, 4, 5)
print(min_tall)

#----------------------------------------------------------------------------#

# e. Lister
jordtyper = ["sand", "leire", "grus", "morene"]

# Legger til en ny jordtype
jordtyper.append("silt")
print(jordtyper)

# Fjern et element fra listen
jordtyper.remove("sand")
print(jordtyper)

# Inverter rekkefølgen av elementene i listen
jordtyper.reverse()
print(jordtyper)

# Sorter listen
jordtyper.sort()
print(jordtyper)

# Henter den første jordtypen
første_jord = jordtyper[0]
print(første_jord)

# Finn indeksen til et element i listen og deretter hente jordtypen på den 
# gitte indeksen
index_for_leire = jordtyper.index("morene")
jordtype_leire = jordtyper[index_for_leire]
print(jordtype_leire)

#----------------------------------------------------------------------------#

# f. Betingede uttrykk
jordtyper = ["sand", "leire", "grus", "morene"]

for jordtype in jordtyper:
    if jordtype == "sand":
        print(jordtype, "- god drenering.")
    elif jordtype == "leire":
        print(jordtype, "- dårlig drenering, holder godt på vann.")
    elif jordtype == "grus":
        print(jordtype, "- veldig grov, drenerer raskt.")
    elif jordtype == "silt":
        print(jordtype, "- moderat drenering, finere enn sand, men grovere enn leire.")
    else:
        print(jordtype, "- blandet materiale, ulike egenskaper.")

#----------------------------------------------------------------------------#
