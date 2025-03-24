import math

'''
Nodes is the base of the tree, and saves som import data regarding that node
'''
class Node:
    def __init__(self, parent, depth, n):
        self.parent = parent
        self.ancestors = [-1] * math.ceil(math.log2(n)+1)
        self.ancestors[0] = parent
        self.depth = depth
        self.children = []