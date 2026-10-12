

#concatenate two linked list

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
    
    
    def concatenate(self, other_list):
        if not self.head:
            self.head = other_list.head
            return

        if not other_list.head:
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = other_list.head       
            
# Main program
if __name__ == "__main__":
    list = MyLinkedList([10, 20, 30, 40, 50])

    print("Traverse:")
    list.traverse()

    print("\nConcatenate with another list:")
    other_list = MyLinkedList([60, 70, 80])
    list.concatenate(other_list)
    list.traverse()
    
