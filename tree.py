import Node
class stack:
    def __init__(self):
        self.data= [] #스택 생성
        self.a=[]
    def inorder(self, root):
        while root or self.data:
            if root:
                self.data.append(root)
                root = root.llink
            else:
                temp = self.data.pop()
                self.a.append(temp.data)
                root = temp.rlink
        return self.a


if __name__=="__main__":
    n1 = Node.Node(1, None, None)
    n2 = Node.Node(4, n1, None)
    n3 = Node.Node(16, None, None)
    n4 = Node.Node(25, None, None)
    n5 = Node.Node(20, n3, n4)
    n6 = Node.Node(15, n2, n5)
    root = n6
    tree = stack()
    print(tree.inorder(root))