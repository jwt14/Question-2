#   HPC Q2 
#   Created by Jan Witold Tomaszewski CID: 00833865

import subprocess
import numpy as np
import matplotlib.pyplot as plt
from math import pi,sin,exp
#Any of these parameters can be changed by user

L = 1
N_x = 10
T = 1
N_t = 10000
d_t = T/float(N_t)                              #Be careful! Integers could yield 0
d_x = L/float(N_x)
theta = 0
alpha = 1
heat_mid = np.array(sin(pi*0.5*L))               #Operatre on Numpy arrays for maximum efficiency
heat_analytic = np.array(sin(pi*0.5*L))               #Operatre on Numpy arrays for maximum efficiency
time = np.linspace(0, 1, N_t+1)


data = subprocess.Popen("./q2 {} {} {} {} {} {}".format(L, N_x, T, N_t, alpha, theta),
                        stdout=subprocess.PIPE).communicate()[0]

a=data.split('\n')

for i in range(1, N_t+1):
    b = eval(a[int((0.5*N_x+1)*(2*i-1))])
    heat_mid = np.append(heat_mid, b)

for j in range(1, N_t+1):
    c = sin(pi*0.5*L)*exp(-alpha*pi**2*j*d_t/L/L)
    heat_analytic = np.append(heat_analytic, c)


fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))
axes[0].plot(time, heat_mid, 'r')
axes[0].set_xlabel('Time (s)')
axes[0].set_ylabel('Temperature at the midpoint (K)')
axes[0].set_title("Standard plot")

axes[1].semilogy(time, heat_mid, 'b')
axes[1].set_xlabel('Time (s)')
axes[1].set_ylabel('Temperature at the midpoint (K)')
axes[1].set_title("Semi-logarithmic plot")

fig.tight_layout() 
#axes.set_title("Forward Euler solution for x(1-x) conditions")
fig.savefig("Comparison.png")