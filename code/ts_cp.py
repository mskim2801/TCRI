# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

fn='../data/20171107_TALIM.txt'
f=open(fn, "r")
lines=f.readlines()
toa=[] #time of analysis
grade=[] #grade #1:TD, 2:TS
lat=[]
lon=[]
cp=[] #center pressure
msws=[] #maximum sustained wind speed #unit: knots
tt=[] 

for line in lines:
    toa.append(line[0:8])
    grade.append(line[13])
    lat.append(line[15:18])
    lon.append(line[20:23])
    cp.append(line[24:28])
    msws.append(line[33:36])
    tt.append(datetime.datetime.strptime(line[0:8], "%y%m%d%H"))
    
int_cp = list(map(int, cp))
int_msws = list(map(int, msws))

# Define the date format
myFmt = DateFormatter("%m/%d") 

# plot the data
fig, (ax1, ax2) = plt.subplots(2,1)
# plot cp
ax1.plot(tt, int_cp, color='purple')
ax1.set(xlabel="Date", ylabel="Center Pressure [hPa]")
ax1.set(title="Time series \n TALIM (2017)")
plt.set_ylim=[930,1010]
plt.gca().invert_yaxis() #reverse y-axis
#tell matplotlib to use the format specified above
ax1.xaxis.set_major_formatter(myFmt); 

# plot msws
ax2.plot(tt, int_msws, color='red')
ax2.set(xlabel="Date", ylabel="Maximum Sustained \n Wind Speed [m/s]")
ax2.set(title="Time Series \n TALIM(2007)")
plt.gca().invert_yaxis() #reverse y-axis
ax2.xaxis.set_major_formatter(myFmt);


plt.tight_layout()
plt.savefig('./../plt/'+fn[8:]+'.png', dpi=300)
