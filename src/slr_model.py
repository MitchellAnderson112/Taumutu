# Imports
import random as ran
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# set up x-axis of years 2020 to 2120
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
    
    plt.plot(years, slr1)#, color='green')
    plt.plot(years, slr2)#, color='yellow')
    plt.plot(years, slr3)#, color='red')
plt.text(2100,1.5, 'WCS')
plt.text(2100,0.95, 'LCS')
plt.text(2100,0.55, 'BCS')
plt.text(2090, 0, 'Iterations: {}'.format(iterations))
plt.plot(2020,0, label = 'BCS: Best Case Scenario')
plt.plot(2020,0, label = 'LCS: Likely Case Scenario') 
plt.plot(2020,0, label = 'WCS: Worst Case Scenario') 
plt.ylabel('Sea Level Rise (m)')
plt.xlabel('Year')
plt.legend(loc='best')
plt.grid()
plt.title('Sea Level Rise Predictions with Monte-Carlo Analysis')
plt.show()

# df1 = pd.DataFrame(res1)
# df2 = pd.DataFrame(res2)
# df3 = pd.DataFrame(res3)
# for i in np.arange(0,100):
#     plt.plot(years, df1[str(int(i))].mean())
