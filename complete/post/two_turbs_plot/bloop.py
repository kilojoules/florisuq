"""
Copyright 2017 NREL

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License. You may obtain a copy of the
License at http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

import sys
from floris.floris import Floris
import numpy as np
from copy import deepcopy
from floris.visualization import VisualizationManager
import matplotlib.pyplot as plt
import matplotlib

if len(sys.argv) > 1:
    floris = Floris(sys.argv[1])
else:
    floris = Floris("example_input.json")

#a, b = floris.farm.turbine_map.items()
#a[0].yaw_angle = 0.43
floris.farm.flow_field.calculate_wake()
hey = None
ii = 0
fig, ax = plt.subplots(2, sharex=True, figsize=(6, 3))
plt.subplots_adjust(hspace=.09)
for ii in [0, 1]:
  for coord, turbine in floris.farm.turbine_map.items():
    if ii == 1:
        if hey is None: 
           turbine.yaw_angle = 0.43
           hey = 'hey'
        else: hey = 'hey'
    print(str(coord) + ":")
    print("\tCp -", turbine.Cp)
    print("\tCt -", turbine.Ct)
    print("\tpower -", turbine.power)
    print("\tai -", turbine.aI)
    print("\taverage velocity -", turbine.get_average_velocity())
  floris.farm.flow_field.calculate_wake()

  # Visualization
  ff_viz = deepcopy(floris.farm.flow_field)
  grid_resolution = (20, 20, 25)
  RESU = 600
  visualization_manager = VisualizationManager(ff_viz, grid_resolution=(RESU, RESU , 25))
  ff =  visualization_manager.flowfield # <--- error
  KK = 2
  mesh = ax[ii].contourf(ff.x[:, :, 12] / 1e3, ff.y[:, :, 12] / 1e3, ff.u_field[:, :, 12].reshape(RESU ** 2).reshape(RESU, RESU), 100, vmin=0, vmax=8)
  ax[ii].set_title('')
  ax[ii].set_ylim(-.3, .3)
  ax[ii].set_xlim(-.2, 1.8)
  mesh.set_clim(0, 8)
#visualization_manager.plot_z_planes([0.5])
#visualization_manager.plot_x_planes([0.5])
#visualization_manager.plot_y_planes([0.5])
#cbar_ax = fig.add_axes([1., 0.15, 0.05, 0.7])
m = plt.cm.ScalarMappable(cmap=plt.cm.viridis)
m.set_array(ff.u_field[:, :, 12].reshape(RESU ** 2).reshape(RESU, RESU))
m.set_clim(0., 8.)
p0 = ax[0].get_position().get_points().flatten()
ax_cbar = fig.add_axes([p0[0], 2 * p0[1] - .13, p0[2] - 0.1265, 0.05])
cb = fig.colorbar(m, cax=ax_cbar, label="Wind speed (m/s)", orientation='horizontal')
cb.ax.xaxis.set_ticks_position('top')
cb.ax.xaxis.set_label_position('top')
ax[1].set_xlabel('x (km)')
ax[0].set_ylabel('y (km)')
ax[1].set_ylabel('y (km)')
ax[0].xaxis.grid()
ax[1].xaxis.grid()
plt.savefig('twoturbs.png', bbox_inches='tight')
plt.clf()
