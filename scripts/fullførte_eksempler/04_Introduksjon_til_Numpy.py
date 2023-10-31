# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 11:07:20 2023

@author: dpe
"""
import numpy as np
from pathlib import Path
#----------------------------------------------------------------------------#

# b. Grunnleggende numpy-array:

fil_bane = Path('../../data/04_numpy_array.csv')
# Leser inn data fra en CSV-fil
# 'delimiter' angir at hver verdi er separert med et semikolon
# 'dtype=int' angir at vi ønsker å konvertere disse verdiene til heltall, 
# kan også være "float" eller "str"

målinger = np.genfromtxt(fil_bane, delimiter=';',
                         dtype=int, skip_header=1)
print(målinger)

#----------------------------------------------------------------------------#

# c. Operasjoner med geologiske numpy arrays: 
# Beregn gjennomsnittlig strøk og fall 
gjennomsnitt_strøk = np.mean(målinger[:, 0]) 
print("Gj.strøk: ", gjennomsnitt_strøk) 
gjennomsnitt_fall = np.mean(målinger[:, 1]) 
print("Gj.fall: ", gjennomsnitt_fall)

#----------------------------------------------------------------------------#

# d. Nyttige numpy funksjoner for geologiske data:
# Finn maksimum og minimum fall-verdier
max_fall = np.max(målinger[:, 1])
print("Maks fall: ", max_fall)
min_fall = np.min(målinger[:, 1])
print("Min fall: ", min_fall)

# Beregn standardavvik for strøk-verdier
std_dev_strøk = np.std(målinger[:, 0])
print("Std.avvik strøk: ", std_dev_strøk)

#----------------------------------------------------------------------------#

# e. Indeksering og skjæring av geologiske data:
# Hent første strøk/fall-måling
første_måling = målinger[0]
print("Første måling: ", første_måling)

# Hent alle strøk-verdier
alle_strøk = målinger[:, 0]
print("Alle strøk: ", alle_strøk)

# Hent strøk/fall-målinger med fall større enn 35 grader
høyt_fall = målinger[målinger[:, 1] > 35]
print("Høyt fall: ", høyt_fall)

#----------------------------------------------------------------------------#
