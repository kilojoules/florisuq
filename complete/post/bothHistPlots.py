import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import pandas as pd
f, ax = plt.subplots(1, 2, figsize=(6, 3))
for ii, typ in enumerate(['go', 'OUU']):
  dat = pd.read_csv('./%sHist.dat' % typ, sep=r'\s+')
  print(dat.columns)
  ax[ii].plot(dat.obj_fn / -1e6, c='k', lw=3, zorder=0)
  if typ == 'go': ax[ii].set_ylabel('Deterministic Power Production (MW)')
  else: ax[ii].set_ylabel('Expecteded Power Production (MW)')
  dat.drop(dat.columns[:2], inplace=True, axis=1)
  ax2 = np.rad2deg(dat).drop('obj_fn', axis=1).plot(ax=ax[ii], legend=None, secondary_y=True)
#ax2 = ax.twinx()
  if ii > 0: ax2.set_ylabel("Turbine Yaw Position ($^\circ$)")
  ax[ii].set_xlabel('Optimization Iteration')

legend_elements = [
                   Line2D([0], [0], marker='o', color='k', lw=3, label='Power',
                          markerfacecolor=None, markeredgecolor='k'),
                   Line2D([0], [0], color='g', label='Yaw Position',
                          markerfacecolor=None, markeredgecolor='k')]

#ax2.legend(handles=legend_elements, loc='lower center', bbox_to_anchor=[.5, 1.])
#plt.tight_layout()
plt.subplots_adjust(wspace=.4)
plt.savefig('hists')
#plt.savefig('hists', bbox_inches='tight')

