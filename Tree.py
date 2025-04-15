class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []

    def add(self,childNode):
        self.children.append(childNode)

    def printTree(self):
        print(self.data)
        for child in self.children:
            child.printTree()


root = TreeNode("School")
child1 = TreeNode("10")
child2 = TreeNode("11")
child3 = TreeNode("12")

root.add(child1)
root.add(child2)
root.add(child3)

child1.add(TreeNode("A"))
child1.add(TreeNode("B"))
child1.add(TreeNode("C"))

child2.add(TreeNode("D"))
child2.add(TreeNode("E"))
child2.add(TreeNode("F"))

child3.add(TreeNode("G"))
child3.add(TreeNode("H"))
child3.add(TreeNode("I"))



root.printTree()
