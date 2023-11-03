## 1\. **Introduksjon (10 minutter):**

#### a. Hvorfor Python?

- Populært programmeringsspråk.
- Allsidig: webutvikling, vitenskapelig databehandling, maskinlæring, automatisering, og mer. 
  - google, dropbox, youtube, yahoo!, NASA
  - reddit --> stort sett kodet i python
- Stort fellesskap og mange biblioteker.

#### b. Anaconda:

- En fri, åpen kildekode distribusjon av Python og R for vitenskapelig databehandling og maskinlæring.
- Hjelper med pakke-, avhengighets- og miljøhåndtering.

#### c. Biblioteker:

Pypi.org

- pandas
- numpy
- matplotlib

#### d. Grunnleggende Python syntaks og eksempler

**1\. Skrive ut en beskjed:**

- Dette er ofte den første koden nybegynnere prøver i et nytt programmeringsspråk.

```python
# dette er en kommentar

"""Detter er også en kommentar. Denen brukes ofte i forbindelse med noe som heter doc-string, 
en beskrivelse til funksjoner"""
```

```python
# 1. Skrive ut en beskjed

# Første kode man ofte skrive på kurs
print("Hei, verden!")
```

**2\. Variabler:**

- I Python trenger du ikke spesifisere datatypen når du deklarerer en variabel.

```python
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
```

**3\. Grunnleggende operasjoner:**

- Du kan utføre matematiske operasjoner direkte.

```python
# 3. Grunnleggende operasjoner

a = 5
b = 3
sum = a + b
print(sum)
```

**4\. Lister:**

- En samling av verdier som kan inneholde tall, strenger eller andre objekter.

```python
# 4. Lister

# En samling av verdier som kan inneholde tall, strenger eller andre objekter.

jordtyper = ["sand", "leire", "grus"]
print(jordtyper, '-->', type(jordtyper))

# Finne størrelsen på en liste er ofte nødvendig ved å iterere gjennom den
# lenght() <-- innebygd funksjon som returnerer et tall

length = len(jordtyper)
print(length)
```

**5\. Betingelser:**

- Brukes for å ta beslutninger i koden, og det er 6 forskjellige.

```python
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
```

**6\. Løkker:**

- For å utføre en handling flere ganger.

```python
# 6. Løkker

# Utfører en handling flere ganger!

for i in range(3):
    print("Dette er iterasjon", i+1)

for element in jordtyper:
    if element == "grus":
        print(element)

# enumerate() <-- returnerer en tuple med en index og verdien, veldig handy når man må ha både indeks og verdien

for idx, element in enumerate(jordtyper):
    print (idx, element)
```

**Deltakeraktivitet:**

- Be deltakerne om å prøve eksemplene ovenfor i deres egne Python-miljøer. Du kan guide dem gjennom hvert eksempel, forklare hva det gjør, og deretter la dem kjøre det selv.

**7\. Øvelse:**

```python
# 7. ØVELSE

# Gitt listene:

strøk = [225, 133, 100, 150, 90]
fall = [40, 35, 66, 20, 15]
bergart = ["granitt", "skifer", "sandstein", "gneis", "dioritt"]

# ved å iterere gjennom listene print bergartene som har fallmålinger mindre enn 35 grader
for idx, elem in enumerate(fall):
    if elem < 35:
        print(bergart[idx])
```

---

## 2\. **Grunnleggende om Python (15 minutter):**

#### a. **Variabler og Datatyper**

Variabler i Python kan tenkes på som navngitte beholdere som kan lagre data. Python er dynamisk typet, noe som betyr at du ikke trenger å deklarere datatypen til en variabel når du oppretter den.

**Eksempler:**

```python
#a. Variabler og Datatyper
tekst = "Dette er tekst! duh!"
heltall = 10
desimaltall = 20.5
```

Her har vi en streng, et heltall og et flyttall (eller desimaltall). Hver har sin egen bruk avhengig av datatypen.

#### b. **Operasjoner med Variabler**

Med variabler kan du utføre operasjoner, spesielt med tall. Dette inkluderer grunnleggende aritmetikk som addisjon, subtraksjon, multiplikasjon og divisjon.

