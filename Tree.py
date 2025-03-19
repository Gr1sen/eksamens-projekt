from node import Node
import math
import random
import debug

class Tree:
    def __init__(self):
        self.nodes : list[Node] = []
        self.n = 0

    @debug.debugDecorator
    def build_ancestors(self, n):
        for i in range(1, math.ceil(math.log2(n))):
            for node in self.nodes:
                node.ancestors[i] = self.nodes[node.ancestors[i-1]].ancestors[i-1]

    # parent list contains parent of element 1 to n-1, it must stand that P[i+1] < i
    @debug.debugDecorator
    def build(self, parentList):
        n = len(parentList)+1
        self.n = n
        self.nodes = [Node(-1, 0, n)]
        for i in parentList:
            self.nodes.append(Node(i, self.nodes[i].depth+1, n))
            self.nodes[parentList[i]].children.append(i+1)
        self.build_ancestors(n)

    @debug.debugDecorator
    def build_random(self, n):
        parentList = []
        for i in range(n-1):
            parentList.append(random.randint(0, i))
        self.build(parentList)
        return parentList

    @debug.debugDecorator
    def print_node(self, node : int):
        pass

    @debug.debugDecorator
    def print_tree(self):
        pass
