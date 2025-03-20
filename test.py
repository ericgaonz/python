# name = input('Please input your name: ')
# age = input('piease input your age: ')


# print(name, age)



# pi = 3.1415926
# r = float(input('please input the radius: '))

# p = 2 * pi * r

# print('the perimeter of the circle with radius is: ', p)



# w = float(input('piease input your w: '))
# a = w * w 
# print('a = ', a)


# w = float(input('piease input your w: '))
# l = w * 4 
# print('l = ',l)


# a = float(input('a= '))
# b = float(input('b= '))

# v = a * b 
# l = (a + b) * 2
# print('area: ', v)
# print('Length: ', l)



# d = float(input('d= '))
# h = float(input('h= '))

# s = 0.5 * d * h 
# print('s= ',s)


# r = float(input('r= '))
# h = float(input('h= '))

# pi = 3.1415926
# t = (pi * r * r) * h
# print('t= ',t)


# r = float(input('r= '))
# h = float(input('h= '))

# pi = 3.1415926
# s = pi * r * r
# z = 2 * pi * r

# t = s * 2 + z * h
# print('t= ', t)




# #将 78 赋值给变量 n
# n = 78
# print(n)
# print( type(n) )

# #给x赋值一个很大的整数
# x = 8888888888888888888888
# print(x)
# print( type(x) )

# #给y赋值一个很小的整数
# y = -7777777777777777777777
# print(y)
# print( type(y) )


# str1 = 'I\'m a great" coder!'
# str2 = "引文双引号是\"，中文双引号是“"
# print(str1)
# print(str2)


# x = "123454321"
# print(x)

# b5 = "千惠是个小笨蛋".encode('UTF-8')
# print("b5: ", b5)

# str = b5.decode('UTF-8')
# print("str: ", str)




# a = float(input("Enter a number: "))
# b = float(input("Enter another number: "))
# print("aType: ", type(a))
# print("bType: ", type(b))

# result = a + b
# print("resultValue: ", result)
# print("resultType: ", type(result))




# a = float(input("enter 1st number: "))
# b = float(input("enter 2nd number: "))
# c = float(input("enter 3rd number: "))

# avg = (a + b + c) / 3

# # print('(',a,'+',b,'+',c,') / 3 =',avg)
# print('(%f + %f + %f) / 3 = %f' % (a,b,c,avg))


# name = "高千惠"
# age = 12
# url = "Raroa"
# print("%s已经%d岁了, 它的学校是%s。" % (url, age, name))

# a = 2

# a += 1 # a = a + 1
# a += 2
# a += 5

# a -= 4

# a *= 4
# a /= 8

# a += 52

# a %= 8  # a = a % 8


# a **= 5 # 2*2*2*2*2

# 6/12 - 3/24 = 12/24 - 3/24 = 9/24 = 3/8



# a = 36

# # a %= 5    # a = a % 5
# #a //= 5    # a = a // 5


# a <<= 2

# print(a)


# a = 666666
# b = 666666
# print(a == b)



# age = int(input("pleas input the age: "))

# if age >= 18:
#     print('It is a legal age to drink wine.')
# elif age >= 13:
#     print('you can make boy friends.')
# elif age >= 6:
#     print('你则会帮家长的朋友带小孩')
# else:
#     print('You are stupid.')


# total = int(input("请放入分数： "))


# if total >= 95: 
#     print('你会被家长夸。')
# elif total >= 80:        
#     print('你不会被夸。')
# elif total >= 70:
#     print('你会被骂。')
# else:
#     print('你会被狂轰乱炸。')


# x = int(input("Please enter an integer: "))

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')



# age = int( input("请输入你的年龄：") )
# if age < 18 :
#     print("你还未成年，建议在家人陪同下使用该软件！")
#     print("如果你已经得到了家长的同意，请忽略以上提示。")

# #该语句不属于if的代码块
# print("软件正在使用中...")





# import sys

# age = int( input("请输入你的年龄：") )
# if age < 18 :
#     print("警告：你还未成年，不能使用该软件！")
#     print("未成年人应该好好学习，读个好大学，报效祖国。")
#     sys.exit()
# else:
#     print("你已经成年，可以使用该软件。")
#     print("时间宝贵，请不要在该软件上浪费太多时间。")

# print("软件正在使用中...")




