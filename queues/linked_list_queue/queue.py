#!/usr/bin/python3

"""
A node to be used in a linked list
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

"""
A class to represent the linked list queue
"""
class Linked_Queue:
    def __init__(self, size):
        self.size = size
        self.list = []
        self.head = None
        self.tail = None
        self.num_items = 0

    """
    Enqueues the items to the array and returns if it is successful
    """
    def enqueue(self, item):
        
    
    """
    Dequeues an item from the queue and returns it, raise IndexError if the queue is empty
    """
    def dequeue(self):
        

    """
    Returns whether the queue is full or not
    """
    def is_full(self):
        

    """
    Returns all the data in the form of a list of data (not nodes)
    """
    def as_list(self):
        
