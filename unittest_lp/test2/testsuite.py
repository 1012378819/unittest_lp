#author:lup
#-*-coding:utf-8-*-
from calc import Count
import unittest

class TestAdd(unittest.TestCase):
    def setUp(self):
        print 'test add start'

    def test_add(self):
        j=Count(2,3)
        self.assertEqual(j.add(),5)

    def test_add2(self):
        j=Count(4,6)
        self.assertEqual(j.add(),10)

    def tearDown(self):
        print 'test add end'

# TextTestRunner 是来执行测试用例的，其中的 run(test)用来执行 TestSuite/TestCase。测
# 试的结果会保存到 TextTestResult 实例中，包括运行了多少个测试用例，成功了多少、失败
# 了多少等信息
class TestSub(unittest.TestCase):
    def setUp(self):
        print 'test sub start'

    def test_sub(self):
        j=Count(2,3)
        self.assertEqual(j.sub(),-1)

    def test_sub2(self):
        j=Count(14,8)
        self.assertEqual(j.sub(),6)

    def tearDown(self):
        print 'test sub end'

if __name__=='__main__':
    #使用测试套，往套里增加的才执行
    # 构造测试集
    suite=unittest.TestSuite()
    suite.addTest(TestAdd("test_add"))
    # suite.addTest(TestAdd("test_add2"))
    suite.addTest(TestSub("test_sub"))
    suite.addTest(TestSub("test_sub2"))
    runner=unittest.TextTestRunner()
    runner.run(suite)

    #执行所有case
    # 执行测试
    # unittest.main()
