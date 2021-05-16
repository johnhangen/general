# binary tree
#
# 5/16/2021
# @author Jack Hangen
# Incomplete
# node implmitation of a binary tree

class tree_node():

    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def get_data(self):
        return self.data 
    
    def get_left(self):
        return self.left

    def get_right(self): 
        return self.right

    def set_data(self, data):
        self.data = data

    def set_left(self, data):
        self.left = data

    def set_right(self, data):
        self.right = data

    def return_all(self):
        return(self.data, self.left, self.right)

