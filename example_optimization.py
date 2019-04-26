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

# import sys
# sys.path.append('../floris')
from floris.floris import Floris
import numpy as np
import json
import os
import OptModules  # modules used for optimizing FLORIS

def florisEval(**kwargs):
#def florisEval(yaws=[0,0,0,0], density=1.225):

    # DAKOTA setup
    NTURBS = 52
    x = kwargs['cv']
    ASV = kwargs['asv']
    retval = dict([])
    yaws = x[:NTURBS]
    if len(x) > NTURBS:
       speed = x[NTURBS]
       direction = x[NTURBS + 1]
    else:
       speed = None
       direction = None
    #print('density',density)
    #print('speed',speed)
    #print('direction',direction)

    filename = 'Peetz.json'
    with open(filename, 'r') as f:
       data = json.load(f)
       if speed: data['farm']['properties']['wind_speed'] = speed
       if direction: data['farm']['properties']['wind_direction'] = direction
    os.remove(filename)
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

    floris = Floris(filename)


     # run FLORIS with no yaw
    turbines    = [turbine for _, turbine in floris.farm.flow_field.turbine_map.items()]
    for k,turbine in enumerate(turbines):
         turbine.yaw_angle = yaws[k]
    floris.farm.flow_field.calculate_wake()
    power_initial = np.sum([turbine.power for turbine in turbines])  # determine initial power production

    retval['fns'] = [-1 * power_initial]
    return(retval)
    
    
    
