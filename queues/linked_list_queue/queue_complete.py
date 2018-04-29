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
        if not self.is_full():                  # If the list is not full, then we can add the item
            node = Node(item)                   # We will make the new item into a node (for the linked list)
            self.list.append(node)              # We append the node to the list
            if self.num_items == 0:             # If there are no items in the list, set this as the head and tail
                self.head = node
                self.tail = node
                self.num_items += 1
                return True
            elif item > self.tail.data:         # If this item has a higher number than the tail (last item), then set it as the new tail
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
                self.num_items += 1
                return True
            else:
                current = self.head             # Otherwise, loop through the list
                while current is not None:      # If the current node is None, then we are at the end of the list
                    if current.data > item:     # If the item is less than the current node, then we should insert it before the current node
                        prev = current.prev
                        if prev is not None:    # Make sure that the previous node exists
                            prev.next = node
                        else:                   # If it doesn't, then the new node should be the head
                            self.head = node
                        current.prev = node
                        node.prev = prev
                        node.next = current
                        self.num_items += 1
                        return True
                    current = current.next      # Increment node
        else:
            return False                        # If the queue is full, then return false
    
    """
    Dequeues an item from the queue and returns it, raise IndexError if the queue is empty
    """
    def dequeue(self):
        if not self.num_items == 0:             # If the queue contains nodes, then it is possible to dequeue
            node = self.head
            if node.next is not None:           # If the head has a next node (size is greater than 1) then set the next node to the head
                next = node.next
                next.prev = None    
                self.head = next
                self.list.remove(node)          # Remove the node from the list
                self.num_items -= 1
                return node.data                # Return the node's data
            else:                               # If the head has no next node (size is 1) then set head and tail to None, as list is now empty
                self.head = None                
                self.tail = None
                self.list.remove(node)          # Remove the node from the list
                self.num_items -= 1             
                return node.data                # Return the node's data
        else:
            raise IndexError                    # If there are no items in the queue, raise an IndexError

    """
    Returns whether the queue is full or not
    """
    def is_full(self):
        return self.num_items == self.size      # If the number of items equals the size, then the queue is full

    """
    Returns all the data in the form of a list of data (not nodes)
    """
    def as_list(self):
        py_list = []                            # Initialize a list
        current = self.head                     # Start the node at the head
        while current is not None:              # Loop through the existing nodes
            py_list.append(current.data)        # Add the current node's data to the list
            current = current.next              # Increment the current node to it's next node
        return py_list                          # Return the new data list
