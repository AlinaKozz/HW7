import unittest

from stack import Stack


class StackTest(unittest.TestCase):

    def test_push(self):
        stack = Stack()
        y = stack.push('1')
        self.assertEqual(y, ['1'])

    def test_push1(self):
        stack = Stack('1', '2', '3')
        y = stack.push('4')
        self.assertEqual(y, ['1', '2', '3', '4'])

    def test_pop(self):
        stack = Stack('1', '2', '3')
        y = stack.pop()
        self.assertEqual(y, '3')
    def test_size(self):
        stack = Stack('1', '2', '3')
        y = stack.size()
        self.assertEqual(y, 3)
    def test_back(self):
        stack = Stack('1', '2', '3')
        y = stack.back()
        self.assertEqual(y, '3')
    def test_clear(self):
        stack = Stack('1', '2', '3')
        x = stack.clear(answer='y')
        self.assertEqual(x, [])

if __name__ == '__main__':
    unittest.main()