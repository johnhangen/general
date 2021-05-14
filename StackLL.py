# stack abstract data type
#
# 5/13/2021
# @author Jack Hangen
# Complete
# follows last in first out (LIFO)s, implimented with an linked list

class node():
    
    def __init__(self, data, next):
        self.data = data
        self.next = next
        
    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data
    
    def getNext(self):
        return self.next
        
    def setNext(self, next):
        self.next = next
        
class stack():
    
    def __init__(self):
        self.rear = node(None, None)
        self.front = node(None, self.rear)
        
    def addStack(self, value):
        self.front.setNext(node(value, self.front.getNext()))
    
    def removeStack(self):
        newNext = self.front.getNext().getNext()
        text = self.front.getNext().getData()
        self.front.setNext(newNext)
        return text
    
    def peek(self):
        return self.front.getNext().getData()
    
    def display(self):
        temp = self.front.getNext()
        string = ""
        while(temp.getNext() != None):
            string = (f"{string}{temp.getData()}")
            temp = temp.getNext()
            
        return string
        
s = stack()
s.addStack('a')
s.addStack('b')
s.addStack('c')
print(s.removeStack())
print(s.peek())
print(s.display())
