
# 1. Implementation with List 

# Left Child = 2X
# Right Chld = 2X+1

class BinaryTree:
    def __init__(self,size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self,value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return 'Full'
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        return 'Inserted'

    def searchNode(self,nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return True
            
        return False

    def preOrder(self,index):
        if index > self.lastUsedIndex:
            return 
        print(self.customList[index])
        self.preOrder(index*2)
        self.preOrder(index*2 + 1)
    
    def inOrder(self,index):
        if index > self.lastUsedIndex:
            return 
        
        self.preOrder(index*2)
        print(self.customList[index])
        self.preOrder(index*2 + 1)

    def postOrder(self,index):
        if index > self.lastUsedIndex:
            return 
        
        self.preOrder(index*2)
        self.preOrder(index*2 + 1)
        print(self.customList[index])

    def levelOrder(self,index):
        for i in range(index,self.lastUsedIndex+1):
            print(self.customList[1])

newBT = BinaryTree(7)
print(newBT.insertNode("Food"))
print(newBT.insertNode("Veg"))
print(newBT.insertNode("NV"))
newBT.preOrder(1)