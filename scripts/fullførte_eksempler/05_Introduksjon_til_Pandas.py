# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 11:16:30 2023

@author: dpe
"""
import pandas as pd
from pathlib import Path
#----------------------------------------------------------------------------#

# b. Grunnleggende DataFrame med geologiske data:
# Definerer dataen
data = {
    'Bergartstype': ['Granitt', 'Skifer', 'Sandstein', 'Kalkstein', 'Skifer', 'Gneis', 'Basalt', 'Skifer', 'Granitt', 'Marmor'],
    'Strøk': [45, 60, 30, 85, 90, 120, 150, 210, 270, 315],
    'Fall': [30, 20, 40, 15, 35, 25, 30, 20, 10, 45]
}

# Oppretter en pandas DataFrame
df = pd.DataFrame(data)
print(df)
#----------------------------------------------------------------------------#

# Vis de første 5 radene i DataFrame
første_fem = df.head()
print(første_fem)

#----------------------------------------------------------------------------#

# Beregn gjennomsnittlig strøk for en bestemt bergartstype
gjennomsnitt_strøk_granitt = df[df['Bergartstype'] == 'Granitt']['Strøk'].mean()
print("Gj.strøk: ", gjennomsnitt_strøk_granitt)
# Beregn gjennomsnittlig fall for en bestemt bergartstype
gjennomsnitt_fall_granitt = df[df['Bergartstype'] == 'Granitt']['Fall'].mean()
print("Gj.fall granitt: ", gjennomsnitt_fall_granitt)

# Finn maksimum og minimum fall-verdier for en bestemt bergartstype
max_fall_skifer = df[df['Bergartstype'] == 'Skifer']['Fall'].max()
print("Største fall skifer: ", max_fall_skifer)
min_fall_skifer = df[df['Bergartstype'] == 'Skifer']['Fall'].min()
print("Minste fall skifer: ", min_fall_skifer)

# Grupper data basert på bergartstypen hvor fall er maks for hver type
gruppert_fall = df.groupby('Bergartstype')['Fall'].max()
print("Maks gruppert fall: \n", gruppert_fall)
# Luk ut bergarter med fall over 35 grader
gruppert_fall_hoy = gruppert_fall[gruppert_fall > 35]
print("Fall over 35 grader: \n", gruppert_fall_hoy)

#----------------------------------------------------------------------------#

# d. Lese/skrive geologiske data:

# Bygger filbanen
fil_bane = Path('../../data/05_bergarter.csv')
# Les filen inn i en DataFrame, kan spesifisere encoding og delimiter
df = pd.read_csv(fil_bane)
df

fil_bane = Path('../../data/07_strøk_fall.xlsx')
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
fil_bane = Path(f'../../output/05_analyse_resultat.{csv}')
df.to_csv(fil_bane, index=False)
fil_bane = Path(f'../../output/05_analyse_resultat.{xlsx}')
df.to_excel(fil_bane, index=False, engine='openpyxl')

#----------------------------------------------------------------------------#

fil_bane = Path(f'../../output/05_analyse_resultat_flere_ark.{xlsx}')
with pd.ExcelWriter(fil_bane, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    data.to_excel(writer, sheet_name='Sheet2', index=False)