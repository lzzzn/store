import unittest
from ddt import ddt
from ddt import data
from ddt import unpack
from Initpage import InitPage
from LoginPage import RegisterPage
from selenium import webdriver
import time

# 用例 ： 整合页面的操作和调用页面的数据
@ddt
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:  # 在每个用例执行前
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/HKR")
        self.driver.maximize_window()
        #self.driver.find_element_by_xpath("//*[@class='eula']/a[1]").click()

    def tearDown(self) -> None: # 在每个用例执行完后执行
        time.sleep(2)
        #self.driver.quit()


    # 登陆成功用例
    @data(*InitPage.Register_success_data)
    def testRegisterSuccess(self,testdata):
        #1.提取用户名和密码和期望数据
        username = testdata["username"]
        name = testdata["name"]
        password = testdata["password"]
        password2 = testdata["password2"]
        age = testdata["age"]
        sex = testdata["sex"]
        email = testdata["email"]
        phone = testdata["phone"]
        adress = testdata["adress"]
        expect = testdata["expect"]

        # 创建页面的对象，并把driver传给他
        Register = RegisterPage(self.driver)
        # 2.登陆
        Register.register(username,name,password,password2,age,sex,email,phone,adress)

        # 3.提取成功的实际结果
        result = Register.get_success_data()

        # 4.断言
        self.assertEqual(expect,result)
