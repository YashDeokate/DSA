#Hospital Management System
class Node:
    def __init__(self,name,id,pr):
        self.name=name
        self.id=id
        self.pr=pr
        self.next=None

class PriorityQueue:
    def __init__(self):
        self.front=None

    def enqueue(self,node):

        if self.front==None or node.pr<self.front.pr:
            node.next=self.front
            self.front=node
            return

        temp=self.front
        while temp.next and temp.next.pr<=node.pr:
            temp=temp.next

        node.next=temp.next
        temp.next=node

    def display(self):
        temp=self.front
        while temp:
            print(temp.name,temp.id,temp.pr)
            temp=temp.next

    def dequeue(self):
        print("deleted patient",self.front.name)
        temp=self.front
        self.front=self.front.next
        temp.next=None

    def display_next(self):
        print("next patient to be treated",self.front.next.name)

q=PriorityQueue()
q.enqueue(Node("yash",101,1))
q.enqueue(Node("nikhil",102,10))
q.enqueue(Node("rhiya",103,3))
q.enqueue(Node("parnika",104,2))
q.display()
q.display_next()
q.dequeue()
q.display()