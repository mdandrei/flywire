
import pandas as pd
from scipy.sparse import csr_matrix, csc_matrix, lil_matrix, coo_matrix
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components


import networkx as nx
import numpy as np


from parse import df_to_sparse, isolate_islands


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
	nset, niseq, Mcs = isolate_islands(mat, rni );

	return nset, niseq, Mcs


def are_isomorphic(mat1, mat2):
    """
    Check structural equivalence of two directed graphs up to node relabeling.

    Parameters
    ----------
    mat1, mat2 : lil_matrix, csr_matrix, or ndarray
        Square directed connectivity matrices to compare.

    Returns
    -------
    bool
        True if graphs are structurally identical up to node relabeling.
    dict or None
        Node mapping {mat1 node -> mat2 node} if isomorphic, else None.
    """
    # normalise to dense numpy
    if hasattr(mat1, 'toarray'): mat1 = mat1.toarray()
    if hasattr(mat2, 'toarray'): mat2 = mat2.toarray()

    # quick size check before expensive isomorphism test
    if mat1.shape != mat2.shape:
        return False, None

    G1 = nx.from_numpy_array(mat1, create_using=nx.DiGraph)
    G2 = nx.from_numpy_array(mat2, create_using=nx.DiGraph)

    gm = nx.algorithms.isomorphism.DiGraphMatcher(G1, G2)
    if gm.is_isomorphic():
        mapping = list(gm.isomorphisms_iter())[0]
        return True, mapping
    return False, None


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

