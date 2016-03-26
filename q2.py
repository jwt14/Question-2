import subprocess

N_x = 10
data = subprocess.Popen('./q2 1 ' + str(N_x) + ' 1 10000 1', stdout=subprocess.PIPE).communicate()[0]
