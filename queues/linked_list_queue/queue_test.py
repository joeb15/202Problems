#!/usr/bin/python3

import unittest
from queue import *

class Test_Linked_Queue(unittest.TestCase):
    
    def test_complete(self):
        queue = Linked_Queue(3)
    
        self.assertTrue(queue.enqueue(5))    
        self.assertFalse(queue.is_full())
        self.assertTrue(queue.enqueue(4))
        self.assertTrue(queue.enqueue(6))
        self.assertFalse(queue.enqueue(3))
        self.assertEqual(queue.as_list(), [4, 5, 6])
        self.assertTrue(queue.is_full())
        self.assertEqual(queue.dequeue(), 4)
        self.assertEqual(queue.dequeue(), 5)
        self.assertEqual(queue.dequeue(), 6)
        with self.assertRaises(IndexError):
            queue.dequeue()

    def test_enqueue(self):
        queue = Linked_Queue(3)
        self.assertTrue(queue.enqueue(4))
        self.assertTrue(queue.enqueue(5))
        self.assertTrue(queue.enqueue(2))
        self.assertFalse(queue.enqueue(6))
    
    def test_dequeue(self):
        queue = Linked_Queue(2)
        with self.assertRaises(IndexError):
            queue.dequeue()
        queue.enqueue(5)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 5)

    def test_list(self):
        queue = Linked_Queue(5)
        queue.enqueue(5)
        self.assertEqual(queue.as_list(), [5])
        queue.enqueue(3)
        self.assertEqual(queue.as_list(), [3, 5])
        queue.enqueue(6)
        self.assertEqual(queue.as_list(), [3, 5, 6])

if __name__ == "__main__":
    unittest.main()
