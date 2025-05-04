# import unittest

# def add(x, y):
#     return x + y

# class TestMath(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(add(2, 3), 5)
#         self.assertEqual(add(-1, 1), 0)
#         self.assertAlmostEqual(add(0, 0), 0)
        

# if __name__ =="__main__":
#     unittest.main();




# import pdb

# def divide(a, b):
#     pdb.set_trace()
#     result = a/b
#     return result

# print(divide(10, 2))




# 2. 🔧 Common Assertions You Can Use:


# | Assertion Method          | Checks if...                     |
# | ------------------------- | -------------------------------- |
# | `assertEqual(a, b)`       | `a == b`                         |
# | `assertNotEqual(a, b)`    | `a != b`                         |
# | `assertTrue(x)`           | `bool(x) is True`                |
# | `assertFalse(x)`          | `bool(x) is False`               |
# | `assertIs(a, b)`          | `a is b` (same object)           |
# | `assertIsNone(x)`         | `x is None`                      |
# | `assertIn(a, b)`          | `a in b`                         |
# | `assertRaises(Exception)` | checks if an exception is raised |


def add(a, b):
    return a + b

def divide(a, b):
    return a / b


import unittest


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(1, -1), 0)
    
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
            
if __name__ == "__main__":
    unittest.main()