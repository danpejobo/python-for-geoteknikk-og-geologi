# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:21:50 2023
Update on Tue Oct 31 10:15:20 2023

@author: dpe
"""
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Loading the Excel file into a DataFrame
fil_bane = Path("../data/07_strøk_fall.xlsx")
geological_data = pd.read_excel(fil_bane)

# Displaying the first few rows of the data
geological_data.head()

# 1. Statistical description
statistical_desc = geological_data.describe()

#Setup figure
cm = 1/2.54  # centimeters in inches
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(21*cm, 29.7*cm))
fig.suptitle('Geologisk analyse', fontsize=24)

# 1. Rose diagram (polar plot)
ax = plt.subplot(3, 1, 1, projection='polar')
# Plotting the data with the adjustments
n, _, _ = ax.hist(np.radians(geological_data['strøk']), bins=36, alpha=0.75, color='blue', rwidth=0.9)
# Setting the direction of 0 degree to top (North)
ax.set_theta_zero_location('N')
# Setting the rotation direction as clockwise
ax.set_theta_direction(-1)
# Adjusting the radial ticks
ax.set_yticks(np.arange(1, int(n.max()) + 1))
ax.set_rlabel_position(15)  # Positioning the radial labels
ax.set_title('Rose Diagram of Strøk')

# 2. Scatter plot
ax2 = axes[1]
ax2.scatter(geological_data['strøk'], geological_data['fall'], alpha=0.6, color='green')
ax2.set_title('Scatter Plot of Strøk vs Fall')
ax2.set_xlabel('Strøk')
ax2.set_ylabel('Fall')
ax2.grid(True, linestyle='--', alpha=0.7)

# 3. Cumulative frequency graph
ax3 = axes[2]
geological_data.sort_values(by='strøk').reset_index(drop=True).plot(y='strøk', use_index=True, ax=ax3, grid=True, linestyle='-', drawstyle='steps-post', label='Strøk')
geological_data.sort_values(by='fall').reset_index(drop=True).plot(y='fall', use_index=True, ax=ax3, grid=True, linestyle='-', drawstyle='steps-post', label='Fall')
ax3.set_title('Cumulative Frequency Graph')
ax3.set_xlabel('Count')
ax3.set_ylabel('Value')
ax3.legend()

# Adjusting the layout
plt.tight_layout()
plt.show()