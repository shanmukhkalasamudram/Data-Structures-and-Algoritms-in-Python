class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    def __str__(self):
        return str(self.value)

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += ' - '
            temp_node = temp_node.next

    def append(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def prepend
    
new_node = DLL()
new_node.append(10)
new_node.append(10)
new_node.append(10)
print(new_node.head)