#   HPC Q2 
#   Created by Jan Witold Tomaszewski CID: 00833865

import subprocess
import numpy as np

#Any of these parameters can be changed by user
L = 1
N_x = 10
T = 1
N_t = 10000
d_t = T/float(N_t)                              #Be careful! Integers could yield 0
d_x = L/float(N_x)
alpha = 1
heat_mid = np.array(0.5*L*(1-0.5*L))                       #Operatre on Numpy arrays for maximum efficiency
time = np.linspace(0, 1, N_t+1)


data = subprocess.Popen("./q2 {} {} {} {} {}".format(L, N_x, T, N_t, alpha),
                        stdout=subprocess.PIPE).communicate()[0]

a=data.split('\n')

for i in range(1, N_t+1):
    b = eval(a[int((0.5*N_x+1)*(2*i-1))])
    heat_mid = np.append(heat_mid, b)
