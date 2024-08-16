
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head =  None

class Stack:

    def __init__(self):
        self.LinkedList = LinkedList()

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def push(self,value):
        node = Node(value)
        if self.LinkedList.head == None:
            self.head = node
        else:
            node.next = self.LinkedList.head 
            self.LinkedList.head = node

    def pop(self):
        self.LinkedList.head = self.LinkedList.head.next
    
    def peek(self):
         if self.LinkedList.head == None:
            return "Empty"
        else:
            return self.LinkedList.head.value

a = Stack()
print(a.isEmpty())