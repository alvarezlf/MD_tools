import matplotlib.pyplot as plt
import numpy as np

font1 = {'family':'Sans','weight':'bold','size':8}
font2 = {'family':'Sans','weight':'regular', 'size':8}

#font = font2

plt.rcParams['font.family'] = font2['family']
plt.rcParams['font.size'] = font2['size']
plt.rcParams['font.weight'] = font2['weight']
fig, ax = plt.subplots(figsize=(17./2.54,6./2.54))
#plt.setp(ax.spines.values(), lw=2)
ax.tick_params(which='major')#, width=2)

# conversion factor from step to time in [ps]
#conv=2.418884254E-5*4

# # # distances (center)
ax1 = plt.subplot(111)
#plt.tick_params('x', labelbottom=False)
#plt.ticklabel_format(useOffset=False)
#plt.vlines(2001*conv, 0, 2, color='gray', linestyle='dashed', label='Exitation')

# DATA
# ∙  →  ↔  ⇌  ─  ═  ≡
# 2 HO∙ → 2 H$_2$O$_2$
# H$_2$O$_2$ + HO∙ → HO$_2$∙ → O$_2$
# Ar─OH + HO∙ → Ar─O∙ +H$_2$O
# C$_{}$ + HO∙ → C$_{}$─OH
# C$_{}$─C$_{}$

lw_val=1.0

#d1=np.loadtxt('')
#plt.plot(d1[:,0], d1[:,1], lw=lw_val, label='C$_{}$─C$_{}$') #
#plt.plot(d1[:,0], d1[:,2], lw=lw_val, label='C$_{}$─C$_{}$') #
#plt.plot(d1[:,0], d1[:,3], lw=lw_val, label='C$_{}$─C$_{}$') #

#d2=np.loadtxt('')
#plt.plot(d2[:,0], d2[:,1], lw=lw_val, label='C$_{}$─C$_{}$') #
#plt.plot(d2[:,0], d2[:,2], lw=lw_val, label='C$_{}$─C$_{}$') #
#plt.plot(d2[:,0], d2[:,3], lw=lw_val, label='C$_{}$─C$_{}$') #

#d3=np.loadtxt('')
#plt.plot(d3[:,0], d3[:,1], lw=lw_val, label='C$_{}$─C$_{}$') #
#plt.plot(d3[:,0], d3[:,2], lw=lw_val, label='C$_{}$─C$_{}$') #
#plt.plot(d3[:,0], d3[:,3], lw=lw_val, label='C$_{}$─C$_{}$') #

#d4=np.loadtxt('')
#plt.plot(d4[:,0], d4[:,1], lw=lw_val, label='C$_{}$─C$_{}$') #
#plt.plot(d4[:,0], d4[:,2], lw=lw_val, label='C$_{}$─C$_{}$') #
#plt.plot(d4[:,0], d4[:,3], lw=lw_val, label='C$_{}$─C$_{}$') #

#d5=np.loadtxt('')
#plt.plot(d5[:,0], d5[:,1], lw=lw_val, label='C$_{}$─C$_{}$') #
#plt.plot(d5[:,0], d5[:,2], lw=lw_val, label='C$_{}$─C$_{}$') #
#plt.plot(d5[:,0], d5[:,3], lw=lw_val, label='C$_{}$─C$_{}$') #

#d6=np.loadtxt('')
#plt.plot(d6[:,0], d6[:,1], lw=lw_val, label='C$_{}$─C$_{}$') #
#plt.plot(d6[:,0], d6[:,2], lw=lw_val, label='C$_{}$─C$_{}$') #
#plt.plot(d6[:,0], d6[:,3], lw=lw_val, label='C$_{}$─C$_{}$') #

#d7=np.loadtxt('')
#plt.plot(d7[:,0], d7[:,1], lw=lw_val, label='C$_{}$─C$_{}$') #
#plt.plot(d7[:,0], d7[:,2], lw=lw_val, label='C$_{}$─C$_{}$') #
#plt.plot(d7[:,0], d7[:,3], lw=lw_val, label='C$_{}$─C$_{}$') #

#d8=np.loadtxt('')
#plt.plot(d8[:,0], d8[:,1], lw=lw_val, label='C$_{}$─C$_{}$') #
#plt.plot(d8[:,0], d8[:,2], lw=lw_val, label='C$_{}$─C$_{}$') #
#plt.plot(d8[:,0], d8[:,3], lw=lw_val, label='C$_{}$─C$_{}$') #

#2. Distance
ax1.legend(loc='upper right')
ax1.set_ylabel('Distance [Å]', fontdict=font1)
ax1.set_ylim(0.5,3)
ax1.set_yticks([1, 2, 3])

#X axis
ax1.set_xlabel('Time [ps]', fontdict=font1)
ax1.set_xlim(0,)
#ax1.set_xticks([])

plt.tight_layout()
plt.show()
#plt.savefig("/home/nicalfil/figures/hlrn-anode-molX-N.svg", format="svg")
