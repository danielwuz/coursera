class Node:

    def __init__(self, lo, hi, value=None):
        self.lo = lo
        self.hi = hi
        self.value = value
        # tree properties
        self.left = self.right = None
        self.max_endpoint = hi

    def __repr__(self):
        return "[(%d, %d, %d)\n%r, %r]" % (self.lo, self.hi, self.max_endpoint,
                                           self.left, self.right)

    def intersect(self, lo, hi):
        return self.lo <= lo <= self.hi or \
            self.lo <= hi <= self.hi


def put(root, node):
    '''put interval-value pair into ST'''
    if not root:
        return node
    # update max endpoint
    root.max_endpoint = max(root.max_endpoint, node.max_endpoint)
    # find which subtree to go
    if root.lo > node.lo:
        root.left = put(root.left, node)
    else:
        root.right = put(root.right, node)
    return root


def get(root, lo, hi):
    '''value pair with given interval'''
    if not root:
        return None
    if root.lo == lo and root.hi == hi:
        return root.value
    if lo < root.lo:
        return get(root.left, lo, hi)
    else:
        return get(root.right, lo, hi)


def delete(lo, hi):
    '''delete given interval'''
    pass


def intersects_any(root, lo, hi):
    '''any intervals that intersect the given interval'''
    if not root or root.intersect(lo, hi):
        return root
    if root.left and root.left.max_endpoint >= lo:
        return intersects_any(root.left, lo, hi)
    else:
        return intersects_any(root.right, lo, hi)

from random import randint


def createNode():
    a, b = randint(0, 10), randint(0, 10)
    return Node(min(a, b), max(a, b), randint(0, 10))


intervals = [createNode() for _ in range(10)]
root = createNode()
for interval in intervals:
    root = put(root, interval)
