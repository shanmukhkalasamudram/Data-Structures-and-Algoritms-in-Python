class TreeNode:
    def __init__(self,data,children=[]):
        self.data = data
        self.children = children
    
    def __str__(self,level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def addChild(self,TreeNode):
        self.children.append(TreeNode)

    
tree = TreeNode('Food',[])
veg = TreeNode('veg',[])
non_veg = TreeNode('non_veg',[])

tree.addChild(veg)
tree.addChild(non_veg)

dal = TreeNode('dal',[])
idly = TreeNode('idly',[])
chicken = TreeNode('chicken',[])
mutton = TreeNode('mutton',[])

veg.addChild(dal)
non_veg.addChild(chicken)
veg.addChild(idly)
non_veg.addChild(mutton)

print(tree)