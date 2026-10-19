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
            nn=int(input("enter node"))
            newnode=Node(nn)
            if nn==1:
                break
            else:
                temp=self.head
                if temp:
                    while temp.next:
                        temp=temp.next
                    temp.next=newnode
                    newnode.prev=temp
                else:

                    self.head=newnode

    def see(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

    def insert(self):
        pos=int(input("enter position"))
        nn=int(input("enter node"))
        newnode=Node(nn)
        if pos==1:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
        else:
            temp=self.head
            p=1
            while p!=pos-1:
                temp=temp.next
                p+=1
            newnode.next = temp.next
            newnode.prev = temp
            temp.next = newnode
            if newnode.next:
                newnode.next.prev=newnode


list=LinkedList()
list.append()
list.see()
list.insert()
list.see()

