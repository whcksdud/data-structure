import Node
def getheight(root):
    if root == None:
        return 0
    return max(getheight(root.rlink),getheight(root.llink))+1
def isbalance(Node):
    if Node == None:
        return True
    diff = getheight(Node.llink) - getheight(Node.rlink)
    if abs(diff) > 1 :
        print("균형 트리가 아닙니다.")
    else:
        print("균형 트리입니다.")

if __name__=="__main__":
    n1 = Node.Node(1, None, None)
    n2 = Node.Node(4, n1, None)
    n3 = Node.Node(16, None, None)
    n4 = Node.Node(25, None, None)
    n5 = Node.Node(20, n3, n4)
    n6 = Node.Node(15, n2, n5)
    root1 = n6
    isbalance(root1)

    n1 = Node.Node(1, None, None)
    n2 = Node.Node(2, n1, None)
    n3 = Node.Node(3, n2, None)
    n4 = Node.Node(4, n3, None)
    n5 = Node.Node(5, n4, None)
    n6 = Node.Node(6, n5, None)
    root2 = n6
    isbalance(root2)