
import pandas as pd
import numpy as np

from scipy.sparse import csr_matrix, csc_matrix, lil_matrix, coo_matrix # coo_matrix == coordinate labeled matrix
from scipy.sparse.csgraph import connected_components

import networkx as nx


try:
	_initialized
except NameError:

	print("Init section: do once")

# long index sets: 2
	d = pd.read_csv("../banc_626_edge_list.csv")
	d.rename(columns={"target neuron id":"tn"}, inplace=True)
	d.rename(columns={"source neuron id":"sn"}, inplace=True)
	d["setValue"]= d.index*0+4

	e = pd.read_csv("../fafb_783_edge_list.csv")
	e.rename(columns={"target neuron id":"tn"}, inplace=True)
	e.rename(columns={"source neuron id":"sn"}, inplace=True)
	e["setValue"] = e.index*0+5


# short index sets: 3
	a = pd.read_csv("../manc_1.2.1_edge_list.csv")
	a.rename(columns={"target neuron id":"tn"}, inplace=True)
	a.rename(columns={"source neuron id":"sn"}, inplace=True)
	a["setValue"]= a.index*0+1


	b = pd.read_csv("../maol_1.1_edge_list.csv")
	b.rename(columns={"target neuron id":"tn"}, inplace=True)
	b.rename(columns={"source neuron id":"sn"}, inplace=True)
	b["setValue"]= b.index*0+2


	c = pd.read_csv("../mcns_0.9_edge_list.csv")
	c.rename(columns={"target neuron id":"tn"}, inplace=True)
	c.rename(columns={"source neuron id":"sn"}, inplace=True)
	c["setValue"]= c.index*0+3

	_initialized=True

#
# form a symmetric ( i.e. weak ) connection matrix and return mat index to neuron forward and reverse correspondence
#
def df_to_sparse(df, source_col, target_col):
    nodes = pd.unique(pd.concat([df[source_col], df[target_col]]))
    node_index = {node: i for i, node in enumerate(nodes)}
    
    rnode_index = {v: k for k, v in node_index.items()}

    n = len(nodes)
    matrix = lil_matrix((n, n), dtype=int)
    
    for _, row in df.iterrows():
        i = node_index[row[source_col]]
        j = node_index[row[target_col]]
        matrix[i, j] = 1
    
    return matrix, node_index, rnode_index


def isolate_islands(matrix, rnode_index):
    """
    Takes a square connectivity matrix (dense, sparse lil/csr/csc, or list-of-lists).
    Returns a list of (node_indices) per island.
    """
    # normalise any input type to csr
    if isinstance(matrix, lil_matrix):
        matrix = matrix.tocsr()
    elif not hasattr(matrix, 'toarray'):
        matrix = csr_matrix(np.array(matrix))

    # symmetrise for undirected component detection
    sym = (matrix + matrix.T).astype(bool).astype(int)

    n_components, labels = connected_components(
        sym, directed=False, return_labels=True )

    islands = []
    for comp_id in range(n_components):
        node_indices = np.where(labels == comp_id)[0]
        sub = matrix[np.ix_(node_indices, node_indices)]
        islands.append([node_indices.tolist(), sub])

# find the component id with the most nodes
    comp_sizes = np.bincount(labels)
    largest_id = np.argmax(comp_sizes)
    node_indices = np.where(labels == largest_id)[0]

    Mc = islands[largest_id][1];
    #Mc = Mc + np.transpose(Mc) # connectivity matrix: symmetrized

    # neuron indixes 
    nset = []
    for key in node_indices:
      nset.append( rnode_index[key] )


    #return n_components, labels
    #return nset
		# returning neurons in the largest subgraph, sequential node indecies and connectivity Mat for the largest
		# subset off sequential indecies
    return np.array(nset), node_indices, Mc # islaislands, largest_id

## need to return the island verteces referred to the original neuron index


def islandingSingle():

	return -1


def isomorphismCheck():

	return -1



##################### Approach 1: m* only repeats: label and structure identical in coincident subgraphs
aNbNc = pd.concat( [a, b, c ] )

# logic gate 1: only keep directed edges which are in all 3 - short-index-name - data sets
# After this step duplication accross all 3 is not guaranteed: just any duplication ( including within a single set, or only 2 set, or the desired all 3 )
L10 = aNbNc[aNbNc.duplicated(subset=['sn','tn'], keep=False )]

# Now for each [sn,tn] repeat count how many distinct sets it belongs too
distinct_setValues = L10.groupby(['sn', 'tn'])['setValue'].transform('nunique') # nunique == number of unique setValue-s in a group where [sn,tn] match

L11 = L10[ distinct_setValues == 3 ]
L2  = L11[ L11.setValue == 1 ].copy();

# identify unique neuron numbers either as source, or target and index them sequentially 1 and up
unique_vals = pd.unique( pd.concat( [L2[["sn","tn"]]] ).values.ravel() )
mapping     = { val: i+1 for i, val in enumerate(unique_vals) }

# dont actually need this
L2["snX"] = -1;
L2["tnX"] = -1;
L2["snX"] = L2a["sn"].map(mapping)
L2["tnX"] = L2a["tn"].map(mapping)

##################### Approach 1
mat, ni, rni = df_to_sparse(L2, "sn", "tn" )
nset, niseq, Mcs = isolate_islands(mat, rni );


### Approach 2: m* and f* repeats via isomorphism checks: only structure is guaranteed to be identical 
