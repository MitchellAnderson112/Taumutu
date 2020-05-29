# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random as ran
import gif

# import elevation data
church = pd.read_csv(r'/Users/mitchellanderson/Desktop/University/J_notebooks/401/church_profile.csv')
marae = pd.read_csv(r'/Users/mitchellanderson/Desktop/University/J_notebooks/401/marae_profile.csv')
bank = pd.read_csv(r'/Users/mitchellanderson/Desktop/University/J_notebooks/401/bank_profile.csv')

# PLOT STATIONARY SLR PROFILES

high_tide = 1.15 #meters above MSL, found using NIWA Tides
tide_x = np.arange(-10, 3000)
now = len(tide_x)*[high_tide]
tide_data_1 = len(tide_x)*[high_tide+0.6]
tide_data_2 = len(tide_x)*[high_tide+1.05]
tide_data_3 = len(tide_x)*[high_tide+1.75]
#storm_surge = len(tide_x)*[high_tide+0.8+1.6] #storm surge rarely exceeds 0.6m in coastal NZ


#plot church elevation
plt.plot(church.dist, church.dem, color='black', label='Ground Profile')
plt.plot(tide_x, tide_data_1, color='green', label='Best Case Scenario 2120', linestyle='dashed')
plt.plot(tide_x, tide_data_2, color='orange', label='Likely Case Scenario 2120', linestyle='dashed')
plt.plot(tide_x, tide_data_3, color='red', label='Worst Case Scenario 2120', linestyle='dashed')
plt.plot(tide_x, now, color='blue', label='Present Sea Level (High Tide)')
plt.legend(loc='best')
plt.text(30,3, 'X')
plt.ylim(0.8, 6.25)
plt.xlim(0, 600)
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Elevation above sea level (m)') # can we assume 0 is sea level?
plt.title('Hone Wetere Church Elevation Profile')
plt.show()

#plot marae elevation
plt.plot(marae.dist, marae.dem, color='black', label='Ground Profile')
plt.plot(tide_x, tide_data_1, color='green', label='Best Case Scenario 2120', linestyle='dashed')
plt.plot(tide_x, tide_data_2, color='orange', label='Likely Case Scenario 2120', linestyle='dashed')
plt.plot(tide_x, tide_data_3, color='red', label='Worst Case Scenario 2120', linestyle='dashed')
plt.plot(tide_x, now, color='blue', label='Present Sea Level (High Tide)')
plt.text(5,3.6, 'X')
plt.legend(loc='best')
plt.xlim(0, 725)
plt.ylim(0.8,6.25)
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Elevation above sea level (m)')
plt.title('Ngati Moki Marae Elevation Profile')
plt.show()

# #plot bank elevation
# plt.plot(bank.dist, bank.dem, color='black')
# plt.plot(tide_x, tide_data_1, color='blue', label='Present')
# plt.plot(tide_x, tide_data_2, color='orange', label='Best Case Scenario 2080', linestyle='dashed')
# plt.plot(tide_x, tide_data_3, color='red', label='IPCC RCP8.5 2080', linestyle='dashed')
# plt.plot(tide_x, storm_surge, color='yellow', label='RCP8.5 & Storm Surge 2080', linestyle='dashed')
# plt.legend(loc='best')
# plt.xlim(0, 2250)
# plt.xlabel('Horizontal Distance (m)')
# plt.ylabel('Elevation above sea level (m)')
# plt.title('Bank Elevation Profile')
# plt.show()
