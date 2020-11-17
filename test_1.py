import unittest
import check
import xmlrunner
 
class CalcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(check.add(1, 2), 3)
        
    def test_sub(self):
        self.assertEqual(check.sub(4, 2), 2)
        
    def test_mul(self):
        self.assertEqual(check.mul(2, 5), 10)
        
    def test_div(self):
        self.assertEqual(check.div(8, 4), 2)
        
if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='D:\check\results.xml'))
    