**Eksempler:**

```python
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
```

#### c. **Strenger og deres metoder**

Strenger er sekvenser av tegn. I Python kan du bruke en rekke innebygde metoder for å jobbe med strenger. Strenger i Python har en rekke nyttige metoder for tekstbehandling.

**Eksempler:**

```python
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
```

#### d. **Tall og deres metoder**

Selv om tall i Python (både heltall og flyttall) ikke har så mange metoder som strenger og lister, er det noen nyttige funksjoner og metoder vi kan utforske.

**Eksempler:**

```python
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
```

#### e. **Lister**

En liste er en samling av verdier som kan endres. Den kan inneholde enhver datatype og kan også inneholde blandede datatyper. De er utrolig fleksible og har mange innebygde metoder for å legge til, fjerne eller manipulere elementer.

**Eksempler:**

```python
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

# Finn indeksen til et element i listen og deretter hente jordtypen på den gitte indeksen
index_for_leire = jordtyper.index("morene")
jordtype_leire = jordtyper[index_for_leire]
print(jordtype_leire)
```

#### f. **Betingede uttrykk**

Med betingede uttrykk kan du la programmet ditt ta beslutninger basert på bestemte kriterier.

**Eksempler:**

```python
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
```

**Deltakeraktivitet:**
Oppfordre deltakerne til å prøve eksemplene ovenfor. Gi dem tid til å eksperimentere med forskjellige verdier og se hvordan resultatene endres. Gjennom denne interaktive økten vil deltakerne få en dypere forståelse av grunnleggende Python-konsepter.

---

## 3\. Tilgang til og lesing av filer:

Når vi arbeider med programmering og dataanalyse, er det ofte nødvendig å lese data fra eksterne filer eller skrive resultater til filer for lagring. Python gir en innebygd funksjon, `open()`, for å håndtere filer.

#### a. **Åpne en fil med** `open()`**og les innholdet**:

For å åpne en fil i Python, bruker vi `open()`\-funksjonen.

- Bruk pathlib for å bygge filbaner

**Eksempel:**

```python
# a. Åpne en fil med open()og les innholdet:
from pathlib import Path
fil_bane = Path('../data/03_grunnvanns_data.csv')
file = open(fil_bane, 'r', encoding='utf-8')
print(fil)
```

Her åpner vi en fil kalt 'grunnvanns_data.csv' i lesemodus ('r').

- "file" en variabel som representerer en *file object* eller *file handle*. Når du åpner en fil med `open()`, returnerer Python et file object som du kan bruke til å lese fra eller skrive til filen. Dette objektet gir deg metoder for å interagere med filinnholdet.

#### b. **Leseinnholdet av en fil:**

Når en fil er åpnet i lesemodus, kan vi lese dens innhold med forskjellige metoder:

- `read()`: Les hele filinnholdet som en enkelt streng.
- `readline()`: Les neste linje fra filen. Som enkelte strenger
- `readlines()`: Les alle linjene i en fil og returner en liste med linjer.

**Eksempel:**

```python
# b. Leseinnholdet av en fil:
content = file.readlines()
print(content)
```

#### c. **Lukking av en fil:**

Det er viktig å alltid lukke filen etter bruk for å frigjøre ressurser:

**Eksempel:**

```python
# c. Lukking av en fil:
file.close()
```

#### d. **Hvorfor bruker vi** `with` når vi åpner filer?

Bruken av `with`\-nøkkelordet når du åpner en fil sikrer at filen lukkes automatisk når blokken under `with` er ferdig. Dette kalles kontekthåndtering og er en mer robust måte å håndtere filer på, spesielt hvis det oppstår feil under filoperasjoner.

**Eksempel:**

```python
# d. Hvorfor bruker vi with når vi åpner filer?
from pathlib import Path
fil_bane = Path('../data/03_grunnvanns_data.csv')
with open(fil_bane, 'r', encoding='utf-8') as fil:
    content = file.readlines()
    print(content)

# test to illustrate
# content = file.readlines()
```

