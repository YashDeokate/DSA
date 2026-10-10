
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

    # Insert node at a given position
    def insert_at(self, pos, value):
        if pos < 0:
            raise IndexError("Position cannot be negative")

        new_node = ListNode(value)

        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(pos - 1):
            if temp is None:
                break
            temp = temp.next

        if temp is None:
            raise IndexError("Position out of range")

        new_node.next = temp.next
        temp.next = new_node

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

    # Delete node at a given position
    def delete_at(self, pos):
        if self.head is None or pos < 0:
            raise IndexError("Invalid position")

        if pos == 0:
            self.head = self.head.next
            return

        temp = self.head

        for i in range(pos - 1):
            if temp is None:
                break
            temp = temp.next

        if temp is None or temp.next is None:
            raise IndexError("Position out of range")

        temp.next = temp.next.next

    # Delete node by value
    def delete_value(self, value):
        if self.head is None:
            return False

        if self.head.data == value:
            self.head = self.head.next
            return True

        temp = self.head

        while temp.next:
            if temp.next.data == value:
                temp.next = temp.next.next
                return True

            temp = temp.next

        return False

    # Reverse the linked list
    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    # Find sums of consecutive node pairs
    def consecutive_sums(self):
        result = []
        temp = self.head

        while temp and temp.next:
            result.append(temp.data + temp.next.data)
            temp = temp.next

        print("Sum of consecutive pairs:", result)
        return result


# Main program
if __name__ == "__main__":
    list = MyLinkedList([10, 20, 30, 40, 50])

    print("Traverse:")
    list.traverse()

    print("\nInsert 25 at position 2:")
    list.insert_at(2, 25)
    list.traverse()

    print("\nMiddle node:")
    list.find_middle()

    print("\nDelete node at position 1:")
    list.delete_at(1)
    list.traverse()

    print("\nReverse:")
    list.reverse()
    list.traverse()

    print("\nConsecutive sums:")
    list.consecutive_sums()


