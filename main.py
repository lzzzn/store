'''
     入口程序去加载TestCalc.py
     并执行俩面的两个用例，最后生成一个界面的测试报告
     任务1：
        计算器的其他三个功能。
        自己实现邮件的发送模块，实现自动化执行用例并发送邮件。
    参数化测试：

'''
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


# 邮件发送模块












