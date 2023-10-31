# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:21:50 2023
Update on Tue Oct 31 10:20:25 2023

@author: dpe
"""
import libgeosuitesnd
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

fil_bane = str(Path("../data/07_AGD_8501.SND"))

try:
    result = libgeosuitesnd.parse(fil_bane)
except Exception as e:
    result = str(e)

# Extracting the main and data parts from the result
main_info = result[0]['main'][0]
data = result[0]['data']

# 1. Displaying the Main Information Table
main_df = pd.DataFrame.from_dict(main_info, orient='index', columns=['Value'])

# 2. Displaying first and last few rows of the depth data
sample_data = pd.concat([data.head(), data.tail()])

# Plotting all the data insights together in one row with indicators plotted against depth
cm = 1/2.54  # centimeters in inches
kilo = 0.001 # get kilonewtons
fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(21*cm, 29.7*cm))
fig.suptitle('Totalsondering', fontsize=24)

# Depth vs Feed Thrust Force
axes[0].plot(data['feed_thrust_force']*kilo, data['depth'], label='Feed Thrust Force', color='blue')
axes[0].invert_yaxis()  # Invert y-axis for depth going downwards
axes[0].set_title('Feed Thrust vs Depth')
axes[0].set_ylabel('Depth [m]')
axes[0].set_xlabel('Feed Thrust Force [kN]')
axes[0].grid(True)

# Depth vs Pumping Rate
axes[1].plot(data['pumping_rate'], data['depth'], label='Pumping Rate', color='green')
axes[1].invert_yaxis()  # Invert y-axis for depth going downwards
axes[1].set_title('Pumping Rate vs Depth')
axes[1].set_xlabel('Pumping Rate [L/min]')
axes[1].grid(True)

# Interval vs Depth
axes[2].plot(data['interval'], data['depth'], color='purple')
axes[2].invert_yaxis()  # Invert y-axis for depth going downwards
axes[2].set_title('Interval vs Depth')
axes[2].set_xlabel('Interval')
axes[2].grid(True)

# Indicators vs Depth
# Removing specific columns from the list of indicators
columns_to_exclude = ['depth', 'torque', 'rotation', 'penetration_rate', 'feed_force', 'comments', 'feed_thrust_force', 'interval', 'pumping_rate']
indicators = [col for col in data.columns if col not in columns_to_exclude]
# Extracting only those indicators which have data
active_indicators = [indicator for indicator in indicators if data[indicator].sum() > 0]
colors = ['red', 'green', 'blue', 'orange']
for indicator, color in zip(active_indicators, colors):
    mask = data[indicator] == 1
    axes[3].scatter([indicator] * mask.sum(), data['depth'][mask], color=color, marker='|', s=300, label=indicator)
axes[3].invert_yaxis()  # Invert y-axis for depth going downwards
axes[3].set_title('Indicators vs Depth')
axes[3].set_xlabel('Indicators')
axes[3].set_xticks(active_indicators)
axes[3].set_xticklabels(active_indicators, rotation=45, fontsize=8)
axes[3].legend(loc='upper right')
axes[3].grid(True, axis='y')

plt.tight_layout()
plt.show()

main_df, sample_data