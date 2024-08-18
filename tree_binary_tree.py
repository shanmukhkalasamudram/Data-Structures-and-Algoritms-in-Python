
# 1. Implementation with LinkedList 

import Queue as qu

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode("Food")
leftChild = TreeNode('Veg')
rightChild = TreeNode('Nonveg')

newBT.leftChild = leftChild
newBT.rightChild = rightChild

# Preorder

def preOrder(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrder(rootNode.leftChild)
    preOrder(rootNode.rightChild)


def inOrder(rootNode):
    if not rootNode:
        return
    inOrder(rootNode.leftChild)
    print(rootNode.data)
    inOrder(rootNode.rightChild)

def postOrder(rootNode):
    if not rootNode:
        return
    inOrder(rootNode.leftChild)
    inOrder(rootNode.rightChild)
    print(rootNode.data)

def postOrder(rootNode):
    if not rootNode:
        return
    inOrder(rootNode.leftChild)
    inOrder(rootNode.rightChild)
    print(rootNode.data)

def levelOrder(rootNode):
    if not rootNode:
        return

    else:
        cus = qu.Queue()
        cus.enqueue(rootNode)
        while not(cus.isEmpty()):
            root = cus.dequeue()
            print(root.value.data)
            if(root.value.leftChild is not None):
                cus.enqueue(root.value.leftChild)
            
            if(root.value.rightChild is not None):
                cus.enqueue(root.value.rightChild)

            
# preOrder(newBT)
# inOrder(newBT)
# postOrder(newBT)
# levelOrder(newBT)

