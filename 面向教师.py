

class teacher:
    __username = ""
    __age = 0

    # setXxxx用于对属性进行间接赋值
    def setAge(self,age):
        if age < 25 or age > 65:
            print("输入错误！")
        else:
            self.__age = age

    # getXxx用于对属性提取数据
    def getAge(self):
        return self.__age

    def setusername(self,username):
        if username != "":
            self.__username = username
        else:
            print("用户名不能为空！")

    def getUsername(self):
        return self.__username

    def rank(self,rankname ):
        print(self.__username,"职称为高级教师")

    def subject(self,subjectname):
        print (self.__username,"所教的科目为数学")

    def salary(self, salary):
        print (self.__username,"您的薪资为4500")



p = teacher()
p.setusername("蜡笔")  #  调用setXXXXA(data) 进行赋值
p.setAge(32)  # 调用setXXX（） 进行赋值

p.rank("高级教师")
p.subject("数学")
p.salary(45000)
