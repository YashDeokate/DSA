class node:
def __init__(self,val):
self.data=val
self.next=None
class linkedlist:
def __init__(self):
self.head=None
def append(self,new_node) :
if self.head==None:
self.head=new_node
else:
temp=self.head
while(temp.next):
temp=temp.next
temp.next=new_node
def print(self):
temp=self.head
while(temp):
print(temp.data,end=" -> ")
temp=temp.next
print("None")
def insertatPos(self,new_node,pos):
if pos==1:
self.head.next==new_node
self.head=new_node
else:
p=1
temp=self.head
while(p!=pos-1):
temp=temp.next