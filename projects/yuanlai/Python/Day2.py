# Alex落地
# hight = 100  # 原始高度
# distance = 0  # 和
#
# for i in range(10):
#     # 将下落高度加入到总和中
#     distance = distance + hight  # distance += hight
#     if i == 9:
#         break
#     # 计算反弹高度
#     hight = hight / 2  # hight /= 2
#     # 将计算好的反弹高度加入到总和中
#     distance += hight
#
# print(f"共经历了{distance}米")


# # 九九乘法表
# sum = 0  # 计数
# for i in range(1, 10):
#     for j in range(1, i+1):
#         sum += 1
#         print(f"{j}*{i}={j * i}", end="\t")
#     print()
# print(sum)


# 年会抽奖
import random  # 随机数

staff_list = []
for i in range(1, 301):
    staff_list.append(f"员工{i}")

level = [30, 6, 3]

for j in range(3):
    winnerList = random.sample(staff_list, level[j])

    for winner in winnerList:
        staff_list.remove(winner)

    print(f"获得{3 - j}等奖的是：{winnerList}")
    print(f"还剩{len(staff_list)}个人未中奖")

# # 三等奖
# winnerList3 = random.sample(staff_list, 30)
# print(winnerList3)
#
# # 二等奖
# winnerList2 = random.sample(staff_list, 6)
# print(winnerList2)
#
# # 一等奖
# winnerList1 = random.sample(staff_list, 3)
# print(winnerList1)
