# #Q. 1 Create a Stack with following operaƟons
# # 1. Push 
# # 2. Pop 
# # 3. Display 
# # 4. Reverse String using Stack 
# # 5. Reverse Stack using another Stack 


class Stack: 
    def __init__(self): 
        self.stack = [] 
    
    def push(self, value): 
        self.stack.append(value) 
        print(value, "pushed into stack") 
    
    def pop(self): 
        if len(self.stack) == 0: 
            print("Stack is empty") 
        else: 
            print("Popped:", self.stack.pop())
    
    def display(self): 
        if len(self.stack) == 0: 
            print("Stack is empty ") 
        else: 
            print("Stack: ", self.stack) 
    
    def reverse_string(self, string): 
        s = [] 
        for ch in string: 
            s.append(ch) 
        result = "" 
        while s: 
            result += s.pop() 
        print("Reversed string:", result) 

    def reverse_stack(self): 
        temp = [] 
        while self.stack: 
            temp.append(self.stack.pop()) 
        self.stack = temp 
        print("Stack reversed") 
s = Stack() 
s.push(10) 
s.push(20) 
s.push(30) 
s.push(40)
s.display() 
s.pop() 
s.display() 
s.reverse_string("PYTHON") 
s.reverse_stack() 
s.display() 

# # Q. 2 Write a program to perform the following operaƟons on a Linear
# # Queue 
# # 1. Enqueue an element into the queue 
# # 2. Dequeue an element from the queue 
# # 3. Display 
# # 4. Reverse the queue using stack 
# # 5. Merge two queues into one. 
# # 6. Check if two queues are identical
class Queue:
    def __init__(self):
        self.queue = []

    # 1. Enqueue
    def enqueue(self, value):
        self.queue.append(value)
        print(value, "inserted into queue")

    # 2. Dequeue
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Deleted:", self.queue.pop(0))

    # 3. Display
    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Queue:", self.queue)

    # 4. Reverse Queue using Stack
    def reverse_queue(self):
        stack = []

        while self.queue:
            stack.append(self.queue.pop(0))

        while stack:
            self.queue.append(stack.pop())

        print("Queue reversed")

    # 5. Merge Two Queues
    def merge(self, q2):
        self.queue.extend(q2.queue)
        print("Queues merged")

    # 6. Check Identical Queues
    def identical(self, q2):
        if self.queue == q2.queue:
            print("Queues are identical")
        else:
            print("Queues are not identical")


# Creating objects
q1 = Queue()
q2 = Queue()

# Enqueue
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)

q2.enqueue(40)
q2.enqueue(50)

# Display
q1.display()
q2.display()

# Dequeue
q1.dequeue()
q1.display()

# Reverse
q1.reverse_queue()
q1.display()

# Merge
q1.merge(q2)
q1.display()

# Identical
q1.identical(q2)