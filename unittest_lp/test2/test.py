#author:lup
#-*-coding:utf-8-*-
import unittest
from calc import Count

class TestCount(unittest.TestCase):
    def setUp(self):
        print 'test start'

    def Test_add(self):
        j=Count(2,3)
        self.assertEqual(j.add(),5,'aaa')

    def tearDown(self):
        print 'test end'

if __name__=='__main__':
    unittest.main()