# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 10:55:03 2023

@author: dpe
"""
#----------------------------------------------------------------------------#

# a. Åpne en fil med open()og les innholdet:
from pathlib import Path
fil_bane = Path('../../data/03_grunnvanns_data.csv')
file = open(fil_bane, 'r', encoding='utf-8')
print(file)

#----------------------------------------------------------------------------#

# b. Leseinnholdet av en fil:
content = file.readlines()
print(content)

#----------------------------------------------------------------------------#

# c. Lukking av en fil:
file.close()

#----------------------------------------------------------------------------#

# d. Hvorfor bruker vi with når vi åpner filer?
fil_bane = Path('../../data/03_grunnvanns_data.csv')
with open(fil_bane, 'r', encoding='utf-8') as file:
    content = file.readlines()
    print(content)

# test to illustrate
# content = file.readlines()

#----------------------------------------------------------------------------#

# f. Håndtering av filfeil
try:
    with open('myfile.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Filen ble ikke funnet!")

#----------------------------------------------------------------------------#

#  Eksempel på å skrive til en fil. La oss si at vannhøyden fra filen vi leste 
# inn er feil, med 0.56m. Vi må da ordne den
fil_bane = Path('../../output/03_korrigert_vannhøyde.csv')
with open(fil_bane, 'w') as file:
    # lager en ny liste som skal holde de nye verdiene
    processed_data = []
    # skriver ut en streng for "å vise" at det er en ny fil
    file.write("Dette er en ny fil, og med korrigert data fra forrige fil!\n\n")
    # looper gjennom opprinnelig data
    for linje in content:
        # splitter hver linje med "," ned i elementer og fjerner "nylinje \n" 
        # bokstaven (se over)
        elementer = linje.strip().split(',')
        # len(elementer) returnerer antall elementer i linjen.
        # len(elementer) > 1 Sjekker om det er mer enn 1 element i linjen. 
        # Viktig sjekk siden vi vil ha et element etter
        # "Sted" (som da blir vannhøyde).
        # elementer[1].replace('.', '', 1).isdigit()
        # --> elementer[1] er det andre elementet i element listen, som 
        # da er Vannhøyde
        # --> replace('.', '', 1) bytter første opptreden av "." med ""
        # (tom streng). 1-tallet spesifiserer bytte 1 gang
        # --> isdigit() sjekker (etter at vi har fjernet desimalplassen) om 
        # strengen bare inneholder tall. Returnerer True.
        if len(elementer) > 1 and elementer[1].replace('.', '', 1).isdigit():
            # Kaster tall-strengen til desimaltall, så legger på feilmargiene. 
            # Deretter avrunder vi desimaltallet til 2
            # desimaler før man konverterer den tilbake til en streng og lagrer
            # den tilbake i elementer listen.
            elementer[1] = str(round(float(elementer[1]) + 0.56, 2))
        # ','.join(elementer) --> lager en sammenhengende streng igjen fra 
        # elementer listen. Dette gjøres for hver linje
        # processed_data.append() --> legger på den nye strengen i den 
        # prosesserte listen
        processed_data.append(','.join(elementer))
    #skriver ut den nye listen til en fil
    for line in processed_data:
        file.write(line + '\n')
    print("Ferdig å skrive korrigerte vannhøyder!")

#----------------------------------------------------------------------------#
