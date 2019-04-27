# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

fn='D:\TCRI\data/20171107_TALIM.txt'
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


# Define the date format
myFmt = DateFormatter("%m/%d") 

# plot the data
fig, ax = plt.subplots()
ax.plot(tt, int_cp, color='purple')
ax.set(xlabel="Date", ylabel="Center Pressure [hPa]")
ax.set(title="Time series \n TALIM (2017)")
plt.set_ylim=[930,1010]
plt.gca().invert_yaxis() #reverse y-axis

#tell matplotlib to use the format specified above
ax.xaxis.set_major_formatter(myFmt); 

plt.savefig('D:\TCRI\plt/cp_'+fn[13:]+'.png', dpi=300)