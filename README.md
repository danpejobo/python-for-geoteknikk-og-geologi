# Introduksjonskurs i Python-programmering: Oppsettsinstruksjoner

Velkommen til kurset i Geologisk Python-programmering! Før vi starter kurset, er det viktig at vi setter opp vårt programmeringsmiljø. Nedenfor er en oversikt over kursmatriellet og instruksjoner for å få alt på plass.

- [Introduksjonskurs i Python-programmering: Oppsettsinstruksjoner](#introduksjonskurs-i-python-programmering-oppsettsinstruksjoner)
  - [0. Git-repositorium](#0-git-repositorium)
    - [Forklaring:](#forklaring)
  - [1. Installer Anaconda](#1-installer-anaconda)
  - [2. Opprett et virtual environment for kurset](#2-opprett-et-virtual-environment-for-kurset)
  - [3. Installer Spyder, Jupyter Notebook og PowerShell Prompt](#3-installer-spyder-jupyter-notebook-og-powershell-prompt)
  - [4. Legg til "conda-forge" pakke samling](#4-legg-til-conda-forge-pakke-samling)
  - [5. Installer nødvendige pakker for kurset](#5-installer-nødvendige-pakker-for-kurset)
- [Ferdig!](#ferdig)

## 0\. Git-repositorium

Kursmateriellet er satt opp i et git-repositorium som vi laster ned før vi starter kurset. Link blir postet i Q&A chatten for møtet! Mappestrukturen er vist under, og det er gitt en forklarende tekst.

```
python-for-geoteknikk-og-geologi/
│
├── Python-kurs-transcript.md
├── fremvisning-Introduksjonskurs-i-Python.pdf
├── fremvisning-Introduksjonskurs-i-Python.pptx
├── LICENSE
├── README.md
├── requirements.txt
│
├── notebooks/
│   ├── 01_Introduksjon_til_Python.ipynb
│   ├── 02_Grunnleggende_om_Python.ipynb
│   ├── 03_Filhåndtering.ipynb
│   ├── 04_Introduksjon_til_Numpy.ipynb
│   ├── 05_Introduksjon_til_Pandas.ipynb
│   └── 06_Visualisering_med_Matplotlib.ipynb
│
├── data/
│   ├── 03_grunnvanns_data.csv
│   ├── 04_numpy_array.csv
│   ├── 05_bergarter.csv
│   ├── 07_AGD_8501.SND
│   └── 07_strøk_fall.xlsx
│
├── scripts/
│   ├── 07_geoteknikk.py
│   ├── 07_geologi.py
│   └── fullførte_eksempler/
│       ├── 01_Introduksjon_til_Python.ipynb
│       ├── 02_Grunnleggende_om_Python.ipynb
│       ├── 03_Filhåndtering.ipynb
│       ├── 04_Introduksjon_til_Numpy.ipynb
│       ├── 05_Introduksjon_til_Pandas.ipynb
│       └── 06_Visualisering_med_Matplotlib.ipynb
│
├── src/
```

### Forklaring:

- README: 
  - En innledende fil som gir en oversikt over kurset, instruksjoner for hvordan man setter opp miljøet (f.eks. installasjon av Anaconda), og hvordan man navigerer i repositoriet.
- requirements.txt: 
  - En liste over alle Python-pakkene som er nødvendige for kurset. Deltakere kan installere alle nødvendige pakker ved å kjøre pip install -r requirements.txt.
- **notebooks/**: 
  - Inneholder Jupyter Notebooks, som er interaktive dokumenter der du kan kombinere kode, tekst, og visualiseringer. Disse filene kan brukes som en interaktiv del av kursundervisningen.
- **data/**: 
  - Datasett som brukes gjennom kurset, som for eksempel CSV-filer med geologiske data.
- **scripts/**: 
  - Python-skript som demonstrerer spesifikke teknikker eller mer komplekse eksempler som kan kjøres separat fra notebooks (i en vanlig IDE).
  - **fullførte_eksempler/**: 
      - Fullførte python-eksempler som inneholder alle eksemplene fra notebooks-mappen. I tillegg ligger eksemplene som vanlige python-filer, som kan åpnes i en IDE.
- **src/**: 
  - python source kode vi skrive på kurset i en IDE  plasseres her

## 1\. Installer Anaconda

Anaconda er en populær distribusjon av Python og R for vitenskapelig databehandling og maskinlæring. Det vil gjøre det enkelt for oss å installere og administrere alle de nødvendige verktøyene og bibliotekene for dette kurset.

- Last ned Anaconda fra den offisielle nettsiden, og følg installasjonsinstruksjonene for ditt operativsystem.
- Følg stegene "Installer", "Starte" og les "Virtual environements (venv)" i [GeoWiki@Anaconda](https://app.nuclino.com/)

## 2\. Opprett et virtual environment for kurset

For å sikre at alle har et konsistent arbeidsmiljø, er det viktig å opprette et eget virtuelt miljø for kurset. Et virtuelt miljø er en isolert kopi av Python, som lar oss holde avhengighetene for ulike prosjekter adskilt. Vi vil kalle vårt miljø "pykurs".

I Anaconda Navigator:

- Gå til fanen "Environments".
- Velg "Create" og navngi "pykurs".
- Packages velg python 3.11.x
- Trykk "Create"

## 3\. Installer Spyder, Jupyter Notebook og PowerShell Prompt

Spyder er en kraftig IDE (Integrated Development Environment) for Python, mens Jupyter Notebook lar deg lage interaktive notatbøker med kode, tekst og visualiseringer. PowerShell Prompt gir oss en kraftig kommandolinje for å håndtere Python-pakker og miljøer.

Åpne Anaconda Navigator (som ble installert i trinn 1) og installer følgende applikasjoner:

- Spyder
- Jupyter Notebook
- PowerShell Prompt

## 4\. Legg til "conda-forge" pakke samling

conda-forge er en samling av Python-pakker.

Åpne PowerShell Prompt (fra Anaconda Navigator eller systemets startmeny):

1. Legg til conda-forge til dine kanaler:

```
conda config --add channels conda-forge
conda config --set channel_priority strict
```

1. Oppdater conda for å sikre at du har den nyeste versjonen:

```
conda update conda
```

## 5\. Installer nødvendige pakker for kurset

Åpne requirements.txt for å se hvilke pakker dette kurset er avhengige av. Disse må installeres og utføres enklest i powershell (kan installeres 1-og-1 også ved pip install "pakkenavn"). Spyder-terminal gir oss en terminal inne i Spyder IDE, noe som er svært nyttig for å kjøre kommandoer raskt mens du koder. Resten er pakker vi trenger på kurset.

1. Fortsett i PowerShell Prompt som du åpnet i forrige steg:

```
pip install -r requirements.txt
```

# Ferdig!

Nå bør du være klar for kurset! Du har satt opp alle de nødvendige verktøyene og bibliotekene for å dykke inn i verden av Python-programmering.