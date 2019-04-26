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
import numpy as np
from floris.floris import Floris
from copy import deepcopy
from visualization_manager import VisualizationManager

if len(sys.argv) > 1:
    floris = Floris(sys.argv[1])
else:
    floris = Floris("example_input.json")

yaws = np.zeros(7)
#yaws = [2.075107359e-05, -0.0001368726696,          0.435,          0.435,          0.435,          0.435 , 0.435]
turbines    = [turbine for _, turbine in floris.farm.flow_field.turbine_map.items()]
for k,turbine in enumerate(turbines):
    turbine.yaw_angle = yaws[k]
floris.farm.flow_field.calculate_wake()

for coord, turbine in floris.farm.turbine_map.items():
    print(str(coord) + ":")
    print("\tCp -", turbine.Cp)
    print("\tCt -", turbine.Ct)
    print("\tpower -", turbine.power)
    print("\tai -", turbine.aI)
    print("\taverage velocity -", turbine.get_average_velocity())

# Visualization
ff_viz = deepcopy(floris.farm.flow_field)
grid_resolution = (100, 100, 25)
visualization_manager = VisualizationManager(ff_viz, grid_resolution)
visualization_manager.plot_z_planes([0.5])
visualization_manager.plot_x_planes([0.5])
#visualization_manager.plot_y_planes([0.5])
