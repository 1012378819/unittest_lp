#author:lup
#-*-coding:utf-8-*-
import unittest

class TestAssert(unittest.TestCase):
    def setUp(self):
        num=input("pls input a number:")
        self.num=num
    def TestAssert(self):
        self.assertEquals(self.num,10,'your input is not 10')
    def tearDown(self):
        pass
if __name__=='__main__':
    unittest.main()