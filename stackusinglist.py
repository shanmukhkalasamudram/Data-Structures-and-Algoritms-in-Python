
class Stack:
    def __init__(self,maxSize):
        self.list = []
        self.maxSize = maxSize 
    
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    def push(self,value):
        if self.isFull():
            return 'Full'
        self.list.append(value)

    def pop(self):
        if(self.list == []):
            return "Empty"
        else:
            self.list.pop()
    
    def peek(self):
        if(self.list == []):
            return "Empty"
        else:
            self.list[len(self.list)-1]

a = Stack(4) #Size of Stack 
print(a.isEmpty())