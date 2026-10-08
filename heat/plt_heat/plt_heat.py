import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument("-N", "--number_particles", type=int)
filename = parser.parse_args().filename
N = parser.parse_args().number_particles
k = 3.166811563e-6 # [Eh/K]

data = np.loadtxt(filename)
c1 =data[:,0]	# Step
c3 =data[:,2]	# classic temperature
c4 =data[:,3]	# Energies
c5 =data[:,4]
c6 =data[:,5]
c7 =data[:,6]	# distribution temperature
c8 =data[:,7]	# K

c3s =signal.savgol_filter(c3,1000,3)
c7s =signal.savgol_filter(c7,1000,3)

K=c8
### Direct replacement ####
DoF3=K/(N*k*c3)
DoF7=K/(3*N*k*c7)
#### Using the derivates ####
#dc3 =np.diff(c3s)
#dc7 =np.diff(c7s)
#dK =np.diff(K)
#dDoF3=np.diff(K/(N*k*c3s))
#dDoF7=np.diff(K/(N*k*c7s))
#DoF3=(dK/dc3)/(N*k)-(dDoF3/dc3)*c3s[1:]
#DoF7=(dK/dc7)/(N*k)-(dDoF7/dc7)*c7s[1:]
####
DoF3s =signal.savgol_filter(DoF3,10000,3)
DoF7s =signal.savgol_filter(DoF7,10000,3)

fig, ax = plt.subplots(3, 3, figsize=(9,9))
fig.suptitle(filename)

ax[0,0].plot(c3, c5, linewidth=0.5)
ax[0,0].plot(c3s, c5, linewidth=2, color='red')
ax[0,0].set_title("Col 5 vs Col 3")
ax[0,0].set_ylim(c5[0],c5[-1])

ax[1,0].plot(c7, c5, linewidth=0.5)
ax[1,0].plot(c7s, c5, linewidth=2, color='red')
ax[1,0].set_title("Col 5 vs Col 7")
ax[1,0].set_ylim(c5[0],c5[-1])

ax[2,0].plot(c3, c7, linewidth=0.5)
ax[2,0].plot(c3s, c7s, linewidth=2, color='red')
ax[2,0].set_title("Col 7 vs Col 3")

#ax[0,1].plot(c3s[1:][dc3!=0], dc5[dc3!=0]/dc3[dc3!=0], linewidth=0.5)
#ax[0,1].set_title("d(Col 5)/d(Col 3) vs Col 3")
#ax[0,1].set_ylim(-10,10)

#ax[1,1].plot(c7s[1:][dc7!=0], dc5[dc7!=0]/dc7[dc7!=0], linewidth=0.5)
#ax[1,1].set_title("d(Col 5)/d(Col 7) vs Col 7")
#ax[1,1].set_ylim(-10,10)

#ax[0,1].plot(c3, DoF3, linewidth=0.5); 
ax[0,1].plot(c3, DoF3s, linewidth=1, color='red'); ax[0,1].set_title("DoF(3) vs Col3")
#ax[0,1].plot(c1, DoF3, linewidth=0.5); ax[0,1].plot(c1, DoF3s, linewidth=1, color='red'); ax[0,1].set_title("DoF(3) vs Col 1"); ax[0,1].set_xlim(c1[0],c1[-1])

#ax[1,1].plot(c7, DoF7, linewidth=0.5);
ax[1,1].plot(c7, DoF7s, linewidth=1, color='red'); ax[1,1].set_title("DoF(7) vs Col7")
#ax[1,1].plot(c1, DoF7, linewidth=0.5); ax[1,1].plot(c1, DoF7s, linewidth=1, color='red'); ax[1,1].set_title("DoF(7) vs Col 1"); ax[1,1].set_xlim(c1[0],c1[-1])

ax[2,1].plot(c1, c8, linewidth=0.5)
#ax[2,1].plot(c1, (c5-c4)/5, linewidth=0.5, label='c5-c4', color='red')
#ax[2,1].plot(c1, (c6-c4)/5, linewidth=0.5, label='c6-c4', color='blue')
#ax[2,1].legend()
ax[2,1].set_title("K [a.u.] (Col 8) vs Col 1")
ax[2,1].set_xlim(c1[0],c1[-1])

ax[0,2].plot(c1, c3, linewidth=0.5)
ax[0,2].plot(c1, c3s, linewidth=2, color='red')
ax[0,2].set_title("Col 3 vs Col 1")
ax[0,2].set_xlim(c1[0],c1[-1])

ax[1,2].plot(c1, c7, linewidth=0.5)
ax[1,2].plot(c1, c7s, linewidth=2, color='red')
ax[1,2].set_title("Col 7 vs Col 1")
ax[1,2].set_xlim(c1[0],c1[-1])

ax[2,2].plot(c1, c4, linewidth=0.5, color='black')
ax[2,2].plot(c1, c5, linewidth=0.5, color='red')
ax[2,2].plot(c1, c6, linewidth=0.5, color='blue')
ax[2,2].set_title("Energy [a.u.] (Col. 4, 5 and 6)")
ax[2,2].set_xlim(c1[0],c1[-1])

fig.tight_layout()
plt.show()
#plt.savefig('graph.png', dpi=600, bbox_inches='tight')
