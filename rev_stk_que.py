class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top == None

    def push(self, val):
        nn = Node(val)
        nn.next = self.top
        self.top = nn

    def pop(self):
        if self.isempty():
            return None

        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.data

    def see(self):
        temp = self.top
        while temp:
            print(temp.data)
            temp = temp.next


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isempty(self):
        return self.front == None

    def enqueue(self, val):
        nn = Node(val)

        if self.front == None:
            self.front = nn
            self.rear = nn
        else:
            self.rear.next = nn
            self.rear = nn

    def dequeue(self):
        if self.isempty():
            return None

        temp = self.front
        self.front = self.front.next

        if self.front == None:
            self.rear = None

        return temp.data

    def see(self):
        temp = self.front
        while temp:
            print(temp.data)
            temp = temp.next


def reverse2(s1):
    q1 = Queue()
    s2 = Stack()

    # Transfer Stack to Queue
    while not s1.isempty():
        q1.enqueue(s1.pop())

    # Transfer Queue to Stack
    while not q1.isempty():
        s2.push(q1.dequeue())

    return s2




# Main program
s1 = Stack()

while True:
    n = int(input("Enter data (1 to stop): "))
    if n == 1:
        break
    s1.push(n)

print("Original Stack:")
s1.see()

s2 = reverse2(s1)

print("Reversed Stack:")
s2.see()