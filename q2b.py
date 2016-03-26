#   HPC Q2b 
#   Created by Jan Witold Tomaszewski CID: 00833865
        
import subprocess
import numpy as np
import matplotlib.pyplot as plt
from math import pi,sin,exp

L = 1                                                                           #Any of these parameters can be changed by user
N_x = 20
T = 1
N_t = 1000
d_t = T/float(N_t)                                                              #Be careful! Integers could yield 0
d_x = L/float(N_x)
theta = 0.5
alpha = 1
heat_mid = np.array(sin(pi*0.5/L))                                              #Operatre on Numpy arrays for maximum efficiency
heat_analytic = np.array(sin(pi*0.5/L))                 
time = np.linspace(0, 1, N_t+1)                                                 #Generating time array- horizontal graph axis

data = subprocess.Popen("./q2 {} {} {} {} {}".format(L, N_x, T, N_t, alpha),
                        stdout=subprocess.PIPE).communicate()[0]    
a=data.split('\n')                                                              #Loading data using subprocess routine

for i in range(1, N_t+1):
    b = eval(a[int((0.5*N_x+1)*(2*i-1))])
    heat_mid = np.append(heat_mid, b)                                           #Recording temperature at the middle during every iteration

for j in range(1, N_t+1):
    c = sin(pi*0.5/L)*exp(-alpha*pi**2*j*d_t/L/L)
    heat_analytic = np.append(heat_analytic, c)                                 #Calculating full analytic solution at the middle of a bar
    

#Plotting routines
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))
axes[0].plot(time, heat_mid, 'r', linestyle=':', label="numerical", linewidth=5.00)
axes[0].plot(time, heat_analytic, label="analytic")
axes[0].set_title("Result comparison")
axes[0].set_xlabel('Time (s)')
axes[0].set_ylabel('Temperature value (K)')
axes[0].legend()
d = heat_analytic - heat_mid                                                    #Determining absolute error- difference between simulation and theory
axes[1].plot(time, d, 'g', linewidth=2)
axes[1].set_title("Absolute error evolution")
axes[1].set_xlabel('Time (s)')

fig.tight_layout()
fig.savefig("Comparison.pdf")                                                   #Saving figure as an external pdf file for best quality
        
