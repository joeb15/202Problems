#!/usr/bin/python3

"""

A queue is a first-in first-out type of data structure
For this to work, you must be able to enqueue (add) items to the queue, dequeue (remove) items from the queue

"""

class List_Queue:
    def __init__(self, size):
        self.size = size
        self.num_items = 0
        self.front = 0
        self.end = 0
        self.list = []

    """
    returns whether the queue is full or not
    """
    def is_full(self):
        

    """
    Method will add a new items to the end of the queue
    
    return True if successful
    return False if not enough space in queue
    """
    def enqueue(self, item):
        

    """
    Method will remove the first item from the queue and return it
    
    Raises an IndexError if no items are in the queue
    """
    def dequeue(self):
        
