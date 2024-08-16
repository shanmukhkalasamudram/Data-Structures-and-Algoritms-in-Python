# No need to allot memory allocation and we just shift the top of the queue
#When enqueue -> Top will be incremeneted 
#when Dequeue -> Start will be incremented 
#After Shift of one time, Top will be joining at the begining of the list 

class Queue:
    def __init__(self,maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isFull(self):
        if self.top +1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False
    
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def enqueue(self,value):
        if self.isFull():
            return "Full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value

    def dequeue(self):
        if self.isEmpty():
            return "empty"
        else:
            ele = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.top = -1
                self.start = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return ele

    def peek(self):
        if self.isEmpty():
            return "zempty"
        else:
            return self.items[self.start]

    def delete(self):
        self.start = -1
        self.top = -1
        self.items = self.maxSize * [None] 

q = Queue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()


print(q.peek())