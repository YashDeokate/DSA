# write a func to swap first and last node in dll

class Node:
    def __init__(self, val):
        self.prev = None
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self):
        while True:
            nn = int(input("enter node: "))
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

    def see(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def swap(self):
        temp=node1=self.head #node1 is first node
        while temp.next:
            temp=temp.next
            
        temp.next=node1.next
        node1.next=None
        node1.prev=temp.prev
        temp.prev.next=node1
        temp.prev=None
        self.head=temp    


list = LinkedList()
list.append()
print("\n Before Swapping")
list.see()

list.swap()
print ("\n after swapping:")
list.see()