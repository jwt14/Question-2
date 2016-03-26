#   HPC Q2 
#   Created by Jan Witold Tomaszewski CID: 00833865

import subprocess

#Any of these parameters can be changed by user
L = 1
N_x = 10
T = 1
N_t = 10000
alpha = 1


data = subprocess.Popen("./q2 {} {} {} {} {}".format(L, N_x, T, N_t, alpha),
                        stdout=subprocess.PIPE).communicate()[0]