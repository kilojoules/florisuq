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
for coord, turbine in floris.farm.turbine_map.items():
    if hey: turbine.yaw_angle = 0.43
#    else: hey = 'hey'
    print(str(coord) + ":")
    print("\tCp -", turbine.Cp)
    print("\tCt -", turbine.Ct)
    print("\tpower -", turbine.power)
    print("\tai -", turbine.aI)
    print("\taverage velocity -", turbine.get_average_velocity())
floris.farm.flow_field.calculate_wake()

# Visualization
SIZE = 8
plt.figure(figsize=(2, 3))
matplotlib.rcParams.update({'font.size': SIZE})
ff_viz = deepcopy(floris.farm.flow_field)
grid_resolution = (100, 100, 25)
visualization_manager = VisualizationManager(ff_viz, grid_resolution)
visualization_manager.plot_z_planes([0.5])
#visualization_manager.plot_y_planes([0.5])
plt.title('')
plt.xlabel('Western Position (m)')
plt.ylabel('Norther Position (m)')
plt.xlim(-500, 500)
plt.ylim(-600, 1000)
#plt.colorbar(label='Wind Speed (m/s)')
plt.savefig('look', bbox_inches='tight', dpi=500)
plt.clf()
