class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        
    def append(self,newnode):
        
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head          
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode      

    def see(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

    

n1=Node(30)
n2=Node(40)
n3=Node(50)

list=LinkedList()
list.append(n1)
list.append(n2)
list.append(n3)
list.see()
