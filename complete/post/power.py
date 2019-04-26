import numpy as np
from scipy.stats import weibull_min
import pandas as pd
dat = pd.read_csv('./amalia_directionally_averaged_speeds.txt', sep=r'\s+')
power = pd.read_csv('./power.csv')
ws, dirs = [], []
#speeds = [ 8., 9., 10., ]
#speeds = [3., 4., 5., 6., 7.]
speeds = [3., 4., 5., 6., 7., 8., 9., 10., 11., 12., 13., 14., 15.]
#speeds = [3.]
#speeds = [10., 11., 12., 13., 14., 15.]
ouu_exp, ouu_det, det_det, det_exp = [], [], [], []
base_exp, base_det = [], []
spees, dees, pees = [], [], []
for ii in range(dat.shape[0]):
   theseprobs = weibull_min.pdf(speeds, 3, scale=dat.average_speed[ii])
   theseprobs /= np.sum(theseprobs)
   if np.isnan(theseprobs.max()): hey
   for jj in range(len(speeds)):
      ws.append(speeds[jj])
      dirs.append(dat.direction[ii])
      fact = theseprobs[jj] * dat.probability[ii]
      subpow = power[power.ws == speeds[jj]]
      #print(speeds[jj], int(dat.direction[ii]), subpow.base_exp_power.values[0], subpow.base_det_power.values[0])
      subsubpow = subpow[subpow.dir == int(dat.direction[ii])]
      #if abs(subpow.ouu_exp_power.values[0]) < abs(subpow.ouu_det_power.values[0]): print(speeds[jj], int(dat.direction[ii]))
      #if abs(subpow.det_exp_power.values[0]) < abs(subpow.det_det_power.values[0]): print(speeds[jj], int(dat.direction[ii]))
      if abs(subpow.base_exp_power.values[0]) < abs(subpow.base_det_power.values[0]): print(speeds[jj], int(dat.direction[ii]))
      ouu_exp.append(fact * subsubpow.ouu_exp_power.values[0])
      det_exp.append(fact * subsubpow.det_exp_power.values[0])
      det_det.append(fact * subsubpow.det_det_power.values[0])
      ouu_det.append(fact * subsubpow.ouu_det_power.values[0])
      base_exp.append(fact * subsubpow.base_exp_power.values[0])
      base_det.append(fact * subsubpow.base_det_power.values[0])

      spees.append(speeds[jj])
      dees.append(dat.direction[ii])
      pees.append(fact)

dat = pd.DataFrame({'speed': spees, 'direction': dees, 'probability': pees})
dat.to_csv('./probs.csv')

print('         exp         det (GWh)')
print('OUU: ', 8760 * np.sum(ouu_exp) / 1e9, 8760 * np.sum(ouu_det) / 1e9)
print('det: ', 8760 * np.sum(det_exp) / 1e9, 8760 * np.sum(det_det) / 1e9)
print('base: ', 8760 * np.sum(base_exp) / 1e9, 8760 * np.sum(base_det) / 1e9)
