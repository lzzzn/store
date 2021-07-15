file = open(file="file\\baidu_x_system.log",mode="r+",encoding="utf-8")

data = file.readlines()

list1 = []

for da in data:
    li = da.split(" ")
    list1.append(li[0])

for index,value in enumerate(list1):
    if value in list1[:index]:
        continue
    else:
        print(value,"共出现了",list1.count(value),"次！")



