import numpy as np
for ii in range(0, 360):
   detdet = np.genfromtxt('working%i/det.det' % ii)
   ouudet = np.genfromtxt('working%i/ouu.det' % ii)
   detexp = np.genfromtxt('working%i/det.exp' % ii)
   ouuexp = np.genfromtxt('working%i/ouu.exp' % ii)

