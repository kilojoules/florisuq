import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
SIZE = 8
dat = pd.read_csv('./VSS.csv')
for ii in [10, 20, 30, 40, 50, 60]:
   dat.dir[dat.dir == 360 - ii] = -1 * ii
   print(360 - ii, -1 * ii)
f, ax = plt.subplots(4, sharex=True, figsize=(6, 4))
#f, ax = plt.subplots(4, figsize=(5, 3), sharex=True)
colors = plt.cm.coolwarm(np.linspace(0, 1, 3))
#colors = plt.cm.coolwarm(np.linspace(0, 1, np.unique(dat.ws).size))
jj = 0
names = {'vss': r'$VSS$', 'vssb': r'$VSS_b$', 'vds': r'$VDS$', 'vdsb': r'$VDS_s$'}
#names = {'vss': r'$VSS$', 'vssb': r'$VSS_\mathrm{baseline}$', 'vds': r'$VDS$', 'vdsb': r'$VDS_\mathrm{deterministic}$'}
sdats = []
SPEEDS = [3.0, 5.0, 7.0, 9.0, 11.0, 13.0]
ws = np.linspace(-2, 2, len(SPEEDS))
colors = plt.cm.viridis(np.linspace(0, 1, len(SPEEDS)))
for ii, nam in enumerate(['vss', 'vssb', 'vds', 'vdsb']):
   for jj, WS in enumerate(SPEEDS):
      subdat = dat[dat.ws == WS]
      #ax[ii].plot(subdat['dir'], subdat[nam], marker='x', label=WS, c=colors[jj])
      ax[ii].bar(subdat['dir'].values + ws[jj], 100 * (subdat[nam].values - 1), width=ws[-1] - ws[-2], label=int(WS), facecolor=colors[jj], edgecolor='k')
   if ii < 2: ax[ii].set_ylabel(names[nam] + ' (\%)', size=SIZE, labelpad=9)
   elif ii == 2: ax[ii].set_ylabel(names[nam] + ' (\%)', size=SIZE, labelpad=6)
   else: ax[ii].set_ylabel(names[nam] + ' (\%)', size=SIZE)
      #ax[ii].set_yscale('log')
ax[0].set_ylim(0., 4)
ax[1].set_ylim(0., 2.5)
ax[2].set_ylim(0., 15.)
ax[3].set_ylim(97 - 100., 2)
ax[3].set_xlabel('Inflow direction (degrees)', size=SIZE)
ax[0].legend(ncol=len(SPEEDS), loc='upper center', bbox_to_anchor=(.5, 1.6), title='Wind speed (m/s)', prop={'size':SIZE})
#ax[3].set_xticks(subdat['dir'].values)
#ax[3].set_xticklabels(subdat['dir'].values)
plt.minorticks_on()
for ii in range(4):
  ax[ii].set_xticks([-60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60])
  ax[ii].xaxis.grid(which='minor')
ax[3].set_xticks([-60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60])
minor_locator = AutoMinorLocator(2)
ax[3].xaxis.set_minor_locator(minor_locator)
plt.savefig('VSS.pdf', bbox_inches='tight')
#plt.savefig('/Users/jquick/Documents/yaw_uncertainty_article/Figures/VSS.pdf', bbox_inches='tight')
