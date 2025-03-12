from Tree import Tree
from node import Node

class LCA:
    def __init__(self, tree : Tree):
        self.tree = tree

    def query(self, a, b):
        if a == b:
            return a
        node_a : Node = self.tree.nodes[a]
        node_b : Node = self.tree.nodes[b]
        if node_a.depth == node_b.depth:
            for i in range(len(node_a.ancestors)-1, 0, -1):
                if node_a.ancestors[i] != node_b.ancestors[i]:
                    return self.query(node_a.ancestors[i], node_b.ancestors[i])
            return node_a.parent
        else:
            if node_a.depth > node_b.depth:
                node_a, node_b, a, b = node_b, node_a, b, a
            d = 1
            while node_a.depth+d < node_b.depth:
                d *= 2
            return self.query(node_a.ancestors[d], b)