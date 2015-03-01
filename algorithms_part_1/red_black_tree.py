RED = True
BLACK = False


class TreeNode:

    def __init__(self, key, value, color=RED):
        self.key = key
        self.value = value
        self.color = color
        self.left = self.right = None

    def __repr__(self):
        return "(%d, %s)" % (self.key, 'RED' if self.color else 'BLACK')


def put(root, key, val):
    if not root:
        # create a tree node with red at bottom
        return TreeNode(key, val)
    if root.key > key:
        root.left = put(root.left, key, val)
    elif root.key < key:
        root.right = put(root.right, key, val)
    else:
        root.value = val

    # maintain red-black property
    if isRed(root.right) and not isRed(root.left):
        root = rotateLeft(root)
    if isRed(root.left) and isRed(root.left.left):
        root = rotateRight(root)
    if isRed(root.left) and isRed(root.right):
        flipColor(root)
    return root


def isRed(node):
    return node and node.color is RED


def rotateLeft(root):
    new_root = root.right
    root.right = new_root.left
    new_root.left = root
    new_root.color = root.color
    root.color = RED
    return new_root


def rotateRight(root):
    new_root = root.left
    root.left = new_root.right
    new_root.right = root
    new_root.color = root.color
    root.color = RED
    return new_root


def flipColor(root):
    root.color = RED
    if root.left:
        root.left.color = BLACK
    if root.right:
        root.right.color = BLACK


def get(root, key):
    while root:
        if root.key == key:
            return root.value
        elif root.key > key:
            root = root.left
        else:
            root = root.right
    return None


# testing code below
from random import randint


def createNode():
    a, b = randint(0, 100), randint(0, 100)
    return TreeNode(a, b)


# random keys
root = createNode()
for i in range(100):
    root = put(root, randint(0, 10), randint(0, 10))


root = TreeNode(-1, -1)
num_of_nodes = randint(2**15, 2**20)
for i in range(num_of_nodes):
    root = put(root, i, i)

global_level = 0


def pprint(root, level=0):
    if not root:
        return
    pprint(root.left, level + 1)
    global global_level
    global_level += level
    pprint(root.right, level + 1)


pprint(root)
print(num_of_nodes)
print(global_level * 1.0 / num_of_nodes)
