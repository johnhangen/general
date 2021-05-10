class linkedList:

    dataType = "Linked List"

    def __init__(self, data, next):
        self.data = data
        self.next = next

    # getters and setters
    def getName(self):
        return self.data

    def getNext(self):
        return self.next

    def setName(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next     

