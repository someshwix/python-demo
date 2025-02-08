import unittest
import calc 
class CalcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(3,4), 7)
        self.assertEqual(calc.add(-1,-1), -2)
    def test_divide(self):
        self.assertEqual(calc.divide(8,4), 2)  
if __name__ == '__main__':
    unittest.main()
