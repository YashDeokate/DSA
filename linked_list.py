#singly linked list
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
class linkedlist:
    def __init__(self):
        self.head = None
        
    def append (self, new_node):
        if (self.head == None):
            self.head = new_node

        else:
            temp=self.head
            while (temp.next!= None):
                temp = temp.next
            temp.next = new_node
                
    def print(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
list=linkedlist()
n1=node(10)
n2=node(20)
n3=node(30)
list.append(n1)
list.append(n2)
list.append(n3)      
list.print()    
    
        