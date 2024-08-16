class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.ta = None
        self.length = None
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

class Queue:
    def __init__(self):
        self.llist = LinkedList()
    
    def __str__(self):
        values = [str(x) for x in self.llist]
        return ' '.join(values)

    def enqueue(self,value):
        new = Node(value)
        if self.llist.head == None:
            self.llist.head = new
            self.llist.tail = new
        else:
            self.llist.tail.next = new
            self.llist.tail = new
    
    def dequeue(self):
        if self.llist.head == self.llist.tail:
            self.llist.head = None
            self.llist.tail = None
        else:
            self.llist.head = self.llist.head.next

    def isEmpty():
        if self.llist.head == None:
            return True
        else:
            return False
        
    def peek():
        if isEmpty():
            return "Empty"
        else:
            return self.llist.head.value
        
    

