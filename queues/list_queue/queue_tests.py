import unittest
from queue import *

class TestListQueue(unittest.TestCase):
    
    def test_full_functionality(self):
        queue = List_Queue(3)

        self.assertTrue(queue.enqueue(3))
        self.assertTrue(queue.enqueue(2))
        self.assertTrue(queue.enqueue(7))
        
        self.assertTrue(queue.is_full())
        
        self.assertFalse(queue.enqueue(4))
        self.assertEqual(queue.dequeue(), 3)
        
        self.assertFalse(queue.is_full())
        self.assertTrue(queue.enqueue(1))
        self.assertTrue(queue.is_full())
        
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 7)
        self.assertEqual(queue.dequeue(), 1)
        
        with self.assertRaises(IndexError):
            queue.dequeue()

    def test_enqueue(self):
        queue = List_Queue(2)
        self.assertTrue(queue.enqueue(1))
        self.assertTrue(queue.enqueue(4))
        self.assertFalse(queue.enqueue(0))
    
    def test_dequeue(self):
        queue = List_Queue(2)
        with self.assertRaises(IndexError):
            queue.dequeue()
        queue.enqueue(1)
        self.assertEqual(queue.dequeue(), 1)

if __name__ == "__main__":
    unittest.main()
