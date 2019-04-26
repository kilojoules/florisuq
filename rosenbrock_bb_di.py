#!/usr/bin/env python

# Dakota will execute this script as
#   rosenbrock_bb_di.py params.in results.out
#  The command line arguments will be extracted by dakota.interfacing automatically.

# necessary python modules
import dakota.interfacing as di

# ----------------------------
# Parse Dakota parameters file
# ----------------------------

params, results = di.read_parameters_file()

# -------------------------------
# Convert and send to application
# -------------------------------

# set up the data structures the rosenbrock analysis code expects
# for this simple example, put all the variables into a single hardwired array
# The asv has to be mapped back into an integer
#continuous_vars = [ params['d1'], params['d2'] , params['d3'], params['d4'], params['d5'], params['d6']]# , params['uuv1'], params['wuv1']]
if 'speed' in params: continuous_vars = [params['d1'],  params['d2'],  params['d3'],  params['d4'],  params['d5'],  params['d6'],  params['d7'],  params['d8'],  params['d9'],  params['d10'],  params['d11'],  params['d12'],  params['d13'],  params['d14'],  params['d15'],  params['d16'],  params['d17'],  params['d18'],  params['d19'],  params['d20'],  params['d21'],  params['d22'],  params['d23'],  params['d24'],  params['d25'],  params['d26'],  params['d27'],  params['d28'],  params['d29'],  params['d30'],  params['d31'],  params['d32'],  params['d33'],  params['d34'],  params['d35'],  params['d36'],  params['d37'],  params['d38'],  params['d39'],  params['d40'],  params['d41'],  params['d42'],  params['d43'],  params['d44'],  params['d45'],  params['d46'],  params['d47'],  params['d48'],  params['d49'],  params['d50'],  params['d51'],  params['d52'], params['speed'], params['direction']]
else: continuous_vars = [params['d1'],  params['d2'],  params['d3'],  params['d4'],  params['d5'],  params['d6'],  params['d7'],  params['d8'],  params['d9'],  params['d10'],  params['d11'],  params['d12'],  params['d13'],  params['d14'],  params['d15'],  params['d16'],  params['d17'],  params['d18'],  params['d19'],  params['d20'],  params['d21'],  params['d22'],  params['d23'],  params['d24'],  params['d25'],  params['d26'],  params['d27'],  params['d28'],  params['d29'],  params['d30'],  params['d31'],  params['d32'],  params['d33'],  params['d34'],  params['d35'],  params['d36'],  params['d37'],  params['d38'],  params['d39'],  params['d40'],  params['d41'],  params['d42'],  params['d43'],  params['d44'],  params['d45'],  params['d46'],  params['d47'],  params['d48'],  params['d49'],  params['d50'],  params['d51'],  params['d52']]


#import json 
#with open('example_input.json', 'r') as file:
#     json_data = json.load(file)
#     json_data['farm']['properties']['air_density'] = params['uuv1']
#     json_data['farm']['properties']['wind_speed'] = params['uuv1']
#with open('example_input.json', 'w') as file:
#    json.dump(json_data, file, indent=2)


active_set_vector = 1
#if results["obj_fn"].asv.function:
   #active_set_vector += 1
#if results["obj_fn"].asv.gradient:
#    active_set_vector += 2
#if results["obj_fn"].asv.hessian:
#    active_set_vector += 4

# Alternatively, the ASV can be accessed by index in
# function, gradient, hessian order
#for i, bit in enumerate(results["obj_fn"].asv):
#    if bit:
#        active_set_vector += 1 << i

# set a dictionary for passing to rosenbrock via Python kwargs
rosen_params = {}
rosen_params['cv'] = continuous_vars
rosen_params['asv'] = [active_set_vector]
rosen_params['functions'] = 1

# execute the rosenbrock analysis as a separate Python module
#from rosenbrock import rosenbrock_list
from example_optimization import florisEval

rosen_results = florisEval(**rosen_params)


# ----------------------------
# Return the results to Dakota
# ----------------------------

# Insert functions from rosen into results
# Results iterator provides an index, response name, and response
for i, n, r in results:
    if r.asv.function:
        r.function = rosen_results['fns'][i]
    if r.asv.gradient:
        r.gradient = rosen_results['fnGrads'][i]
    if r.asv.hessian:
        r.hessian = rosen_results['fnHessians'][i]

results.write()
