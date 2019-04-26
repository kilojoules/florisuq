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

from floris import Floris
import json
import numpy as np

def florisEval(**kwargs):

    # accept input
    x = kwargs['cv']
    NTURBS = 2
    yaws = x[:NTURBS]
    if len(x) > NTURBS:
       speed = None
       ti = x[NTURBS]
       #for ii in range(len(yaws)):
       #   yaws[ii] += np.deg2rad(direction)
    else:
       speed = None
       direction = None

    # configure input file
    filename = 'example_input.json'
    with open(filename, 'r') as f:
       data = json.load(f)
       if ti: data['farm']['properties']['turbulence_intensity'] = ti
       #if direction: 
       #    data['farm']['properties']['wind_direction'] += direction
       #    data['farm']['properties']['wind_direction'] %= 360
    with open(filename+'rm', 'w') as f:
       json.dump(data, f, indent=4)
    floris = Floris(filename+'rm')
    floris.farm.set_wake_model("gauss")

    # Run floris with input yaw settings
    floris.farm.set_yaw_angles(yaws, calculate_wake=True)

    # Determine power production
    power_initial = np.sum([turbine.power for turbine in floris.farm.turbines])

    retval = dict([])
    retval['fns'] = list(np.nan_to_num([power_initial] + [turbine.power for turbine in floris.farm.turbines]))
    return(retval)