Her vil filen 'myfile.txt' bli automatisk lukket etter at `print(content)`\-linjen er kjørt.

#### e. **Forskjellige lese- og skrivemoduser:**

- `'r'`: Lese-modus. (standard)
- `'w'`: Skrivemodus. Overskriver filen hvis den eksisterer, eller oppretter en ny fil.
- `'a'`: Legg til modus. Legger til innhold på slutten av en eksisterende fil eller oppretter en ny fil.
- `'b'`: Binær modus. Brukes med de ovennevnte modiene for å lese/skrive binærfiler, som bilder.

#### f. **Generelle "must know" standard metoder for filhåndtering:**

- `file.write(text)`: Skriver en streng til en fil. Brukes ofte i skrivemodus (`'w'`) eller legg til modus (`'a'`).
- `file.seek(offset)`: Flytter filpekeren til en bestemt posisjon. Nyttig hvis du vil lese eller skrive fra et bestemt sted i en fil.
- `file.tell()`: Gir den nåværende posisjonen til filpekeren.

**Håndtering av filfeil:**

```python
# Håndtering av filfeil
try:
    with open('myfile.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Filen ble ikke funnet!")
```

**Eksempel på skriving til en fil:**

```python
#  Eksempel på å skrive til en fil. La oss si at vannhøyden fra filen vi leste inn er feil, med 0.56m. Vi må da ordne den
fil_bane = Path('../output/03_korrigert_vannhøyde.csv')
with open(fil_bane, 'w') as file:
    # lager en ny liste som skal holde de nye verdiene
    processed_data = []
    # skriver ut en streng for "å vise" at det er en ny fil
    file.write("Dette er en ny fil, og med korrigert data fra forrige fil!\n\n")
    # looper gjennom opprinnelig data
    for linje in content:
        # splitter hver linje med "," ned i elementer og fjerner "nylinje \n" bokstaven (se over)
        elementer = linje.strip().split(',')
        # len(elementer) returnerer antall elementer i linjen.
        # len(elementer) > 1 Sjekker om det er mer enn 1 element i linjen. Viktig sjekk siden vi vil ha et element etter
        # "Sted" (som da blir vannhøyde).
        # elementer[1].replace('.', '', 1).isdigit()
        # --> elementer[1] er det andre elementet i element listen, som da er Vannhøyde
        # --> replace('.', '', 1) bytter første opptreden av "." med ""(tom streng). 1-tallet spesifiserer bytte 1 gang
        # --> isdigit() sjekker (etter at vi har fjernet desimalplassen) om strengen bare inneholder tall. Returnerer True.
        if len(elementer) > 1 and elementer[1].replace('.', '', 1).isdigit():
            # Kaster tall-strengen til desimaltall, så legger på feilmargiene. Deretter avrunder vi desimaltallet til 2
            # desimaler før man konverterer den tilbake til en streng og lagrer den tilbake i elementer listen.
            elementer[1] = str(round(float(elementer[1]) + 0.56, 2))
        # ','.join(elementer) --> lager en sammenhengende streng igjen fra elementer listen. Dette gjøres for hver linje
        # processed_data.append() --> legger på den nye strengen i den prosesserte listen
        processed_data.append(','.join(elementer))
    #skriver ut den nye listen til en fil
    for line in processed_data:
        file.write(line + '\n')
```

---

## 4\. **Introduksjon til numpy (10 minutter):**

#### a. Hvorfor og hva er numpy?

`numpy` er et essensielt verktøy for de som jobber med numeriske data. Det gir støtte for å håndtere store sett av målinger, utføre beregninger, og analysere data på en effektiv måte.

- Hurtigere og mer minneeffektivt enn rene Python-lister.
- Brukt for matematiske operasjoner på store datamengder.

`numpy` (Numerical Python) gir funksjonalitet for å arbeide med store, multidimensjonale arrays og matriser av numerisk data. Det er spesielt nyttig for raske operasjoner på grupper av målinger, som for eksempel strøk/fall-målinger i geologi.

#### b. Grunnleggende numpy-array:

