from node import Node
import math
import random
import debug

'''
Tree handles all the nodes in the tree and has different ways of building the tree
'''

class Tree:
    def __init__(self): # we don't initialise the tree with anything since the build functions will build it
        self.nodes : list[Node] = []
        self.n = 0

    @debug.debugDecorator
    def build_ancestors(self, n): # this is a helper function and is called by build to prepare the nodes for binary lifting
        for i in range(1, math.ceil(math.log2(n)+1)):
            for node in self.nodes:
                node.ancestors[i] = self.nodes[node.ancestors[i-1]].ancestors[i-1]

    # build is the main builder to build the tree using a parent list
    @debug.debugDecorator
    def build(self, parentList : list[int]) -> None: # parent list contains parent of element 1 to n-1, it must stand that P[i+1] < i
        n = len(parentList)+1
        self.n = n
        self.nodes = [Node(-1, 0, n)]
        for i in range(len(parentList)):
            self.nodes.append(Node(parentList[i], self.nodes[parentList[i]].depth+1, n))
            self.nodes[parentList[i]].children.append(i+1)
        self.build_ancestors(n)

    @debug.debugDecorator
    def build_random(self, n): # this is a secondary builder, it builds a valid parent list and sends it to build
        parentList = []
        for i in range(n-1):
            parentList.append(random.randint(0, i))
        self.build(parentList)
        return parentList

    #@debug.debugDecorator
    def print_node(self, node : int, indent : int): # this function uses recursion to print the tree in a nice format
        prefix = ""
        if indent-1 > 0: prefix = "|  " * (indent - 1)
        if indent > 0: prefix += "|--"
        print(prefix, node)
        for i in self.nodes[node].children: # all children are called with one more indent
            self.print_node(i, indent + 1)

    @debug.debugDecorator
    def print_tree(self): # this initialises th print_node recursion by calling it at the root (node 0)
        self.print_node(0, 0)
