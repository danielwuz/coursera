class ListNode:

    def __init__(self, item):
        self.item = item
        self.next = None


class LinkListStack:

    def __init__(self):
        self.head = None

    def push(self, item):
        node = ListNode(item)
        node.next = self.head
        self.head = node

    def pop(self):
        if not self.head:
            raise ValueError()
        temp = self.head.item
        self.head = self.head.next
        return temp

    def empty(self):
        return self.head is None


class ArrayStack:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.data = [None] * self.capacity
        self.tail = 0  # pointer to last append element

    def push(self, item):
        if self.tail == self.capacity:
            self.resize(self.capacity * 2)
        self.data[self.tail] = item
        self.tail += 1

    def __nonzero__(self):
        return self.tail != 0

    def pop(self):
        if not self:
            raise ValueError("Empty Stack")
        if self.tail > 0 and self.tail == self.capacity // 4:
            self.resize(self.capacity // 2)
        self.tail -= 1
        value = self.data[self.tail]
        self.data[self.tail] = None
        return value

    def __len__(self):
        return self.tail

    def resize(self, new_capacity):
        new_data = [None] * new_capacity
        # pay attention: we should only iterate items that need to be copied
        for i in range(self.tail):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity


# test client
astack = ArrayStack()
for i in range(1000):
    astack.push(i)
while astack:
    astack.pop()


def evaluate_expression(expr):
    mapping = {
        '+': lambda x, y: x + y,
        '*': lambda x, y: x * y,
    }
    operators = []
    operands = []
    for symbol in expr:
        if symbol == ')':
            v1 = operands.pop()
            v2 = operands.pop()
            op = operators.pop()
            operands.append(op(v2, v1))
        elif symbol.isdigit():
            operands.append(int(symbol))
        elif symbol in mapping:
            operators.append(mapping[symbol])
    return operands[-1]


expr = '( 1 + ( ( 2 + 3 ) * ( 4 * 5 ) ) )'
print evaluate_expression(expr)
