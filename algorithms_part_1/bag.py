class Bag:

    def __init__(self):
        self.stack = []

    def add(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)

    def __iter__(self):
        return self.stack.__iter__()


# NOTE: test client
b = Bag()
for i in range(10):
    b.add(i)

for k in b:
    print k