```python
# b. Grunnleggende numpy-array:
import numpy as np
from pathlib import Path
fil_bane = Path('../data/04_numpy_array.csv')
# Leser inn data fra en CSV-fil
# 'delimiter' angir at hver verdi er separert med et semikolon
# 'dtype=int' angir at vi ønsker å konvertere disse verdiene til heltall, kan også være "float" eller "str"

målinger = np.genfromtxt(fil_bane, delimiter=';', dtype=int, skip_header=1)
print(målinger)
```

#### c. **Operasjoner med geologiske numpy arrays:**

**Eksempler:**

```python
# c. Operasjoner med geologiske numpy arrays: 
# Beregn gjennomsnittlig strøk og fall 
gjennomsnitt_strøk = np.mean(målinger[:, 0]) print("Gj.strøk: ", gjennomsnitt_strøk) 
gjennomsnitt_fall = np.mean(målinger[:, 1]) print("Gj.fall: ", gjennomsnitt_fall)
```

#### d. **Nyttige numpy funksjoner for geologiske data:**

**Eksempler:**

```python
# d. Nyttige numpy funksjoner for geologiske data:
# Finn maksimum og minimum fall-verdier
max_fall = np.max(målinger[:, 1])
print("Maks fall: ", max_fall)
min_fall = np.min(målinger[:, 1])
print("Min fall: ", min_fall)

# Beregn standardavvik for strøk-verdier
std_dev_strøk = np.std(målinger[:, 0])
print("Std.avvik strøk: ", std_dev_strøk)
```

#### e. **Indeksering og skjæring av geologiske data:**

**Eksempler:**

```python
# e. Indeksering og skjæring av geologiske data:
# Hent første strøk/fall-måling
første_måling = målinger[0]

# Hent alle strøk-verdier
alle_strøk = målinger[:, 0]

# Hent strøk/fall-målinger med fall større enn 25 grader
høyt_fall = målinger[målinger[:, 1] > 25]
```

---

## 5\. **Introduksjon til pandas (20 minutter):**

#### a. Hvorfor og hva er pandas?

`pandas` er et kraftig verktøy i Python for dataanalyse. Det gir strukturer som DataFrames for å håndtere og analysere strukturerte data enkelt og effektivt.

- Kraftig for databehandling og analyse.
- Lett å lese inn og skrive ut data fra ulike kilder (f.eks. CSV, Excel).

`pandas` (Python Data Analysis Library) er bygget på toppen av `numpy` og gir to hoveddatastrukturer: `Series` og `DataFrame`. Disse gjør det enkelt å importere, rense, manipulere og analysere data i Python.

#### b. Grunnleggende DataFrame med geologiske data:

```python
import pandas as pd
# b. Grunnleggende DataFrame med geologiske data:
# Definerer dataen
data = {
    'Bergartstype': ['Granitt', 'Skifer', 'Sandstein', 'Kalkstein', 'Skifer', 'Gneis', 'Basalt', 'Skifer', 'Granitt', 'Marmor'],
    'Strøk': [45, 60, 30, 85, 90, 120, 150, 210, 270, 315],
    'Fall': [30, 20, 40, 15, 35, 25, 30, 20, 10, 45]
}

# Oppretter en pandas DataFrame
df = pd.DataFrame(data)
df
```

```python
# Vis de første 5 radene i DataFrame
første_fem = df.head()
første_fem
```

#### **c. Nyttige pandas funksjoner for geologiske data:**

**Eksempler:**

```python
# Beregn gjennomsnittlig strøk for en bestemt bergartstype
gjennomsnitt_strøk_granitt = df[df['Bergartstype'] == 'Granitt']['Strøk'].mean()
gjennomsnitt_strøk_granitt
# Beregn gjennomsnittlig fall for en bestemt bergartstype
gjennomsnitt_fall_granitt = df[df['Bergartstype'] == 'Granitt']['Fall'].mean()
gjennomsnitt_fall_granitt

# Finn maksimum og minimum fall-verdier for en bestemt bergartstype
max_fall_skifer = df[df['Bergartstype'] == 'Skifer']['Fall'].max()
max_fall_skifer
min_fall_skifer = df[df['Bergartstype'] == 'Skifer']['Fall'].min()
min_fall_skifer

# Grupper data basert på bergartstypen hvor fall er maks for hver type
gruppert_fall = df.groupby('Bergartstype')['Fall'].max()
gruppert_fall
# Luk ut bergarter med fall over 35 grader
gruppert_fall_hoy = gruppert_fall[gruppert_fall > 35]
gruppert_fall_hoy
```

