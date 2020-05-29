
# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random as ran
import gif

church = pd.read_csv(r'C:\Users\man112\401\401_copy\church_profile.csv')
marae = pd.read_csv(r'C:\Users\man112\401\401_copy\marae_profile.csv')
bank = pd.read_csv(r'C:\Users\man112\401\401_copy\bank_profile.csv')


years = np.arange(2020,2120,1)
res1, res2, res3 = [], [], []
# for loops to randomise the rate of SLR
iterations = 100
for n in np.arange(0,iterations):
    # init empty lists to be filled
    slr1, slr2, slr3 = [], [], []
    # set randomised SLR rate
    g1, g2, g3 = 3/700, 1/140, 33/2800
    gl1 = [g1*ran.randint(50,60)/100, g1*ran.randint(60,70)/100,g1*ran.randint(70,80)/100,g1*ran.randint(80,90)/100,g1*ran.randint(90,100)/100, g1*ran.randint(100,110)/100, g1*ran.randint(110,120)/100,g1*ran.randint(120,130)/100,g1*ran.randint(130,140)/100,g1*ran.randint(140,150)/100]
    gl2 = [g2*ran.randint(50,60)/100, g2*ran.randint(60,70)/100,g2*ran.randint(70,80)/100,g2*ran.randint(80,90)/100,g2*ran.randint(90,100)/100, g2*ran.randint(100,110)/100, g2*ran.randint(110,120)/100,g2*ran.randint(120,130)/100,g2*ran.randint(130,140)/100,g2*ran.randint(140,150)/100]
    gl3 = [g3*ran.randint(50,60)/100, g3*ran.randint(60,70)/100,g3*ran.randint(70,80)/100,g3*ran.randint(80,90)/100,g3*ran.randint(90,100)/100, g3*ran.randint(100,110)/100, g3*ran.randint(110,120)/100,g3*ran.randint(120,130)/100,g3*ran.randint(130,140)/100,g3*ran.randint(140,150)/100]
    # 2020-2030
    for i in np.arange(0,10):
        slr1.append(i*gl1[0])
        slr2.append(i*gl2[0])
        slr3.append(i*gl3[0])

    # 2030-2040
    for i in np.arange(11,21):
        slr1.append(i*gl1[1])
        slr2.append(i*gl2[1])
        slr3.append(i*gl3[1])

    # 2040-2050
    for i in np.arange(21,31):
        slr1.append(i*gl1[2])
        slr2.append(i*gl2[2])
        slr3.append(i*gl3[2])

    # 2050-2060
    for i in np.arange(31,41):
        slr1.append(i*gl1[3])
        slr2.append(i*gl2[3])
        slr3.append(i*gl3[3])

    # 2060-2070
    for i in np.arange(41,51):
        slr1.append(i*gl1[4])
        slr2.append(i*gl2[4])
        slr3.append(i*gl3[4])

    # 2070-2080
    for i in np.arange(51,61):
        slr1.append(i*gl1[5])
        slr2.append(i*gl2[5])
        slr3.append(i*gl3[5])

    # 2080-2090
    for i in np.arange(61,71):
        slr1.append(i*gl1[6])
        slr2.append(i*gl2[6])
        slr3.append(i*gl3[6])

    # 2090-2100
    for i in np.arange(71,81):
        slr1.append(i*gl1[7])
        slr2.append(i*gl2[7])
        slr3.append(i*gl3[7])

    # 2100-2110
    for i in np.arange(81,91):
        slr1.append(i*gl1[8])
        slr2.append(i*gl2[8])
        slr3.append(i*gl3[8])

    # 2110-2120
    for i in np.arange(91,101):
        slr1.append(i*gl1[9])
        slr2.append(i*gl2[9])
        slr3.append(i*gl3[9])


    res1.append(slr1), res2.append(slr2), res3.append(slr3)

high_tide = 1.15 #meters above MSL, found using NIWA Tides
tide_x = np.arange(-10, 3000)
now = len(tide_x)*[high_tide]
tide_data_1 = len(tide_x)*[high_tide+0.6]
tide_data_2 = len(tide_x)*[high_tide+1.05]
tide_data_3 = len(tide_x)*[high_tide+1.75]
#storm_surge = len(tide_x)*[high_tide+0.8+1.6] #storm surge rarely exceeds 0.6m in coastal NZ


# init list to be plotted
frames = []
# plotting function
@gif.frame
def plot(i, year):
    plt.plot(marae.dist, marae.dem, color='black', label='Ground Profile')
    plt.plot(tide_x, len(tide_x)*[high_tide + res1[0][i]], color='green', label='Best Case Scenario', linestyle='dashed')
    plt.plot(tide_x, len(tide_x)*[high_tide + res2[0][i]], color='orange', label='Likely Case Scenario', linestyle='dashed')
    plt.plot(tide_x, len(tide_x)*[high_tide + res3[0][i]], color='red', label='Worst Case Scenario', linestyle='dashed')
    plt.plot(tide_x, now, color='blue', label='Present Sea Level (High Tide)')
    plt.text(5,3.6, 'X')
    plt.legend(loc='best')
    plt.text(400, 5.5, 'Year: {}'.format(year))
    plt.xlim(0, 725)
    plt.ylim(0.8,6.25)
    plt.xlabel('Horizontal Distance (m)')
    plt.ylabel('Elevation above sea level (m)')
    plt.title('Ngati Moki Marae Elevation Profile')



for i in np.arange(0,len(years)):
    year = years[i]
    frame = plot(i, year)
    frames.append(frame)
gif.save(frames, 'MARAE_SLR.gif')
