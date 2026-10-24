# stack operations : push, pop, reverse

class node: 
    def __init__(self,value):
        self.data=value
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    def isempty(self):
        return self.top is None
    
    def push(self,new_node):
        new_node.next=self.top
        self.top=new_node
        
    def print(self):
        if self.isempty():
            print("stack is empty")    
        else:
            print ("stack contains...")    
            temp=self.top
            while temp:
                print(temp.data)
                temp=temp.next
                
    def pop(self):
        if self.isempty():
            print("stack is empty")  
        else:
            temp=self.top
            print("popped element:",temp.data)
            self.top=self.top.next
            temp=None     
            
    def reverse(self):
        temp=self.top
        while temp:
            st1.push(node(temp.data))                 
            temp=temp.next       
            
st=stack()
st1=stack()
st.push(node(10))                
st.push(node(20))                
st.push(node(30))                
st.push(node(40))                
st.push(node(50))
st.print()
st.pop()
st.print() 
st.reverse()
st1.print()               