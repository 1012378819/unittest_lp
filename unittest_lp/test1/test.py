#author:lup
#-*-coding:utf-8-*-
from unittest_lp.test2.calc import Count

class TestCount(object):
    def test_add(self):
        try:
            j=Count(2,4)
            add=j.add()
            assert (add==6),'result error!'
        except AssertionError,msg:
            print 'msg:',msg
        else:
            print 'test pass!'

mytest=TestCount()
mytest.test_add()