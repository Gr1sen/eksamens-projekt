'''
we use a debug decorator to see whenever a function is called.
how to use

import debug
@debug.debugDecorator
def foo():
    pass
'''

import LCA
import Tree
import node
from random import randint

def debugDecorator(func):
    def wrapper(*args, **kwargs):
        print(f"[DEBUG] Calling {func.__name__}({args}, {kwargs})")
        return func(*args, **kwargs)
    return wrapper

def systemTest():
    # edge case tree has one node
    testTree = Tree.Tree()
    testTree.build([])
    assert len(testTree.nodes) == 1
    assert testTree.nodes[0].parent == -1
    assert testTree.nodes[0].children == []
    assert testTree.nodes[0].depth == 0
    assert testTree.nodes[0].ancestors == [-1]
    testLca = LCA.LCA(testTree)
    assert testLca.query(0, 0) == 0

    # standard case for tree of size 10
    testTree = Tree.Tree()
    testTree.build([0,0,1,2,1,5,4,5,5])
    testLca = LCA.LCA(testTree)
    assert testLca.query(0, 0) == 0
    assert testLca.query(4, 6) == 0
    assert testLca.query(6, 4) == 0
    assert testLca.query(3, 9) == 1
    assert testLca.query(3, 1) == 1
    assert testLca.query(9, 8) == 5
    assert testLca.query(0, 9) == 0

    # test that lca(a, b) == lca(b, a)
    for i in range(10):
        testTree = Tree.Tree()
        testTree.build_random(randint(1,100))
        testTree.print_tree()
        testLca = LCA.LCA(testTree)
        for j in range(100):
            a = randint(0,testLca.n-1)
            b = randint(0,testLca.n-1)
            assert testLca.query(a,b) == testLca.query(b,a)

    # big tree
    testTree = Tree.Tree()
    testTree.build_random(100000)
    for j in range(100000):
        a = randint(0, testLca.n - 1)
        b = randint(0, testLca.n - 1)
        assert 0 <= testLca.query(a, b) < 100000 # simply assert that the value is sensible

if __name__ == '__main__':
    systemTest()