#!/usr/bin/python3

import unittest
from stack import *

class Test_Stack(unittest.TestCase):
    
    def test_push(self):
        stack = Stack(2)
        self.assertTrue(stack.push(3))
        self.assertTrue(stack.push(2))
        self.assertFalse(stack.push(4))

    def test_pop(self):
        stack = Stack(2)
        stack.push(3)
        self.assertEqual(3, stack.pop())
        with self.assertRaises(IndexError):
            stack.pop()

    def test_peek(self):
        stack = Stack(3)
        with self.assertRaises(IndexError):
            stack.peek()
        stack.push(4)
        stack.push(2)
        self.assertEqual(2, stack.peek())
        self.assertEqual(2, stack.peek())
       
    def test_empty(self):
        stack = Stack(2)
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertFalse(stack.is_empty())

    def test_full(self):
        stack = Stack(2)
        self.assertFalse(stack.is_full())
        stack.push(1) 
        stack.push(2)
        self.assertTrue(stack.is_full()) 

if __name__ == "__main__":
    unittest.main() 