#### d. Lese/skrive geologiske data:

```python
# d. Lese/skrive geologiske data:
from pathlib import Path

# Bygger filbanen
fil_bane = Path('../data/05_bergarter.csv')
# Les filen inn i en DataFrame, kan spesifisere encoding og delimiter
df = pd.read_csv(fil_bane)
df

fil_bane = Path('../data/07_strøk_fall.xlsx')
#lese excel dok med pandas, avhengig av biblioteket openpyxl (pip install openpyxl)
data = pd.read_excel(fil_bane, sheet_name='Ark1', engine='openpyxl')
data

#skrive ut data til CSV og Excel
# lage filendinger
csv = 'csv'
xlsx = 'xlsx'

#Legger til en rad
ny_rad = pd.DataFrame({'strøk': [88], 'fall': [50]})

#slår sammen den gamle dataframen med den nye og lagrer den i variablen 'df'
df = pd.concat([ny_rad, data]).reset_index(drop=True)

#index=False trengs for å ikke skrive ut indeksene i dataframen
fil_bane = Path(f'../output/05_analyse_resultat.{csv}')
df.to_csv(fil_bane, index=False)
fil_bane = Path(f'../output/05_analyse_resultat.{xlsx}')
df.to_excel(fil_bane, index=False, engine='openpyxl')
```

Hvis du vil skrive til et bestemt ark eller til flere ark i en Excel-fil, kan du gjøre det med sheet_name-parameteren og ExcelWriter-objektet:

```python
fil_bane = Path(f'../output/05_analyse_resultat_flere_ark.{xlsx}')
with pd.ExcelWriter(fil_bane, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    data.to_excel(writer, sheet_name='Sheet2', index=False)
```

---

## 6\. **Visualisering med matplotlib (20 minutter):**

`matplotlib` er et kraftig bibliotek i Python for å lage statiske, animerte og interaktive visualiseringer. For geologer gir det en flott måte å visualisere geologiske data, som strøk/fall-målinger, for å forstå og kommunisere resultater.

#### a. **Hva er matplotlib?**

`matplotlib` er et 2D-plottingbibliotek som kan produsere figurer av høy kvalitet i forskjellige formater. Det gir en objektorientert API for å bygge inn plott i applikasjoner ved bruk av generelle GUI-verktøy som Tkinter, wxPython, Qt eller GTK.

`plot()`\-funksjonen i matplotlib er svært fleksibel og kan ta en rekke argumenter for å tilpasse plottet ditt. Her er en detaljert oversikt over noen av de vanligste argumentene:

### Grunnleggende argumenter:

1. **x, y**: Array-lignende eller skalarlignende. Dette er de grunnleggende datasettene som skal plottes. `x` er dataene for x-aksen, og `y` er dataene for y-aksen.
2. **fmt** (format string, valgfritt): En snarvei for å spesifisere markører, linjestil og farge. For eksempel, `'ro-'` betyr røde sirkelmarkører med solid linje.

### Farge og linjestil:

1. **color** (eller `c`): Sett fargen på linjen. Kan være en streng som `'green'` eller forkortelser som `'g'`.
2. **linestyle** (eller `ls`): Bestemmer stilen på linjen, som `'-'` for solid, `'--'` for stiplet, `'-.'` for dash-dot, `':'` for prikket.
3. **linewidth** (eller `lw`): Tykkelsen på linjen.

### Markører:

1. **marker**: Stil av markøren, for eksempel `'o'` for sirkler, `'s'` for kvadrater, `'*'` for stjerner.
2. **markersize** (eller `ms`): Størrelsen på markørene.
3. **markeredgecolor** (eller `mec`): Fargen på kanten av markørene.
4. **markeredgewidth** (eller `mew`): Bredde på kanten av markørene.
5. **markerfacecolor** (eller `mfc`): Fyllfargen til markørene.

