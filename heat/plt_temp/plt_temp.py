import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')
filename = parser.parse_args().filename

data = np.loadtxt(filename)
c1 =data[:,0]	# Step
c3 =data[:,2]	# classic temperature
c4 =data[:,3]	# Energies
c5 =data[:,4]
c6 =data[:,5]
c7 =data[:,6]	# distribution temperature
c8 =data[:,7]	# Kinetic energy

fig, ax = plt.subplots(3, 2, figsize=(6,9))
fig.suptitle(filename)
linew=1
ax[0,0].plot(c3, c5, linewidth=linew)
ax[0,0].set_title("Col 5 vs Col 3")
ax[0,0].set_ylim(c5[0],c5[-1])

ax[1,0].plot(c7, c5, linewidth=linew)
ax[1,0].set_title("Col 5 vs Col 7")
ax[1,0].set_ylim(c5[0],c5[-1])

ax[2,0].plot(c3, c7, linewidth=linew)
ax[2,0].set_title("Col 7 vs Col 3")

ax[0,1].plot(c1, c3, linewidth=linew)
ax[0,1].set_title("Col 3 vs Col 1")
ax[0,1].set_xlim(c1[0],c1[-1])

ax[1,1].plot(c1, c7, linewidth=linew)
ax[1,1].set_title("Col 7 vs Col 1")
ax[1,1].set_xlim(c1[0],c1[-1])

ax[2,1].plot(c1, c4, linewidth=linew, color='black')
ax[2,1].plot(c1, c5, linewidth=linew, color='red')
#ax[2,1].plot(c1, c6, linewidth=linew, color='blue')
ax[2,1].set_title("Energy (Col. 4, 5 and 6)")
ax[2,1].set_xlim(c1[0],c1[-1])

fig.tight_layout()
plt.show()
#plt.savefig('graph.png', dpi=600, bbox_inches='tight')
