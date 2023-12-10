class Node:
    def __init__(self, data=None, llink=None, rlink=None, thread=0):
        self.data = data
        self.llink = llink
        self.rlink = rlink
        self.thread = thread