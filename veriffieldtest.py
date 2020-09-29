#verrifieldtest.py
from 3224849unit test import veriffield
import unittest

class Testverrifieldtest(unittest.TestCase):
    def setUp(self):
        self.rec = Rectangle(3,4)

    def testGetWidth(self):
        self.assertEqual(self.rec.getWidth(),3)

    def testGetHeight(self):
        self.assertEqual(self.rec.getHeight(),4)

    def testGetArea(self):
        self.assertEqual(self.rec.getArea(),12)

    def testSetWidth(self):
            #first show that the width is 3 
        self.assertEqual(self.rec.getWidth(),3)
            # now change that value to 10
        self.rec.setWidth(10)
            # and now show that the value has been changed
        self.assertEqual(self.rec.getWidth(),10)

    def testSetHeight(self):
            #first show that the width is 4 
        self.assertEqual(self.rec.getHeight(),4)
            # now change that value to 7
        self.rec.setHeight(7)
            # and now show that the value has been changed
        self.assertEqual(self.rec.getHeight(),7)

    def testIsLarger(self):
        other = Rectangle(2,7)
        self.assertFalse(self.rec.isLarger(other))
        self.assertTrue(other.isLarger(self.rec))

    def testIsEqual(self):
        self.assertTrue(self.rec.isEqual(Rectangle(3,4)))
        self.assertTrue(self.rec.isEqual(Rectangle(4,3)))
        self.assertFalse(self.rec.isEqual(Rectangle(3,5)))
        self.assertFalse(self.rec.isEqual(Rectangle(5,4)))
        
                        
        


if __name__ == '__main__':
    unittest.main()   


