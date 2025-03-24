from Tree import Tree
from node import Node
import debug

'''
LCA is the class that handles lowest common ancestor querys in the tree
'''
class LCA:
    def __init__(self, tree : Tree): # needs a tree to initialise
        self.tree = tree
        self.n = tree.n

    @debug.debugDecorator
    def query(self, a : int, b: int) -> int: # the query runs O(log(n))
        if a == b: # if the nodes are the same they are there lca
            return a
        node_a : Node = self.tree.nodes[a] # get the nodes from there id
        node_b : Node = self.tree.nodes[b]
        if node_a.depth == node_b.depth: # if the nodes are at the same height we find the lowest i such that the nodes don't share the (2**i)'th parent
            for i in range(len(node_a.ancestors)-1, -1, -1):
                if node_a.ancestors[i] != node_b.ancestors[i]:
                    return self.query(node_a.ancestors[i], node_b.ancestors[i]) # use recursion now that we have climbed at least half the distance to the lca
            return node_a.parent # if the nodes share every ancestor, there parent must be there lca
        else: # if the nodes are at different depths we must do level ancestor first (find parents where the nodes are at the same level)
            if node_a.depth > node_b.depth: # make sure that node b is of greater depth
                node_a, node_b, a, b = node_b, node_a, b, a # switch node a and b
            d = 1
            d2 = 1
            if node_a.depth+1 == node_b.depth:
                return self.query(node_b.parent, a)
            while node_a.depth < node_b.depth-d: # find the lowest d2 such that 2**d2 is greater than the difference in depth of the nodes
                d *= 2
                d2 += 1
            return self.query(node_b.ancestors[d2-2], a) # use recursion now that we have removed at least half of the difference between the depths