import pandas as pd
d1 = pd.read_csv('./1.dat', sep=r'\s+')[['d1', 'd2', 'obj_fn_1', 'obj_fn_2', 'obj_fn_3']]
d2 = pd.read_csv('./2.dat', sep=r'\s+')[['d1', 'd2', 'obj_fn_1', 'obj_fn_2', 'obj_fn_3']]
fin = (d1 + d2) / 2
fin.to_csv('./dakota_tabular.dat', sep='\t')
