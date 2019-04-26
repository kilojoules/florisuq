import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
SIZE = 7.
font = {'size'   : SIZE}
matplotlib.rc('font', **font)
f, ax = plt.subplots(figsize=(4.5,2.4))
dat = pd.read_csv('yaws.csv')
ax.hist([np.rad2deg(dat.ouu), np.rad2deg(dat.det)], bins=np.linspace(-25, 25, 11), label=['OUU', 'Deterministic'], normed=True, edgecolor='k', linewidth=1, color=plt.cm.viridis([0., 0.8]), align='mid')
ax.legend(ncol=1, loc='upper right', bbox_to_anchor=[.98, .95], prop={'size':SIZE-1})
#plt.legend(ncol=2, bbox_to_anchor=(.5, 1.), loc='upper center')
ax.set_ylabel('Probability mass', size=SIZE)
ax.set_xlabel("Yaw position (degrees)", size=SIZE)
ax.set_xticks(np.linspace(-25, 25, 11))
ax.set_xlim(-25, 25)
ax.xaxis.grid()
plt.savefig('yawpdf', bbox_inches='tight')
