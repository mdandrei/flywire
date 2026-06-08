

try:
	_initialized
except NameError:
	import pandas as pd
	from scipy.sparse import csr_matrix, csc_matrix, lil_matrix, coo_matrix

	print("here")

# long index sets: 2
	d = pd.read_csv("banc_626_edge_list.csv")
	d.rename(columns={"target neuron id":"tn"}, inplace=True)
	d.rename(columns={"source neuron id":"sn"}, inplace=True)
	d["setValue"]= d.index*0+4

	e = pd.read_csv("fafb_783_edge_list.csv")
	e.rename(columns={"target neuron id":"tn"}, inplace=True)
	e.rename(columns={"source neuron id":"sn"}, inplace=True)
	e["setValue"] = e.index*0+5


# short index sets: 3
	a = pd.read_csv("manc_1.2.1_edge_list.csv")
	a.rename(columns={"target neuron id":"tn"}, inplace=True)
	a.rename(columns={"source neuron id":"sn"}, inplace=True)
	a["setValue"]= a.index*0+1


	b = pd.read_csv("maol_1.1_edge_list.csv")
	b.rename(columns={"target neuron id":"tn"}, inplace=True)
	b.rename(columns={"source neuron id":"sn"}, inplace=True)
	b["setValue"]= b.index*0+2


	c = pd.read_csv("mcns_0.9_edge_list.csv")
	c.rename(columns={"target neuron id":"tn"}, inplace=True)
	c.rename(columns={"source neuron id":"sn"}, inplace=True)
	c["setValue"]= c.index*0+3


#####################
	aNbNc = pd.concat( [a, b, c ] )
	_initialized=True

#
# logic gate 1: only keep directed edges which are in all 3 - short-index-name - data sets
# 
# After this step duplication accross all 3 is not guaranteed: just any duplication ( including within a single set, or only 2 set, or the desired all 3 )
#
L10 = aNbNc[aNbNc.duplicated(subset=['sn','tn'], keep=False )]

# Now for each [sn,tn] repeat count how many distinct sets it belongs too
distinct_setValues = L10.groupby(['sn', 'tn'])['setValue'].transform('nunique') # nunique == number of unique setValue-s in a group where [sn,tn] match

#
L11 = L10[ distinct_setValues == 3 ]

L2a = L11[ L11.setValue == 1 ].copy();
L2b = L11[ L11.setValue == 2 ].copy();
L2c = L11[ L11.setValue == 3 ].copy();

# concatenation at this point is optional 
unique_vals = pd.unique( pd.concat( [L2a[["sn","tn"]], L2b[["sn","tn"]], L2c[["sn", "tn"]]] ).values.ravel() )
mapping     = {val: i+1 for i, val in enumerate(unique_vals)}

L2a["snX"] = -1;
L2a["tnX"] = -1;
L2a["snX"] = L2a["sn"].map(mapping)
L2a["tnX"] = L2a["tn"].map(mapping)

L2b["snX"] = -1;
L2b["tnX"] = -1;

L2b["snX"] = L2b["sn"].map(mapping)
L2b["tnX"] = L2b["tn"].map(mapping)


L2c["snX"] = -1;
L2c["tnX"] = -1;
L2c["snX"] = L2c["sn"].map(mapping)
L2c["tnX"] = L2c["tn"].map(mapping)


def df_to_sparse(df, source_col, target_col):
    nodes = pd.unique(pd.concat([df[source_col], df[target_col]]))
    node_index = {node: i for i, node in enumerate(nodes)}
    
    n = len(nodes)
    matrix = lil_matrix((n, n), dtype=int)
    
    for _, row in df.iterrows():
        i = node_index[row[source_col]]
        j = node_index[row[target_col]]
        matrix[i, j] = 1
    
    return matrix, node_index


import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

def isolate_islands(matrix):
    """
    Takes a square connectivity matrix (dense, sparse lil/csr/csc, or list-of-lists).
    Returns a list of (node_indices, sub_matrix) tuples, one per island.
    """
    # normalise any input type to csr
    if isinstance(matrix, lil_matrix):
        matrix = matrix.tocsr()
    elif not hasattr(matrix, 'toarray'):
        matrix = csr_matrix(np.array(matrix))

    # symmetrise for undirected component detection
    sym = (matrix + matrix.T).astype(bool).astype(int)

    n_components, labels = connected_components(
        sym, directed=False, return_labels=True
    )

    islands = []
    for comp_id in range(n_components):
        node_indices = np.where(labels == comp_id)[0]
        sub = matrix[np.ix_(node_indices, node_indices)]
        islands.append((node_indices.tolist(), sub))


    # find the component id with the most nodes
    comp_sizes = np.bincount(labels)
    largest_id = np.argmax(comp_sizes)

    node_indices = np.where(labels == largest_id)[0]
    sub = matrix[np.ix_(node_indices, node_indices)]

    return node_indices.tolist(), sub

#    return islands

