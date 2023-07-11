class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

            
    def pop(self):
        popped_item = self.head.data
        self.head = self.head.next
        return popped_item

    def peek(self):
       return self.head.data

s = stack()
s.push(1)
s.push(23444)
print(s.pop())
print(s.pop())