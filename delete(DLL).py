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

    def delete(self, value):
        temp = self.head

        while temp and temp.data != value:
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next:
            temp.next.prev = temp.prev


list = LinkedList()
list.append()

list.see()

list.delete(30)

print("\nAfter deletion:")

list.see()