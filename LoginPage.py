# 只做页面的操作
class RegisterPage:

    def __init__(self,driver):
        self.driver = driver

    # 1.登陆的操作
    def register(self,username,name,password,password2,age,sex,email,phone,adress):
        #注册
        self.driver.find_element_by_xpath("//*[@class='eula']/a[1]").click()
        # 输入用户名
        self.driver.find_element_by_id("loginname").send_keys(username)
        #名字
        self.driver.find_element_by_name("username").send_keys(name)
        # 输入密码
        self.driver.find_element_by_id("pwd").send_keys(password)
        #再次输入密码
        self.driver.find_element_by_name("reloginpass").send_keys(password2)
        #下一步
        self.driver.find_element_by_name("next").click()
        #
        self.driver.find_element_by_id("valid_age").send_keys(age)
        self.driver.find_element_by_name("sex").send_keys(sex)
        self.driver.find_element_by_id("classname").click()
        self.driver.find_element_by_xpath("//*[@value='Python自动化']").click()
        self.driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/input[3]").click()

        self.driver.find_element_by_id("reg_mail").send_keys(email)
        self.driver.find_element_by_id("reg_phone").send_keys(phone)
        self.driver.find_element_by_name("address").send_keys(adress)
        self.driver.find_element_by_id("btn_reg").click()

        # 点击登陆
        self.driver.find_element_by_xpath("//*[@id='submit']").click()

    # 获取成功的数据信息
    def get_success_data(self):
        return self.driver.title

    # # 获取密码错误信息
    # def get_error_pwd_data(self):
    #     return self.driver.find_element_by_xpath("//*[@id='msg_uname']").text


