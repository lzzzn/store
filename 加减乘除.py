from unittest import  TestCase
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

class Calc:
    def add(self,a,b):
        return a + b

    def minus(self,a,b):
        return a - b

    def multi(self,a,b):
        return a * b

    def devision(self,a,b):
        return a / b

from HTMLTestRunner import HTMLTestRunner  # 联网安装一下模块HTMLTestRunner-python3
import unittest

# 加载所有测试用例
tests = unittest.defaultTestLoader.discover(
    r"C:\Users\Administrator\PycharmProjects\pythonProject\venv\day13",pattern="Test*.py")

# 创建一个测试运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title="计算器的测试报告",
    description="这是加法测试结果",
    verbosity=1,
    stream = open("计算器测试报告.html",mode="w+",encoding="utf-8")
)
# 让运行器去执行所有测试用例，并得出测试报告
runner.run(tests)