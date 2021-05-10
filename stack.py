# stack abstract data type
#
# 5/9/2021
# @author Jack Hangen
#
# follows last in first out (LIFO)s

class stack:

    datatype = "stack"

    def __init__ (self):
        self.stackWorking = []
        self.top = -1

    # adds a new item to the top of the stack. It needs the item and returns nothing.
    def push(self, item):
        self.stackWorking.append(item)
        self.top = self.top + 1


    # removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
    def pop(self):
        temp = self.stackWorking[self.top]
        self.stackWorking.pop(self.top)
        self.top = self.top - 1
        return temp
    
    # returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.
    def peek(self):
        return self.stackWorking[self.top]

    # tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
    def isEmpty(self):
        if size() == 0 :
            return True
        else:
            return False

    # returns the number of items on the stack. It needs no parameters and returns an integer.
    def size(self):
        return len(self.stackWorking)


# testing ADT
s = stack()
s.push('a')
s.push('b')
s.push('c')
s.push('d')
s.push('e')
print(s.size())
print(s.peek())
print(s.pop())
print(s.size())