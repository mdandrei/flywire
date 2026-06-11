
import pandas as pd
from scipy.sparse import csr_matrix, csc_matrix, lil_matrix, coo_matrix
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

mat1 = lil_matrix((8,8), dtype=int)
mat2 = lil_matrix((8,8), dtype=int)

g1 = [ [ 0, 1, 0, 1, 0, 0, 0, 0 ], [ -1, 0, 1, -1, 0, 0, 0, 0 ], [ 0, -1, 0, -1, -1, 0, 0, 0 ],  [ -1, 1, 1, 0, 1, 0, 0, 0  ],   
           [ 0, 0, 1, -1, 0, 0, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 1, -1 ], [ 0, 0, 0, 0, 0, -1, 0, -1 ], [ 0, 0, 0, 0, 0, 1, 1, 0 ]];

g2 = [ [ 0, 0, 0, -1, 0, 0, 0, 1 ], [ 0, 0, -1, 0, 1, 1, 1, 0 ], [ 0, 1, 0, 0, 1, 0, 0, 0 ], [ 1, 0, 0, 0, 0, 0, 0, 1 ], \
 [ 0, -1, -1, 0, 0, 0, 1, 0 ], [ 0, -1, 0, 0, 0, 0, 1, 0 ], [ 0, -1, 0, 0, -1, -1, 0, 0 ], [ -1, 0, 0, -1, 0, 0, 0, 0 ]];


i = 0
for rowg1, rowg2 in zip(g1,g2):
	print( rowg1 )
	print( rowg2 )
	mat1[i] = rowg1
	mat2[i] = rowg2
	i+=1;

#mat1 = abs( mat1 )
#mat2 = abs( mat2 )

m1f2 = ( mat1 > 0 ) * 1;
m2f2 = ( mat2 > 0 ) * 1;

print( m1f2.todense(), "\n" )
print( m2f2.todense(), "\n" )

nc1, labels1 = connected_components(
        mat1, directed=False, return_labels=True )

nc2, labels2 = connected_components(
        mat2, directed=False, return_labels=True )


def pp( M ):
	"""
	matrix to a graph plottable matrix ( no ,  no [] )
	"""
	arr = M.toarray()
	for row in arr:
		print(' '.join(map(str, row)))

	return

