class CircularLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self, data):
        new_node = Node (data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  
        # point to itself
            return
        temp = self.head
        while temp.next != self.head:   # reach  last node
            temp = temp.next
            temp.next = new_node
            new_node.next = self.head
        
    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")
        
        
       