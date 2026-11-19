class node:
    def __init__(self,value):
        self.right= None
        self.left= None
        self.data= value
        
class bst:
    def __init__(self):
        self.root = None

            
    def insert(self,newnode):        
        if self.root  is None:
            self.root= newnode       
            return
        else:
            temp= self.root
            while True:
                if newnode.data < temp.data:
                    if temp.left is None:
                        temp.left= newnode
                        return
                    else:
                        temp= temp.left
                elif newnode.data > temp.data:
                    if temp.right is None:
                        temp.right= newnode
                        return
                    else:
                        temp= temp.right

def inorder(temp):
    if temp is None:
        return
    else:
        inorder(temp.left)
        print(temp.data, end=" ")
        inorder(temp.right)
            
btree=bst()
btree.insert(node(10))
btree.insert(node(5))
btree.insert(node(2))
btree.insert(node(15))
btree.insert(node(20))
inorder(btree.root)
