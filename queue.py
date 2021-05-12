# queue abstract data type
#
# 5/12/2021
# @author Jack Hangen
# Complete
# follows first in first out (FIFO)s

class queue():
    
    def __init__ (self):
        self.array = []
        self.bottom = 0

    # adds it tot the top of the queue
    def enQueue(self, value):
        self.array.append(value)
    
    # removes the bottom element and returns it
    def deQueue(self):
        self.bottom += 1
        return self.array[self.bottom - 1]

    # prints the queue
    def display(self):
        string = ""
        for i in range(self.bottom, len(self.array)):
            string = (f"{string}{self.array[i]}")

        return string

# Testing the queue
q = queue()
q.enQueue('a')
q.enQueue('b')
q.enQueue('c')
q.deQueue()
print(q.display())