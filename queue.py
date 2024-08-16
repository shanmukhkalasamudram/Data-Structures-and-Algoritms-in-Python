

class Queue:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self,value):
        self.items.append(value)
    
    def dequeue(self):
        if(self.isEmpty()):
            return "Empty"
        else:
            return self.items.pop(0)
    
    def delete(self):
        self.items = None

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)