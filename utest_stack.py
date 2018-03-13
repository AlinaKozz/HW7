import unittest
import stack


class StackTest(unittest.TestCase):

    def test_push(self):
        stack_list = []
        y = stack.push(stack_list, '1')
        self.assertEqual(y, ['1'])
    def test_push1(self):
        stack_list = ['1', '2', '3']
        y = stack.push(stack_list, '4')
        self.assertEqual(y, ['1', '2', '3', '4'])
    def test_pop(self):
        stack_list = ['1', '2', '3']
        y = stack.pop(stack_list)
        self.assertEqual(y, ['1', '2'])
    def test_size(self):
        stack_list = ['1', '2', '3']
        y = stack.size(stack_list)
        self.assertEqual(y, 3)
    def test_back(self):
        stack_list = ['1', '2', '3']
        y = stack.back(stack_list[-1])
        self.assertEqual(y, '3')
    def test_clear(self):
        stack_list = ['1', '2', '3']
        x = stack.clear(stack_list, answer='y')
        self.assertEqual(x, [])

if __name__ == '__main__':
    unittest.main()