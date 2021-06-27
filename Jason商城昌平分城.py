'''
    Jason的商城：
        1.准备商品
        2.空的购物车
        3.钱包初始化金钱
        4.最后打印购物小条
    1.业务：
        看到商品：
            商品存在
                看金钱够：
                    成功加入购物车。
                    余额减去对应价格。
                不够：
                    穷鬼，去买其他商品。
            商品不存在：
                输入错误。
            输入Q或q，退出并结算。打印小条。
    任务：尽量多的添加商品
    任务：10辣条优惠券（0.3），20机械革命优惠券（0.9）。
        在进入商城时，随机抽取优惠券，在最后结算使用改优惠券。
'''

# 1.商品

quans = ["三折券","九折券"]
import random
index = random.randint(0,len(quans)-1)
print ("恭喜您抽中",quans[index])

shop = [
    ["机械革命",15000],
    ["HUAWEI watch",1200],
    ["MAC PC",13000],
    ["Iphone 54 plus",45000],
    ["辣条",2.5],
    ["老干妈",13]
]



# 2.初始化您的余额
money = input("请输入您的钱包余额:")
money = int(money)



# 3.准备一个空的购物车
mycart = []

# 买东西

while True:
    # 展示商品

    for index,value in enumerate(shop): # 枚举，将角标和商品整体都打印
        print(index,"  ",value)
    # 请输入您要的商品
    chose = input("请输入您要的商品：")

    # 看是否存在
    if chose.isdigit():  # 是否能被看成数字：
        chose = int(chose)
        # 看商品是否存在
        if chose > len(shop) - 1:
            print("您要的商品不存在！")
        else:
            if shop[chose][0] == "机械革命":
                mycart.append(shop[chose])
                money = money - shop[chose][1]*0.9
                print("恭喜，成功添加购物车，您的余额还剩：￥", money)
            elif shop[chose][0] == "辣条":
                mycart.append(shop[chose])
                money = money - shop[chose][1] * 0.3
                print("恭喜，成功添加购物车，您的余额还剩：￥", money)
            else:
                if money > shop[chose][1]:
                    mycart.append(shop[chose])
                    # 钱减去
                    money = money - shop[chose][1]
                    print("恭喜，成功添加购物车，您的余额还剩：￥", money)
                else:
                    print("对不起，穷鬼，余额不足，请到商城去购买！")
    elif chose == 'q' or chose == 'Q':
        print("欢迎下次光临！")
        break
    else:
        print("对不起，您的输入商品不存在！别瞎弄!")

        # 打印小票
print("下面是您的购物小条，请拿好：")
for index, value in enumerate(mycart):
    print(index, "   ", value)
print("您的钱包还剩：￥", money)


















