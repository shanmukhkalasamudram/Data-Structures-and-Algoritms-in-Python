class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
        return result
    
    def append(self,value):
        new_node = Node(value)
        if(self.head == None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def preappend(self,value):
        new_node = Node(value)
        if(self.head == None):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def appendspecific(self,index,value):
        new_node = Node(value)
        if(self.head == None):
            self.head = new_node
            self.tail = new_node
        if(index == 0):
            new_node.next = self.head
            self.head = new_node
        temp_node = self.head
        for i in range(index-1):
            if not(temp_node.next): #If No Next
                temp_node.next = new_node
                self.tail = new_node
                return
            temp_node = temp_node.next
        new_node.next = temp_node.next
        temp_node.next = new_node
        self.length += 1

    def traverse(self):
        now = self.head
        while now is not None:
            print(now.value)
            now = now.next
    def get(self,index):
        if( index <0 or index >= self.length):
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value
    def popfirst(self):
        if self.length == 1:
            self.head = None
            self.last = None
        self.head = self.head.next
        self.length -= 1
    def pop(self):
        if self.length = 0:
            return None
        pop_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return pop_node
    
    def appendCircular(self,value):
        new_node = Node(value)
        if(self.length == 0):
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        self.length += 1
        
    


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
print(ll)
ll.preappend(3)
ll.appendspecific(20,5)
ll.traverse()
ll.popfirst()
print(ll)
print(ll.get(2))