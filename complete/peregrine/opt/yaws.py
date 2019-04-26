import numpy as np
import pandas as pd
ws, dirs = [], []
o, d = [], []
for WS in ['7.0', '8.0', '9.0', '10.0', '11.0', '12.0', '13.0', '14.0', '15.0']:
   for DIR in [0, 10, 30, 40, 50, 60]:
      ouu = np.genfromtxt('%s_%s/ouu.dat' % (WS, DIR))
      det= np.genfromtxt('%s_%s/det.dat' % (WS, DIR))
      o.extend(ouu)
      d.extend(det)

dat = pd.DataFrame({'ouu':o, 'det':d})
dat.to_csv('yaws.csv')
    
