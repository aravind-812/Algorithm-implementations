class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        return self.head is None
    
    def enqueue(self, data):
        newNode = Node(data);
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
        self.length += 1


    def dequeue(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        data =  self.head
        self.head = self.head.next

        if self.head == None:
            self.tail = None
        return data
    
    def peek(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        return self.head.data

q = queue()

q.enqueue(1)
print(q.peek())





