### Ekstra:

1. **alpha**: Gjennomsiktighet av plottlinjen og markørene. Verdi mellom 0 (helt gjennomsiktig) og 1 (helt opak).
2. **label**: Etiketten som skal brukes for dette datasettet i en eventuell legend.

#### a. Plotte grunnvannsnivå over tid:

```python
import matplotlib.pyplot as plt
# a. Plotte grunnvannsnivå over tid:
tid = ["Januar", "Februar", "Mars", 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Desember']
grunnvannsnivå = [4.3, 4.9, 4.5, 4.7, 5.2, 6.5, 6.0, 5.5, 5.3, 5.0, 4.5, 4.0]
cm = 1 / 2.54
plt.figure(figsize=(21*cm, 29.7*0.5*cm))  # A4 bred, høy (med mål i tommer, derfor multipliseres med cm)
plt.plot(tid, grunnvannsnivå, marker='o')
plt.xlabel('Måneder')
plt.xticks(rotation=45)  # Roterer etikettene for å forhindre overlapping
plt.ylabel('Grunnvannsnivå (m)')
plt.title('Grunnvannsnivå over tid')
# funksjon som automatisk justerer subplot-parametere for å gi angitt padding rundt plotene inne i en figur.
plt.tight_layout()
plt.show()
```

#### b. Histogram av bergartsklassifikasjoner:

```python
# b. Histogram av bergartsklassifikasjoner:
bergarter = ['Granitt', 'Skifer', 'Kalkstein', 'Skifer', 'Granitt', 'Granitt']
plt.hist(bergarter)
plt.title('Fordeling av bergarter i prøver')
plt.xlabel('Bergartstype')
plt.ylabel('Antall prøver')
plt.show()
```

#### **c. Grunnleggende plotting med strøk/fall-målinger:**

```python
# c. Grunnleggende plotting med strøk/fall-målinger:
# lage scatterplott
import pandas as pd
from pathlib import Path
fil_bane = Path('../data/05_bergarter.csv')
#lese excel dok med pandas, avhengig av biblioteket openpyxl (pip install openpyxl)
data = pd.read_csv(fil_bane)

# Anta at vi har en DataFrame df med strøk, fall og bergartstype
plt.scatter(data['Strøk'], data['Fall'], c='blue', label='Målinger')
plt.xlabel('Strøk')
plt.ylabel('Fall')
plt.title('Strøk vs Fall Målinger')
plt.legend()
plt.show()
```

```python
# lage rosediagram
import numpy as np

# Angi størrelsen på hver bin i grader
bin_størrelse = 10  # For eksempel, hver bin dekker 10 grader. Du kan justere dette for forskjellig oppløsning
antal_bins = int(360 / bin_størrelse)
# Sette opp bins for histogrammet
bins = np.linspace(0, 2 * np.pi, antal_bins + 1)

# Konvertere grader til radianer for plotting
data['radianer'] = np.deg2rad(data['Strøk'])

# Plotte rosediagrammet
ax = plt.subplot(111, polar=True)  # tallet 111 i subplot-funksjonen er en tre-sifret heltall hvor den første sifferen representerer antall rader, den andre sifferen representerer antall kolonner, og den tredje sifferen representerer indeksen til det nåværende subplotet.
ax.set_theta_direction(-1)  # Roter med klokken
ax.set_theta_zero_location('N')  # 0 grader på toppen (Nord)

# Telle og plotte data
telling, _ = np.histogram(data['radianer'], bins=bins)
ax.bar(bins[:antal_bins], telling, width=bins[1]-bins[0], align='edge', edgecolor='black')

# Tilpasse plot
ax.set_title("Geologisk rosediagram av strøkmålinger")
plt.show()
```

#### d. **Visualisere data basert på bergartstypen:**

Vi kan fargelegge punktene i scatter-plottet basert på bergartstypen for å få bedre innsikt i hvordan forskjellige bergarter fordeler seg i forhold til strøk og fall.

