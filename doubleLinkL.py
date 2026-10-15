class Node:
    def __init__(self,val):
        self.prev=None
        self.data=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def append(self):
     while True:
        nn = int(input("enter node"))

        if nn == 1:
            break

        newnode = Node(nn)
        temp = self.head

        if temp:
            while temp.next:
                temp = temp.next
            temp.next = newnode
            newnode.prev = temp
        else:
            self.head = newnode
            
    def print(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next        

list=LinkedList()
list.append()
list.print()


