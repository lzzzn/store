'''
    1. 测试类要继承unittest.TestCase，
    2. 写测试用例,testXxxxxx
    3.生成测试报告
        HTMLTestRunner
'''

from unittest import  TestCase
from Calc import Calc
class TestCalc(TestCase):

    def testAdd1(self):
        a = 6
        b = 9
        c = 15

        calc = Calc()
        sum = calc.add(a,b)

        # 断言
        self.assertEqual(c,sum)

    def testminus(self):
        a = 9
        b = 6
        c = 3

        calc = Calc()
        sum = calc.minus(a,b)

    def testmulti(self):
        a = 6
        b = 9
        c = 54

        calc = Calc()
        sum = calc.multi(a, b)

        # 断言
        self.assertEqual(c, sum)

    def testdevision(self):
        a = 9
        b = 3
        c = 3

        calc = Calc()
        sum = calc.devision(a, b)
        # 断言
        self.assertEqual(c,sum)












