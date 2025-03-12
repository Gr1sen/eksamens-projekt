import math

class Node:
    def __init__(self, parent, depth, n):
        self.parent = parent
        self.ancestors = [-1] * math.ceil(math.log2(n))
        self.ancestors[0] = parent
        self.depth = depth