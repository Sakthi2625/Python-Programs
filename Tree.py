# # General Tree:

# class TreeNode:
#     def __init__(self,data):
#         self.data = data
#         self.children = []

#     def add(self,childNode):
#         self.children.append(childNode)

#     def printTree(self):
#         print(self.data)
#         for child in self.children:
#             child.printTree()


# root = TreeNode("School")
# child1 = TreeNode("10")
# child2 = TreeNode("11")
# child3 = TreeNode("12")

# root.add(child1)
# root.add(child2)
# root.add(child3)

# child1.add(TreeNode("A"))
# child1.add(TreeNode("B"))
# child1.add(TreeNode("C"))

# child2.add(TreeNode("D"))
# child2.add(TreeNode("E"))
# child2.add(TreeNode("F"))

# child3.add(TreeNode("G"))
# child3.add(TreeNode("H"))
# child3.add(TreeNode("I"))



# root.printTree()

# Binary Tree:

class BinaryNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def addValue(root,data):
    if not root:
            print("First")
            return BinaryNode(data)
    if data< root.data:
        root.right=addValue(root.right,data)
    else:
        root.left=addValue(root.left,data)
    return root
def printValues(root):
    if root:
        printValues(root.left)
        print(root.data,end="-->")
        printValues(root.right)
    
root = None
l=[50,30,70,20,40,60,80]
for i in l:
    print(root)
    root=addValue(root,i)
    print(root.data, "next")

printValues(root)