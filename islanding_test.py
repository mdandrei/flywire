
import pandas as pd
from scipy.sparse import csr_matrix, csc_matrix, lil_matrix, coo_matrix
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

mat1 = lil_matrix((8,8), dtype=int)
mat2 = lil_matrix((8,8), dtype=int)

g1 = [ [ 1, 1, 0, 1, 0, 0, 0, 0 ], [ -1, 0, 1, -1, 0, 0, 0, 0 ], [ 0, -1, 0, -1, -1, 0, 0, 0 ],  [ -1, 1, 1, 0, 1, 0, 0, 0  ],   
           [ 0, 0, 1, -1, 0, 0, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 1, -1 ], [ 0, 0, 0, 0, 0, -1, 0, -1 ], [ 0, 0, 0, 0, 0, 1, 1, 0 ]];

g2 = [ [ 0, 0, 0, -1, 0, 0, 0, 1 ], [ 0, 0, -1, 0, 1, 1, 1, 0 ], [ 0, 1, 0, 0, 1, 0, 0, 0 ], [ 1, 0, 0, 0, 0, 0, 0, 1 ], \
 [ 0, -1, -1, 0, 0, 0, 1, 0 ], [ 0, -1, 0, 0, 0, 0, 1, 0 ], [ 0, -1, 0, 0, -1, -1, 0, 0 ], [ -1, 0, 0, -1, 0, 0, 0, 0 ]];


i = 0
for rowg1, rowg2 in zip(g1,g2):
	mat1[i] = rowg1
	mat2[i] = rowg2
	i+=1;

mat1 = abs( mat1 )
mat2 = abs( mat2 )
