class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None

    # Create linked list
    def create(self, values):
        for value in values:
            new_node = ListNode(value)

            if self.head is None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = new_node

    # Display linked list
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Insert at position
    def insert_at(self, pos, value):
        new_node = ListNode(value)

        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for i in range(pos - 1):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    # Find middle node
    def find_middle(self):
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow:
            print("Middle:", slow.data)

    # Delete at position
    def delete_at(self, pos):
        if pos == 0:
            self.head = self.head.next
            return

        temp = self.head
        for i in range(pos - 1):
            temp = temp.next

        temp.next = temp.next.next

    # Delete by value
    def delete_value(self, value):
        if self.head.data == value:
            self.head = self.head.next
            return

        temp = self.head
        while temp.next:
            if temp.next.data == value:
                temp.next = temp.next.next
                return
            temp = temp.next

    # Reverse linked list
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    # Consecutive sums
    def consecutive_sums(self):
        temp = self.head

        while temp and temp.next:
            print(temp.data + temp.next.data, end=" ")
            temp = temp.next
        print()


# Main program
ll = MyLinkedList()
ll.create([10, 20, 30, 40, 50])

ll.traverse()

ll.insert_at(2, 25)
ll.traverse()

ll.find_middle()

ll.delete_at(1)
ll.traverse()

ll.reverse()
ll.traverse()

ll.consecutive_sums()