**Eksempler:**

```python
# d. Visualisere data basert på bergartstypen:
farger = {
    'Granitt': 'red',
    'Skifer': 'blue',
    'Sandstein': 'green',
    'Kalkstein': 'yellow',
    'Gneis': 'purple',
    'Basalt': 'black',
    'Marmor': 'orange'
}

plt.scatter(df['Strøk'], df['Fall'], c=df['Bergartstype'].map(farger), label='Målinger')
plt.xlabel('Strøk')
plt.ylabel('Fall')
plt.title('Strøk vs Fall Målinger basert på Bergartstype')
plt.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=farger[key], markersize=10) for key in farger], labels=farger.keys())
plt.show()
```

#### e. **Tilpasse plottet:**

Med `matplotlib` kan vi enkelt justere utseendet på plottet, legge til rutenett, endre aksebegrensninger og mye mer.

**Eksempler:**

```python
# e. Tilpasse plottet:
plt.scatter(data['Strøk'], data['Fall'], c=data['Bergartstype'].map(farger), label='Målinger')
plt.xlabel('Strøk')
plt.ylabel('Fall')
plt.title('Strøk vs Fall Målinger basert på Bergartstype')
plt.grid(True)
plt.xlim([0, 360])
plt.ylim([0, 90])
plt.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=farger[key], markersize=10) for key in farger], labels=farger.keys())
plt.show()
```

### 

---

## 7\. **Praktisk øvelse (30 minutter):**

- Deltakerne gis et datasett i en CSV-fil.
- Bruke `pandas` for å lese dataen, `numpy` for enkel behandling og `matplotlib` for visualisering.
- Målet kan være å analysere jordsmonnsammensetningen på forskjellige dybder, identifisere hvor ofte forskjellige bergarter forekommer, eller plotte grunnvannsnivået over tid.

---

## 8\. **Oppsummering og spørsmål (10 minutter):**

#### a. Gjennomgang av det som er lært.

I løpet av dette kurset har vi dykket ned i Python-programmering med et spesielt fokus på geologiske data. La oss ta et øyeblikk for å reflektere over hva vi har lært:

1. **Introduksjon til Python:** Vi startet med grunnleggende konsepter i Python, inkludert variabler, datatyper, og kontrollstrukturer.
2. **Filhåndtering:** Vi lærte hvordan vi kan lese fra og skrive til filer, noe som er kritisk for dataanalyse. Ved hjelp av `open()` lærte vi også viktigheten av kontekthåndtering med `with`.
3. **Dataanalyse med numpy og pandas:** Vi utforsket kraftige biblioteker som `numpy` og `pandas` for å behandle og analysere geologiske data. Fra grunnleggende array-operasjoner i `numpy` til datahåndtering med DataFrames i `pandas`, fikk vi en solid forståelse av verktøyene som er tilgjengelige for geologisk databehandling.
4. **Visualisering med matplotlib:** Visualisering er en nøkkelkomponent i dataanalyse. Vi lærte hvordan vi kan lage informative og estetisk tiltalende visualiseringer av geologiske data ved hjelp av `matplotlib`.
5. **Geologisk kontekst:** Gjennom kurset integrerte vi eksempler og data som er spesielt relevante for geologi, som strøk/fall-målinger og bergartsklassifikasjoner. Dette sikret at læringen var direkte anvendbar for geoteknikkere og geologer.

#### b. Åpen diskusjon og Q&A-sesjon.

**Til slutt,** vi håper at du føler deg mer komfortabel med Python som et verktøy for geologisk og geoteknisk dataanalyse. Med de ferdighetene du har lært i dag, er du godt rustet til å utforske, analysere og visualisere geologiske datasett på egen hånd. Vi oppfordrer deg til å fortsette å eksperimentere, utforske ytterligere ressurser, og dykke dypere inn i de kraftige verktøyene og bibliotekene vi har dekket. God koding!

---

Merk: Dette blir en rask innføring i disse bibliotekene gitt tidsbegrensningene. Avhengig av din erfaring kan noen deler føles litt raskt, men målet er å gi en oversikt og vekke interesse for videre læring.