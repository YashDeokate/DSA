

#find the middle node of linked list and delete the middle node of linked list


# Class for creating a node
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


# Class for linked list operations
class MyLinkedList:
    def __init__(self, values=None):
        self.head = None
        if values:
            self.create(values)

    # Create linked list
    def create(self, values):
        self.head = None
        last = None

        for value in values:
            new_node = ListNode(value)

            if self.head is None:
                self.head = last = new_node
            else:
                last.next = new_node
                last = new_node

    # Copy the linked list
    def duplicate(self):
        items = []
        temp = self.head

        while temp:
            items.append(temp.data)
            temp = temp.next

        return MyLinkedList(items)

    # Display linked list elements
    def traverse(self):
        items = []
        temp = self.head

        while temp:
            items.append(temp.data)
            temp = temp.next

        print("  ".join(map(str, items)) + " -> None"
            if items else "List is empty")

        return items


    # Find the middle node
    def find_middle(self):
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow is None:
            print("List is empty")
            return None

        print("Middle node value:", slow.data)
        return slow.data
    
    #deletete the middle node
    
    def deletemiddle(self):
            c=0
            temp=self.head
            while temp:
                temp=temp.next
                c+=1
    
            mid=(c+1)//2
            temp=self.head
            i=1
            while i!=mid:
                prev=temp
                temp=temp.next
                i+=1
    
            prev.next=temp.next
            temp.next=None  

# Main program
if __name__ == "__main__":
    list = MyLinkedList([10, 20, 30, 40, 50])

    print("Traverse:")
    list.traverse()

  
    print("\nMiddle node:")
    list.find_middle()
    
    print("\nDelete middle node:")
    list.deletemiddle()
    list.traverse()


