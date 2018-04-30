#!/usr/bin/python3

"""
A class to represent a stack (last in, first out data type)
"""
class Stack:
    def __init__(self, size):
        self.num_items = 0
        self.size = size
        self.list = []
    
    """
    Pushes an item to the end of the stack, returns True if possible, or False if full
    """
    def push(self, item):
        if self.is_full():                  # If the stack is full, return False
            return False
        else:                               # If the stack is not full the add the item and return true
            self.list.append(item)      
            self.num_items += 1
            return True
    
    """
    Removes and returns the last item on the stack, raises an IndexError if there are no items
    """
    def pop(self):
        if self.is_empty():                 # If the stack is empty, raise an IndexError
            raise IndexError
        item = self.list[-1]                # Get the last item from the stack
        del self.list[-1]                   # Delete the last item from the stack
        self.num_items -= 1                 # Decrement the number of items counter
        return item                         # Returns the item that was deleted
    
    """
    Returns the last element on the stack without removing it, raises an IndexError if there are no items
    """
    def peek(self):
        if self.is_empty():                 # If the stack is empty, raise an IndexError
            raise IndexError
        return self.list[-1]                # Returns the last item from the stack

    """
    Returns if the stack is empty
    """
    def is_empty(self):
        return self.num_items == 0          # If the number of items in the stack is zero, it is empty
    
    """
    Returns if the stack is full
    """
    def is_full(self):                      
        return self.num_items == self.size  # If the number of items in the stack is equal to its max size, then it is full
    
