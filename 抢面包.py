'''
    5个人同时抢500张票
    同时：
        意味着：500同时对5个人开放。
        5个人有同时抢票的资格
            5个人实现多线程
            任务：抢票

'''
mianbao = 500
from threading import Thread
import time


class User(Thread):
    customer = ""  # 用户名
    count = 0  # 抢票计数器
    money = 30

    # 任务
    def run(self) -> None:
        global mianbao  # 将全局变量在方法里也能使用
        while True:
            if mianbao >= 1:
                self.count = self.count + 1
                mianbao = mianbao - 1
                self.money = self.money - 3
                print(self.customer, "成功抢了一个面包！，还剩", mianbao, "个面包!")
                print(self.customer,"您还剩",self.money,"元")
                # time.sleep(0.05)
            elif mianbao == 0:
                print(self.customer, "请稍等")
                time.sleep(3)

            if self.money < 3:
                print("对不起，你的钱不够！")
                print (mianbao)
                break


class Sell(Thread):
    username = "" # 用户名
    count = 0 # 抢票计数器
    # 任务
    def run(self) -> None:
        global mianbao # 将全局变量在方法里也能使用
        while True:

            if mianbao == 500:
                print(self.username,"篮子已满，请等待三秒")
                time.sleep(3)
                break
            elif mianbao > 0 and mianbao < 500:
                self.count = self.count + 1
                mianbao = mianbao + 1
                print(self.username, "篮子里已经有", mianbao, "个!")
                print (mianbao)
u1 = Sell()
u2 = Sell()
u3 = Sell()


u1.username = "tt"
u2.username = "xx"
u3.username = "zz"

u1.start()
u2.start()
u3.start()




c1 = User()
c2 = User()
c3 = User()
c4 = User()
c5 = User()
c1.customer = "安宁"
c2.customer = "赵丽蓉"
c3.customer = "任继超"
c4.customer = "张海燕"
c5.customer = "孙健"
c1.start()
c2.start()
c3.start()
c4.start()
c5.start()

'''
if mianbao < 500:
    self.count = self.count + 1
    mianbao = mianbao + 1
    print(self.username, "篮子里已经有", mianbao, "个!")
    # time.sleep(0.05)
'''


