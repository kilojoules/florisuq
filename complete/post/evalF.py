import sys
from example_optimization import florisEval
import numpy as np
yaw = np.genfromtxt('./%s.dat' % sys.argv[-1])
f = str((florisEval(**{'functions':-33, 'asv':1e3, 'cv':np.array(yaw)}))['fns'][0])
outf = open('%s.det' % sys.argv[-1], 'w')
outf.write(f)
outf.close()
