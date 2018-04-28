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
        self.list = [None for i in range(self.size)]

    """
    returns whether the queue is full or not
    """
    def is_full(self):
       return self.num_items == self.size   #returns if the num items is equal to the size (queue is full)

    """
    Method will add a new items to the end of the queue
    
    return True if successful
    return False if not enough space in queue
    """
    def enqueue(self, item):
        if not self.is_full():              # only add to list if not full
            self.list[self.end] = item      # adds the item to the queue
            self.num_items += 1             # adds to the num_item count
            self.end += 1                   # increments the end 
            self.end %= self.size           # makes sure that the end is looping back to the front if too large. Alternate code below:
            """
            self.end += 1
            if self.end == self.size:
                self.end = 0
            """
            return True                     # returns True because item was added to queue
        else:
            return False                    # returns False because queue is full

    """
    Method will remove the first item from the queue and return it
    
    Raises an IndexError if no items are in the queue
    """
    def dequeue(self):
        if self.num_items == 0:             # If there are no items, raise an Index error
            raise IndexError                
        item = self.list[self.front]        # Get the item from the front of the queue
        self.list[self.front] = None        # Removes the item from the queue
        self.num_items -= 1                 # Decrements the num_item count
        self.front += 1                     # Increments the front variable
        self.front %= self.size             # Loops the front to the beginning if it overflows
        """
        self.front += 1
        if self.front == self.size:
            self.front = 0
        """
        return item                         # returns the item that was removed
