import Node
class Thread_tree:
    def thread_inorder(self,root):
        temp = root
        while not temp.llink == None:
            temp = temp.llink
        print(temp.data)
        while True:
            temp = self.find_thread(temp)
            print(temp.data)
            if temp.rlink == None:
                break

    def find_thread(self, node):
        pre = node
        node = node.rlink
        #if node == None:
         #   return node
        if pre.thread == 1:
            return node
        while not node.llink == None:
            node = node.llink
        return node

if __name__=="__main__":
    n1 = Node.Node('A', None, None, 1)
    n2 = Node.Node('B', None, None, 1)
    n3 = Node.Node('C', n1, n2)
    n4 = Node.Node('D', None, None, 1)
    n5 = Node.Node('E', None, None)
    n6 = Node.Node('F', n4, n5)
    n7 = Node.Node('G', n3, n6)
    n1.rlink=n3
    n2.rlink=n7
    n4.rlink=n6
    root = n7
    tr = Thread_tree()
    tr.thread_inorder(root)