# height = float(input("输入身高（米）："))
# weight = float(input("输入体重（千克）："))
# bmi = weight / (height * height)  #计算BMI指数

# if bmi < 18.5:
#     print("BMI指数为："+str(bmi))
#     print("体重过轻")
# elif bmi >= 18.5 and bmi < 24.9:
#     print("BMI指数为："+str(bmi))
#     print("正常范围，注意保持")
# elif bmi >= 24.9 and bmi < 29.9:
#     print("BMI指数为："+str(bmi))
#     print("体重过重")
# else:
#     print("BMI指数为："+str(bmi))
#     print("肥胖")

# age = 17
# print(age < 18)

# b = True
# if b:
#     print('b是True')
# else:
#     print('b是False')


# n = 4
# if n:
#     print('n不是零值')
# else:
#     print('n是零值')


# s = ""
# if s:
#     print('s不是空字符串')
# else:
#     print('s是空字符串')


# l = []
# if l:
#     print('l不是空列表')
# else:
#     print('l是空列表')


# d = {}
# if d:
#     print('d不是空字典')
# else:
#     print('d是空字典')


# def func():
#     print("函数被调用")
# if func():
#     print('func()返回值不是空')
# else:
#     print('func()返回值为空')




# str="C语言中文网"

# print(str[2])
# print(str[-4])



# print(str[0],"==",str[-6])
# print(str[5],"==",str[-1])




# str="C语言中文网"
# # #取索引区间为[0,2]之间（不包括索引2处的字符）的字符串
# # print(str[:2])
# # #隔 1 个字符取一个字符，区间是整个字符串
# # print(str[::2])
# # #取整个字符串，此时 [] 中只需一个冒号即可
# # print(str[:])

# print(str[1:5])
# print(str[1:-1])


# str = "123456789"
# print(str[2::2])

# str="123456"
# print("C语言"+"中文网:"+str)

# str="C语言中文网"
# print(str*300)


# str="c.biancheng.net"
# # print('b' in str)

# print(len(str))



# str="c.biancheng.net"
# #找出最大的字符
# print(max(str))
# #找出最小的字符
# print(min(str))
# #对字符串中的元素进行排序
# print(sorted(str))


# url = list("http://c.biancheng.net/shell/")

# print(url)

# #使用索引访问列表中的某个元素
# print(url[3])  #使用正数索引
# print(url[-4])  #使用负数索引
# #使用切片访问列表中的一组元素
# print(url[9: 18])  #使用正数切片
# print(url[9: 18: 3])  #指定步长
# print(url[-6: -1])  #使用负数切片



# import time  #引入time模块

# t1 = time.gmtime() # gmtime()用来获取当前时间
# t2 = time.gmtime()

# print(t1 == t2) #输出True
# print(t1 is t2) #输出False




# age = int(input("请输入年龄："))
# height = int(input("请输入身高："))
# if age>=18 and age<=30 and height >=170 and height <= 185 :
#     print("恭喜，你符合报考飞行员的条件")
# else:
#     print("抱歉，你不符合报考飞行员的条件")


# 任意输入姓名，分数，
# - 分数 >= 95 : 天才
# - 分数 >= 75 : 优秀
# - 分数 >= 60 : 还行
# - 其他分数 : 白痴

# name = input("please input name: ")
# scores = int(input("please input scores: "))

# if scores >= 95 :
#     print(name, ", you are smart ")
# elif scores >= 75 :
#     print(name, ", you are good ")
# elif scores >= 60 :
#     print(name, ", you are not good ")
# else :
#     print(name, ", stupid")



# url = "http://c.biancheng.net/cplus/"

# # print("----False and xxx-----")
# # print( False and print(url) )

# print("----True and xxx-----")
# print( True and print(url) )

# # print("----False or xxx-----")
# # print( False or print(url) )

# # print("----True or xxx-----")
# # print( True or print(url) )

# a = int(input('a= '))
# b = int(input('b= '))

# # if a>b:
# #     max = a;
# # else:
# #     max = b;

# max = a if a>b else b

# print(max)

# a = int(input('a= '))
# b = int(input('b= '))
# c = int(input('c= '))
# d = int(input('d= '))

# # max =  a if a>b else c if c>d else d
# if a>b:
#     if a > c:
#         if a >d:
#             max = a
#         else:
#             max = d
#     else:
#         if c > d:
#             max = c
#         else:
#             max = d
# else:
#     if b > c:
#         if b > d:
#             max = b
#         else:
#             max = d
#     else:
#         if c > d:
#             max = c
#         else:
#             max = d
# # max = a if (a>b) el

