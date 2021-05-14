# queue abstract data type
#
# 5/12/2021
# @author Jack Hangen
# Incomplete
# follows first in first out (FIFO)s, implimented with linked list

class node():

    def __init__(self, data, next_data):
        self.data = data
        self.next = next_data

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next

    def setData(self, data):
        self.data = data


class queue():
    
    def __init__ (self):
        self.rear = node(None, None)        
        self.front = node(None, self.rear)
        

    # adds it tot the top of the queue
    def enQueue(self, value):
        if(self.rear.getData() == None):
            self.rear.setData(value)
        else:
            temp = self.front.getNext()
            self.front.setNext(node(value, None))
            self.front.getNext().setNext(temp)
            
    
    # removes the bottom element and returns it
    def deQueue(self):
        # unable to do it at this time
        pass

    # returns the bottom element
    def peek(self):
        temp = self.front
        while(temp.getNext() != self.rear):
            temp = temp.getNext()
        temp = temp.getNext()
        return temp.getData()

    # prints the queue
    def display(self):
        temp = self.front.getNext()
        string = ""
        while(temp.getNext() != None):
            string = (f"{temp.getData()}{string}")
            temp = temp.getNext()

        string = (f"{temp.getData()}{string}")
        return string


# Testing the queue
q = queue()
q.enQueue('a')
q.enQueue('b')
q.enQueue('c')
print(q.peek())
print(q.display())