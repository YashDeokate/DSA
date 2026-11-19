class node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None
        
class priority:
    def __init__(self):
        self.front=self.rear=None
        
    def enqueue(self, new):
        if self.front.priority < new.priority:
            new.next=self.front
            self.front=new
            return
        else:
            prev=temp=self.front
            while temp:
                if new.priority > temp.priority:
                    
                else:
                    prev=temp
                    temp=temp.next
            prev.next=new   
            new.next=temp         
      