# print(max)


# str = "C语言中文网"

# print(str[0],"==",str[-6])
# print(str[5],"==",str[-1])



# str="C语言中文网"
# #取索引区间为[0,2]之间（不包括索引2处的字符）的字符串
# print(str[:2])
# #隔 1 个字符取一个字符，区间是整个字符串
# print(str[::2])
# #取整个字符串，此时 [] 中只需一个冒号即可
# print(str[:])



# str=[1,2,3,4,5,6,7,77,66,44,33,222,88]
# print(sorted(str))


# #将字符串转换成列表
# list1 = list("hello")
# print(list1)




# #将元组转换成列表
# tuple1 = ('Python', 'Java', 'C++', 'JavaScript')
# list2 = list(tuple1)
# print(list2)



# #将字典转换成列表
# dict1 = {'a':100, 'b':42, 'c':9}
# list3 = list(dict1)
# print(list3)



# #将区间转换成列表
# range1 = range(1, 6)
# list4 = list(range1)
# print(list4)

# #创建空列表
# print(list())



# url = list("http://c.biancheng.net/shell/")

# #使用索引访问列表中的某个元素
# print(url[3])  #使用正数索引
# print(url[-4])  #使用负数索引

# #使用切片访问列表中的一组元素
# print(url[9: 18])  #使用正数切片
# print(url[9: 18: 3])  #指定步长
# print(url[-6: -1])  #使用负数切片


# l = ['Python', 'C++', 'Java']
# #追加元素
# l.append('PHP')
# print(l)    #   ['Python', 'C++', 'Java', 'PHP']

# #追加元组，整个元组被当成一个元素
# t = ('JavaScript', 'C#', 'Go')
# l.append(t)
# print(l)      # ['Python', 'C++', 'Java', 'PHP', ('JavaScript', 'C#', 'Go')]

# #追加列表，整个列表也被当成一个元素
# l.append(['Ruby', 'SQL'])
# print(l)   # ['Python', 'C++', 'Java', 'PHP', ('JavaScript', 'C#', 'Go'), ['Ruby', 'SQL']]


# l = ['Python', 'C++', 'Java']
# #追加元素
# l.extend('C')
# print(l)
# #追加元组，元祖被拆分成多个元素
# t = ('JavaScript', 'C#', 'Go')
# l.extend(t)
# print(l)
# #追加列表，列表也被拆分成多个元素
# l.extend(['Ruby', 'SQL'])
# print(l)




# l = ['Python', 'C++', 'Java']
# #插入元素
# l.insert(1, 'C')
# print(l)


# #插入元组，整个元祖被当成一个元素
# t = ('C#', 'Go')
# l.insert(2, t)
# print(l)


# #插入列表，整个列表被当成一个元素
# l.insert(3, ['Ruby', 'SQL'])
# print(l)


# #插入字符串，整个字符串被当成一个元素
# l.insert(0, "http://c.biancheng.net")
# print(l)


# # ["http://c.biancheng.net", 'Python', 'C', ('C#', 'Go'), ['Ruby', 'SQL'], 'C++', 'Java']






# lang = ["Python", "C++", "Java", "PHP", "Ruby", "MATLAB"]
# #使用正数索引
# del lang[2]
# print(lang)
# #使用负数索引
# del lang[-2]
# print(lang)

# lang = ["Python", "C++", "Java", "PHP", "Ruby", "MATLAB"]
# del lang[1: 4]  # ["Python", "Ruby", "MATLAB"]
# print(lang)
# lang.extend(["SQL", "C#", "Go"]) # ["Python", "Ruby", "MATLAB", "SQL", "C#", "Go"]
# del lang[-5: -2] # ["Python", "C#", "Go"]
# print(lang)


# lang = ["Python", "C++", "Java", "PHP", "Ruby", "MATLAB"]
# del lang[1] # del C++
# del lang[2: 4] # del PHP, Ruby
# lang.insert(3, "C#")               # insert C# at index 3
# print(lang) 


# nums = [40, 36, 89, 2, 36, 100, 7]
# nums.pop(3)
# print(nums)
# nums.pop()
# print(nums)




