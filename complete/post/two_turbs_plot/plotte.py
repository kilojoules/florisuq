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
fig, ax = plt.subplots(1, 2, sharey=True, figsize=(3, 4))
plt.subplots_adjust(wspace=1)
for ii in [0, 1]:
  for coord, turbine in floris.farm.turbine_map.items():
    if ii == 1:
        if hey: turbine.yaw_angle = 0.43
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
  mesh = ax[ii].contourf(ff.x[:, :, 12] / 1e3, ff.y[:, :, 12] / 1e3, ff.u_field[:, :, 12].reshape(RESU ** 2).reshape(RESU, RESU), 100, vmin=0, vmax=8)
  ax[ii].set_title('')
  ax[ii].set_xlim(-.4, .4)
  ax[ii].set_ylim(-.6, .8)
  mesh.set_clim(0, 8)
#visualization_manager.plot_z_planes([0.5])
#visualization_manager.plot_x_planes([0.5])
#visualization_manager.plot_y_planes([0.5])
cbar_ax = fig.add_axes([1., 0.15, 0.05, 0.7])
m = plt.cm.ScalarMappable(cmap=plt.cm.viridis)
m.set_array(ff.u_field[:, :, 12].reshape(RESU ** 2).reshape(RESU, RESU))
m.set_clim(0., 8.)
c = fig.colorbar(m, cax=cbar_ax, label="Wind Speed (m/s)")
ax[0].set_xlabel('Western Position (km)')
ax[1].set_xlabel('Western Position (km)')
ax[0].set_ylabel('Northern Position (km)')
plt.savefig('hey.png', bbox_inches='tight')
plt.clf()
