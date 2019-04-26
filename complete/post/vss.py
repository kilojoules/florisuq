import numpy as np
import pandas as pd
vss, vssb, vds, vdsb = [], [], [], []
ws, dirs = [], []
ouu_det_power, ouu_exp_power, det_det_power, det_exp_power = [], [], [], []
base_exp_power, base_det_power = [], []
for WS in ['3.0', '4.0', '5.0', '6.0', '7.0', '8.0', '9.0', '10.0', '11.0', '12.0', '13.0', '14.0', '15.0']:
   for DIR in [0, 10, 30, 40, 50, 60, 350, 340, 330, 320, 310, 300]:
      ouu_exp = np.genfromtxt('%s_%s/ouu.exp' % (WS, DIR))
      ouu_det = np.genfromtxt('%s_%s/ouu.det' % (WS, DIR))
      det_exp = np.genfromtxt('%s_%s/det.exp' % (WS, DIR))
      det_det = np.genfromtxt('%s_%s/det.det' % (WS, DIR))
      base_exp = np.genfromtxt('%s_%s/base.exp' % (WS, DIR))
      base_det = np.genfromtxt('%s_%s/base.det' % (WS, DIR))
      ouu_det_power.append(ouu_det)
      ouu_exp_power.append(ouu_exp)
      det_exp_power.append(det_exp)
      det_det_power.append(det_det)
      base_exp_power.append(base_exp)
      base_det_power.append(base_det)
      vss.append(ouu_exp / det_exp)
      vssb.append(ouu_exp / base_exp)
      vds.append(det_det / base_det)
      vdsb.append(det_exp / base_exp)
      ws.append(WS)
      dirs.append(DIR)
dat = pd.DataFrame({'ws':ws, 'dir':dirs, 'vss':vss, 'vssb':vssb, 'vds':vds, 'vdsb':vdsb})
dat.to_csv('VSS.csv')
dat = pd.DataFrame({'ouu_det_power':ouu_det_power, 'ouu_exp_power':ouu_exp_power, 'det_exp_power':det_exp_power, 'det_det_power':det_det_power, 'base_exp_power':base_exp_power, 'base_det_power': base_det_power, 'ws':ws, 'dir':dirs})
dat.to_csv('power.csv')
    
