import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
dat = pd.read_csv('./probs.csv')
dat.direction[dat.direction > 180] -= 360
ns = np.unique(dat.speed).size
nd = np.unique(dat.direction).size
f, ax = plt.subplots(figsize=(6, 3))
c = ax.imshow(dat.probability.values.reshape((nd, ns)).T) 
ax.set_yticks(range(ns))
ax.set_xticks(range(nd))
ax.set_yticklabels(np.unique(dat.speed))
ax.set_xticklabels(np.unique(dat.direction))
for label in ax.xaxis.get_ticklabels()[1::2]:
    label.set_visible(False)
ax.set_xlabel('Direction (degrees)')
ax.set_ylabel('Speed (m/s)')
#plt.yticks(np.unique(dat.direction))
plt.colorbar(c, label='Probability mass')
plt.savefig('imshowpdf')
plt.clf()


summs = {}
f, ax = plt.subplots(figsize=(6, 3))
for ii in np.unique(dat.direction): summs[ii] = 0
for ii, spee in enumerate((np.unique(dat.speed))):
   subdat = dat[dat.speed == spee].reset_index()
   ax.bar(subdat.direction, subdat.probability, bottom=[summs[di] for di in subdat.direction], label=int(spee), width=5)
   for jj in range(nd):
      summs[subdat.direction[jj]] += subdat.probability[jj]
ax.set_ylabel('Probability')
ax.set_xlabel('Direction (degrees)')
ax.legend(title='Wind Speed (m/s)')
plt.savefig('barpdf')
plt.clf()
