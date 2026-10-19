#write a func to count occurance of number in the dll

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

    def count_occ(self,num):
        temp=self.head
        cnt=0
        while temp:
            if temp.data == num:
                cnt+=1
            temp=temp.next
        print("\n the ocurance:",cnt)        
    


list = LinkedList()
list.append()

list.see()
list.count_occ(2)

