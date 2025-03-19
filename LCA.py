from Tree import Tree
from node import Node
import debug

class LCA:
    def __init__(self, tree : Tree):
        self.tree = tree
        self.n = tree.n

    @debug.debugDecorator
    def query(self, a : int, b: int) -> int:
        if a == b:
            return a
        node_a : Node = self.tree.nodes[a]
        node_b : Node = self.tree.nodes[b]
        if node_a.depth == node_b.depth:
            for i in range(len(node_a.ancestors)-1, -1, -1):
                if node_a.ancestors[i] != node_b.ancestors[i]:
                    return self.query(node_a.ancestors[i], node_b.ancestors[i])
            return node_a.parent
        else:
            if node_a.depth > node_b.depth:
                node_a, node_b, a, b = node_b, node_a, b, a
            d = 1
            while node_a.depth < node_b.depth-d:
                d *= 2
            return self.query(node_b.ancestors[d-1], a)