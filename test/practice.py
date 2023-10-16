# for x in range(1, 6):
#     if x == 4: continue
#     for y in range(1, 10):
#         if y == 4: continue
#         print(f"{x} 0 {y}", end='\t')
#     print()



# def set_floor(floors, rooms, isFourIncluded = True):
#     levels = floors + 2 if not isFourIncluded else floors + 1
#     dorms = rooms + 2 if not isFourIncluded else rooms + 1

#     for x in range(1, levels):
#         if not isFourIncluded and x == 4: continue
#         for y in range(1, dorms):
#             if not isFourIncluded and y == 4: continue
#             print("%02d-%02d" % (x,y), end='\t')
#         print()


# # set_floor(5, 8)
# set_floor(9, 12, False)
# # set_floor(8, 8, False)

# def sumEven(number):
#     s = 1
#     for x in range(1, number+1, 2):
#         # s = s + x
#         s *= x
#     return s

# number = int(input('Please input a number: '))
# print(sumEven(number))



# s = 0
# high = 100

# for x in range(1, 11):
#     s += high

#     if x != 10:
#         # calculate the half height
#         high /= 2
#         s += high


# print(s)



# for i in range (1, 10):
#     for k in range(1, 48 - i * 5):
#         print(' ', end = '')
#     for j in range (1, i + 1):
#         # print(f'{j} * {i} = {i * j}', end = '\t')
#         print(f'{j} * {i} = {i * j} ', end = '')
#     print()



data = [5,8,4,1]
#实现冒泡排序
for i in range(len(data)-1):
    for j in range(len(data)-i-1):
        if(data[j]>data[j+1]):
            data[j],data[j+1] = data[j+1],data[j]

print("排序后：",data)



