class ListNode:

    def __init__(self, item):
        self.item = item
        self.next = None


class ListQueue:

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        old_tail = self.tail
        self.tail = ListNode(item)
        if not self:
            self.head = self.tail
        else:
            old_tail.next = self.tail

    def dequeue(self):
        value = self.head.item
        self.head = self.head.next
        # NOTE: update tail pointer if no data anymore
        if not self:
            self.tail = None
        return value

    def __nonzero__(self):
        return self.head is not None

    def __iter__(self):
        def iter():
            temp = self.head
            while temp:
                yield temp.item
                temp = temp.next
        return iter()

# test client
lq = ListQueue()
for i in range(10):
    lq.enqueue(i)

for item in lq:
    print item

print lq.dequeue()
