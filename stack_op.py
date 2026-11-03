
class Stack:

    def __init__(self):
        self.stack = []

    # 1. Push
    def push(self, value):
        self.stack.append(value)
        print(value, "pushed into stack")

    # 2. Pop
    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow")
        else:
            print("Popped:", self.stack.pop())

    # 3. Display
    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Stack:", self.stack[::-1])

    # 4. Peek
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Top element:", self.stack[-1])

    # 5. Size
    def size(self):
        print("Size:", len(self.stack))

    # 6. Search
    def search(self, value):
        if value in self.stack:
            print("Element found at position:", self.stack.index(value))
        else:
            print("Element not found")

    # 7. Reverse String
    def reverse_string(self, string):
        temp = []

        for ch in string:
            temp.append(ch)

        result = ""

        while len(temp) > 0:
            result += temp.pop()

        print("Reversed string:", result)

    # 8. Reverse Stack using another Stack
    def reverse_stack(self):
        temp = []

        while len(self.stack) > 0:
            temp.append(self.stack.pop())

        self.stack = temp
        print("Stack reversed:", self.stack[::-1])

    # 9. Clear Stack
    def clear(self):
        self.stack.clear()
        print("Stack cleared")


s = Stack()

while True:
    print("\n--- STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Peek")
    print("5. Size")
    print("6. Search")
    print("7. Reverse String")
    print("8. Reverse Stack")
    print("9. Clear Stack")
    print("10. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        value = int(input("Enter value: "))
        s.push(value)

    elif ch == 2:
        s.pop()

    elif ch == 3:
        s.display()

    elif ch == 4:
        s.peek()

    elif ch == 5:
        s.size()

    elif ch == 6:
        value = int(input("Enter value to search: "))
        s.search(value)

    elif ch == 7:
        string = input("Enter string: ")
        s.reverse_string(string)

    elif ch == 8:
        s.reverse_stack()

    elif ch == 9:
        s.clear()

    elif ch == 10:
        break

    else:
        print("Invalid choice")