# nums = [40, 36, 89, 2, 36, 100, 7]
# #第一次删除36
# nums.remove(36)
# print(nums)
# #第二次删除36
# nums.remove(36)
# print(nums)
# #删除78
# nums.remove(78)
# print(nums)


# url = list("http://c.biancheng.net/python/")
# print(url)
# url.clear()
# print(url)

# please input a string (length > 10): 1234567890
# str = "abcdefghijk"
# delete 第1,3,5,8个元素      # 246890 
# 在头和尾部各追加一个$符号
# then print

# str = input('pleas input a string: ') # "abcdefghijk"
# qqq = list(str) # ['a','b','c'....]

# del qqq[0] # "bcdefghijk"
# del qqq[1] # "bdefghijk"
# del qqq[2] # "bdfghijk"
# del qqq[4] # "bdfgijk"


# qqq.insert(0,'$')
# qqq.append('$')

# print(qqq)


# nums = [40, 36, 89, 2, 36, 100, 7]
# nums.pop(3)
# print(nums)
# nums.pop()
# print(nums)



# nums = [40, 36, 89, 2, 36, 100, 7]
# #第一次删除36
# nums.remove(36)
# print(nums)
# #第二次删除36
# nums.remove(36)
# print(nums)
# #删除78
# nums.remove(78)
# print(nums)



# nums = [40, 36, 89, 2, 36, 100, 7]
# nums[2] = -26  #使用正数索引
# nums[-3] = -66.2  #使用负数索引

# nums[-2] = 88
# nums[5] = 66

# print(nums)


# nums = [40, 36, 89, 2, 36, 100, 7]
# #修改第 1~4 个元素的值（不包括第4个元素）
# nums[1: 4] = [45.25, -77, -52.5]
# print(nums)




# nums = [40, 36, 89, 2, 36, 100, 7]
# #在4个位置插入元素
# nums[4: 4] = [-77, -52.5, 999]
# print(nums)




# s = list("Hello")    # ['H','e','l'.....]
# s[2:4] = 'K'
# print(s)



# nums = [40, 36, 89, 2, 36, 100, 7, 40, 36, 89, 2, 36, 100, 7]
# #步长为2，为第1、3、5个元素赋值
# nums[1: 12: 5] = [1, 6, 11]
# print(nums)


# nums = [40, 36, 89, 2, 36, 100, 7, -20.5, -999, 55]
# #检索列表中的所有元素
# print( nums.index(2) )
# #检索3~7之间的元素
# print( nums.index(100, 3, 7) )
# #检索4之后的元素
# print( nums.index(7, 4) )
# #检索一个不存在的元素
# print( nums.index(55) )



# nums = [40, 36, 89, 2, 36, 1000, 7, -20.5, 36]
# #统计元素出现的次数
# print("36出现了%d次" % nums.count(36))
# #判断一个元素是否存在
# if nums.count(100):
#     print("列表中存在100这个元素")
# else:
#     print("列表中不存在100这个元素")



# tt = 'hello'
# #定义一个包含多个类型的 list
# list1 = [1,4,tt,3.4,"yes",[1,2]]
# print(list1,id(list1))


# #比较 list 中添加元素的几种方法的用法和区别
# list3 = [6,7]
# l2 = list1 + list3
# print(l2,id(l2))

# name =  ['xgg', 'mia', 'hex', 'lxz', 'yh' ,'sx', 'wmy', 'ava']
# print(name)
# print(id(name))

# print(name[2])





# tuple1 = ('Python', 'Java', 'C++', 'JavaScript')
# tuple1[3] = '123'
# print(tuple1)

# list2 = list(tuple1)
# list2[3] = '123'
# print(list2)



# range1 = range(2, 100, 2)
# list4 = list(range1)
# print(list4)


# url = list("http://c.biancheng.net/shell/")
# #使用索引访问列表中的某个元素
# print(url[3])  #使用正数索引
# print(url[-4])  #使用负数索引
# #使用切片访问列表中的一组元素
# print(url[9: 18])  #使用正数切片
# print(url[9: 18: 3])  #指定步长
# print(url[-6: -1])  #使用负数切片


# language = ["Python", "C++", "Java","aurora"]
# birthday = [1991, 1998, 1995,2024]
# info = language + birthday
# print("language =", language)
# print("birthday =", birthday)
# print("info =", info)



