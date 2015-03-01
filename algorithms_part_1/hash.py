from collections import namedtuple

Node = namedtuple('Node', ['key', 'value'])


class ChainingHash:

    def __init__(self, capacity=17):
        self.st = [[] for _ in range(capacity)]
        self.capacity = capacity

    def put(self, key, value):
        i = self._hash(key)
        chain = self.st[i]
        for j in range(len(chain)):
            if chain[j].key == key:
                chain[j].value = value
                return
        chain.append(Node(key, value))

    def get(self, key):
        i = self._hash(key)
        for k, value in self.st[i]:
            if k == key:
                return value
        return None

    def _hash(self, key):
        return (key & 0x7fffffff) % self.capacity


st = ChainingHash()

for i in range(10):
    st.put(i, i)


class LinearProbingHash:

    def __init__(self, capacity=17):
        self.st = [None] * capacity
        self.capacity = capacity

    def put(self, key, value):
        i = self._hash(key)
        temp = i
        while self.st[i]:
            if self.st[i].key == key:
                break
            i = (i + 1) % self.capacity
            if i == temp:
                raise ValueError("hash table full")
        self.st[i] = Node(key, value)

    def get(self, key):
        i = self._hash(key)
        temp = i
        while self.st[i]:
            if self.st[i].key == key:
                return self.st[i].value
            i = (i + 1) % self.capacity
            if i == temp:
                raise ValueError("hash table full")
        return None

    def _hash(self, key):
        return (key & 0x7fffffff) % self.capacity


from random import randint


st = LinearProbingHash()

for _ in range(10):
    i = randint(0, 100)
    st.put(i, i)
