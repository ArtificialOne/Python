##Flask = Micro-framework, minimal to no dependence on external libraries
##AssertEqual compares two values and determines if equal (actual, expected)

import unittest
from python_learn3 import func_cubed, func_square

class TestMyModule(unittest.TestCase):
   def test_func_square(self):
      self.assertEqual(func_square(2), 4)
      self.assertEqual(func_square(3.0), 9.0)
      self.assertNotEqual(func_square(-3), -9)
    
class TestMyModule2(unittest.TestCase):
   def test_func_cubed(self):
      self.assertEqual(func_cubed(5), 125)
      self.assertEqual(func_cubed(3.0), 27.0)
      self.assertNotEqual(func_cubed(-3), -9)

if __name__ == "__main__":
    unittest.main()