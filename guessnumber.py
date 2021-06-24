import random
num = random.randint(0,100)
count = 0
i = 0
while i <=10:
    coin = 5000
    count =  count + 1
    a = input("请输入您要猜的数字：")
    a = int(a)
    if a > num:
        print("大了！")
        coin = coin - 100
        print ("本次扣除您100金币")
    elif a < num:
        print("小了！")
        coin = coin - 100
        print("本次扣除您100金币")
        i = i + 1
    else:
        print("恭喜你，猜中了！您本次猜了",count,"次！","奖励您500金币")
        break
