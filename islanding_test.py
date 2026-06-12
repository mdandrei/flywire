
import pandas as pd
from scipy.sparse import csr_matrix, csc_matrix, lil_matrix, coo_matrix
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components


import networkx as nx
import numpy as np


from parse import df_to_sparse, isolate_islands, are_isomorphic


mat1 = lil_matrix((8,8), dtype=int)
mat2 = lil_matrix((8,8), dtype=int)

g1 = [ [ 0, 1, 0, 1, 0, 0, 0, 0 ], [ -1, 0, 1, -1, 0, 0, 0, 0 ], [ 0, -1, 0, -1, -1, 0, 0, 0 ],  [ -1, 1, 1, 0, 1, 0, 0, 0  ],   
           [ 0, 0, 1, -1, 0, 0, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 1, -1 ], [ 0, 0, 0, 0, 0, -1, 0, -1 ], [ 0, 0, 0, 0, 0, 1, 1, 0 ]];

g2 = [ [ 0, 0, 0, -1, 0, 0, 0, 1 ], [ 0, 0, -1, 0, 1, 1, 1, 0 ], [ 0, 1, 0, 0, 1, 0, 0, 0 ], [ 1, 0, 0, 0, 0, 0, 0, 1 ], \
 [ 0, -1, -1, 0, 0, 0, 1, 0 ], [ 0, -1, 0, 0, 0, 0, 1, 0 ], [ 0, -1, 0, 0, -1, -1, 0, 0 ], [ -1, 0, 0, -1, 0, 0, 0, 0 ]];

dftx = pd.read_csv("sntnT.txt", comment="%", names = ['sn', 'tn', 'sn1', 'tn1', 'sn2', 'tn2', 'sn3', 'tn3'], sep='\s+', engine='python')


def pp( M ):
	"""
	matrix to a graph plottable matrix ( no ,  no [] )
	"""
	arr = M.toarray()
	for row in arr:
		print(' '.join(map(str, row)))

	return

def islandingSingleTest( df, sn, tn ): # broken at the moment

	mat, ni, rni = df_to_sparse(df, sn, tn )
	nset, niseq, Mcs = isolate_islands(mat, rni, imode=0 );

	return nset, niseq, Mcs


#############################
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




###
nset, niseq, Mcs  = islandingSingleTest( dftx[ ['sn', 'tn']], 'sn', 'tn' )
nset1, niseq1, Mcs1  = islandingSingleTest( dftx[ ['sn1', 'tn1']], 'sn1', 'tn1' )
nset2, niseq2, Mcs2  = islandingSingleTest( dftx[ ['sn2', 'tn2']], 'sn2', 'tn2' )
nset3, niseq3, Mcs3  = islandingSingleTest( dftx[ ['sn3', 'tn3']], 'sn3', 'tn3' )




b01, _ =  are_isomorphic( Mcs, Mcs1 )
b02, _ =  are_isomorphic( Mcs, Mcs2 )
b03, _ =  are_isomorphic( Mcs, Mcs3 )