# l = ['Python', 'C++', 'Java']
# #追加元素
# l.append('PHP')
# print(l)
# #追加元组，整个元组被当成一个元素
# t = ('JavaScript', 'C#', 'Go')
# l.append(t)
# print(l)
# #追加列表，整个列表也被当成一个元素
# l.append(['Ruby', 'SQL'])
# print(l)


# 请输入字符串: tom1
# 请输入字符串: tom2
# 请输入字符串: tom3
# ['tom1', 'tom2', 'tom3']

# l = []
# l.append('start')

# str = input('plaese input a string :  ')
# l.append(str)

# str = input('please input a string :  ')
# l.append(str)

# str = input('please input a string :  ')
# l.append(str)

# l.append('end')
# print(l)



# lst = list(input('pleas input a str:  '))
# # lst = list(str)
# lst.remove('a')
# print(lst)



# nums = [40, 36, 89, 2, 36, 100, 7]

# nums[3: 5] = [1, 2, 3 ]
# print(nums)





# weight = float(input('please input your weight: '))
# if weight >= 80: 
#     print("overweight")
# else:
#     print('normal')


# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))

# print(type(a))
# print(type(b))

# result = a + b
# print("result Value: ", result)
# print("result Type: ", type(result))



# a = float(input("a =  "))
# b = float(input("b =  "))
# c = float(input("c =  "))

# # result = a * b * c

# print(a, '*', b, '*', c,  '=', a * b * c)


# user_name = 'Charlie'
# user_age = 8

# print("读者名：", user_name, "年龄：", user_age, sep='        ')


# print(40,'\t', end="")
# print(50,'\t', end="")
# print(60,'\t')

# name = "Tom"
# age = 8
# print("%s已经%d岁了！" % (name,age))



# name = input('pleas input a name: ')
# year = int(input('pleas input a year: '))

# print("%s is Y%d's student." % (name,year))





# class revealAccess:
#     def __init__(self, initval = None, name = 'var'):
#         self.val = initval
#         self.name = name
#     def __get__(self, obj, objtype):
#         print("Retrieving",self.name)
#         return self.val
#     def __set__(self, obj, val):
#         print("updating",self.name)
#         self.val = val
# class myClass:
#     x = revealAccess(10,'var "x"')
#     y = 5
# m = myClass()
# print(m.x)
# m.x = 20
# print(m.x)
# print(m.y)






# str = "C语言中文网"

# # print(str[0],str[-6])
# # print(str[5],str[-1])


# # print(str[:2])

# # print(str[::2])

# # print(str[:])

# print(str[2:5:])




# str="c.biancgaoheng.net"



# print(list(str))


# numbers = [22,40,8,9,10]

# # print(sorted(numbers, reverse=True))

# # numbers.reverse()
# # print(numbers)

# print(list(enumerate(numbers)))









# import urllib.request
# import bz2
# import shutil

# # 下载文件
# url = "http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2"
# file_path = "shape_predictor_68_face_landmarks.dat.bz2"
# urllib.request.urlretrieve(url, file_path)

# # 解压缩
# with bz2.BZ2File(file_path) as fr, open("shape_predictor_68_face_landmarks.dat", "wb") as fw:
#     shutil.copyfileobj(fr, fw)

# print("下载并解压完成！")





# # 先检测并提取人脸区域
# faces = detector(gray_face)

# if len(faces) == 0:
#     result = "无法检测到人脸，请提供更清晰的图片。"
# else:
#     # 获取人脸边界框
#     x, y, w, h = faces[0].left(), faces[0].top(), faces[0].width(), faces[0].height()
#     face_cropped = face_image[y:y+h, x:x+w]

#     # 卡通化处理（使用双边滤波+边缘检测）
#     face_color = cv2.bilateralFilter(face_cropped, 9, 75, 75)
#     gray_face_cropped = cv2.cvtColor(face_cropped, cv2.COLOR_BGR2GRAY)
#     edges = cv2.adaptiveThreshold(cv2.medianBlur(gray_face_cropped, 7), 255,
#                                   cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
#     edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
#     cartoon_face = cv2.bitwise_and(face_color, edges)

#     # 保存并返回结果
#     cartoon_face_path = "/mnt/data/cartoon_face.png"
#     cv2.imwrite(cartoon_face_path, cartoon_face)
#     result = cartoon_face_path

# result




