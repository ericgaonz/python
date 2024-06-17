# lst = []
# while 1 == 1:
#     print("Plase input a command (add, del or end): ", end = '')
#     command = input()
#     if (command == 'add'):
#         value = input('please input what to add: ')
#         lst.append(value)
#     elif (command == 'del'):
#         idx = int(input('please input the element index to delete: '))
#         del lst[idx]
#     elif (command == 'end'):
#         break
#     else:
#         print('You input a wrong command!')
#         continue
    
#     print(lst)


# lst = []
# n = int(input('Please input a number: '))
# for i in range(2, n):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         lst.append(i)

# print(lst)




#----------------------------------------------#
# newlist = [i for i in range(2, 100) if i % 2 != 1]
# print(newlist)

# lst = []
# for i in range(1, 100):
#     if (i % 2 == 0):
#         lst.append(i)

# print(lst)

#----------------------------------------------#

# lst = []
# for i in range(1,100, 2):
#     lst.append(i)

# print(lst)

# newlist = [i for i in range(2, 100, 2)]
# print(newlist)
#----------------------------------------------#

# newlist = [i for i in range(1, 100) if i % 7 == 0]
# print(newlist)

# newlist = [x for x in range(10) if x < 5]
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x.upper() for x in fruits if 'a' in x]
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = ['hello %s' % x for x in fruits]
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x if x != "cherry" else "ABC" for x in fruits]
# print(newlist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse = True)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)



# list1 = ["a", "c", "b"]
# list2 = ['1', '22', '3']

# list3 = list1 + list2
# list3.sort()
# print(list3)


# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)


# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)

# ---------------- 2023-06-10 ---------------- #





# n = int(input('Please input a number: '))

# yesOrNo = False
# for i in range(2, n):
#     if n % i == 0:
#         break
# else:
#     yesOrNo = True

# if yesOrNo == False:
#     print('No, it is not a prime number!')
# else:
#     print('yes, it is a prime number.')



# lst = ['a', 'b', 'c'] #list
# tpl = ('d', 'e', 'f') #tuple
# dic = {'name':'tom', 'age':13, 'gender':'female'} #dictionary

# # print(lst[1])
# # lst[1] = 'ccc'
# # print(lst[1])


# # print(tpl[1])
# # tpl[1] = 'ccc'
# # print(tpl[1])

# print(dic['age'])
# dic['age'] = 66
# print(dic['age'])


#dictname = {'key':'value1', 'key2':'value2', ..., 'keyn':valuen}   #brace

# student = {'姓名': 'Tom', '年龄': '12', '数学': 95, '英语': 92, '语文': 84}
# print(student)
# print(student['姓名'])
# print(student['年龄'])
# print(student['语文'])



# dict1 = {(20, 30): 'great', 30: 'abc', 'others':'12345'}
# print(dict1[(20, 30)])


# subs = ['语文', '数学', '英语']
# scores = dict.fromkeys(subs, 60)
# print(scores)





# a = {'pe':95}
# # print(a)

# a['science'] = 89
# # print(a)

# a['music'] = 90
# print(a)

# # del a['science']
# # print(a)

# # del a
# # print(a)


# print('music' in a)
# print('abc' in a)

# a['abc'] = 99
# print('abc' in a)





# scores = {'music': 95, 'english': 89, 'pe': 90}

# # print(type(scores.keys()))
# # print(scores.values())
# # print(scores.items())

# for rcd in scores.keys():
#     print(rcd)



# a = {'music': 95, 'english': 89, 'pe': 90}
# b = list(a.keys())
# print(type(b))
# print(b)

# a = {'music': 95, 'english': 89, 'pe': 90}
# for k in a.keys():
#     print(k,end=' ')
# print("\n---------------")
# for v in a.values():
#     print(v,end=' ')
# print("\n---------------")



# for k,v in a.items():
#     print("key:",k," value:",v)




# a = {'one': 1, 'two': 2, 'three': [1,2,3]}
# b = a.copy()
# print(b)


# a = {'one': 1, 'two': 2, 'three': [1,2,3]}
# b = a.copy()

# a['one'] = 11            #this will only update a
# a['three'][1] = 22       #this will affect both a and b

# print(a)
# print(b)


# # to update dic a by using dic b
# a = {'one': 1, 'two': 2, 'three': 3}
# b = {'one':4.5, 'four': 9.3}
# a.update(b)
# print(a)


# a = {'math': 95, 'English': 89, 'Japanese': 90, 'DH': 83, 'pe': 98, 'PY': 89}
# print(a)
# a.pop('Japanese')
# print(a)
# a.popitem()
# print(a)


# a = {'math': 95, 'English': 89, 'Japanese': 90}
# print(a)
# #key不存在，指定默认值
# a.setdefault('py', 94)
# print(a)
# #key不存在，不指定默认值
# a.setdefault('PE')
# print(a)
# #key存在，指定默认值
# a.setdefault('math', 100)
# print(a)


# table = {}
# table[(0,0)] = 1
# table[(0,1)] = 2
# table[(0,3)] = 3
# table[(1,0)] = 4

# print(table)



# table = {
#     (0, 0): 1,
#     (0, 1): 2,
#     (0, 2): 3,
#     (1, 0): 4,
#     (1, 1): 5,
#     (1, 2): 6,
#     (2, 0): 7,
#     (2, 1): 8,
#     (2, 2): 9
# }
# a = {
#     'math': 95,
#     'English': 89,
#     'Japanese': 90
# }
# a['English'] 

# print(table[(1, 2)])

# table = {}
# for i in range(3):
#     for j in range(3):
#         table[(i, j)] = int(input('Please input a number: '))

# # print(table)

# for i in range(3):
#     for j in range(3):
#         print(table[(i, j)], '\t', end=' ')
#     print()



# for i in range(3):
#     for j in range(3):
#         print(i,j)




# table = {}
# for i in range(3):
#     for j in range(3):
#         table[(i, j)] = input('Please input a number: ')


# print("tom\tjack\teric")
# for i in range(3):
#     for j in range(3):
#         print(table[(i, j)], '\t', end=' ')
#     print()

# scores = {}
# scores['tom'] = {}
# scores['tom']['math'] = 99
# scores['tom']['music'] = 90
# scores['tom']['english'] = 90


# scores['eric'] = {}
# scores['eric']['math'] = 99
# scores['eric']['music'] = 90
# scores['eric']['english'] = 90

# print(scores)

# {
#     'tom': {
#         'math': 99, 
#         'music': 90, 
#         'english': 90
#     }, 
#     'eric': {
#         'math': 99, 
#         'music': 90, 
#         'english': 90
#     }
# }



# myscores = {}
# myscores[('tom', 'math')] = 99
# myscores[('tom', 'music')] = 99
# myscores[('tom', 'english')] = 99


# myscores[('eric', 'math')] = 99
# myscores[('eric', 'music')] = 99
# myscores[('eric', 'english')] = 99

# print(myscores)
# # {
# #     ('tom', 'math'): 99, 
# #     ('tom', 'music'): 99, 
# #     ('tom', 'english'): 99, 
# #     ('eric', 'math'): 99, 
# #     ('eric', 'music'): 99, 
# #     ('eric', 'english'): 99
# # }

# please input the number of students: 3

# please input No.1 student name:
# please input the scorce of No.1 student math:
# please input the scorce of No.1 student music:
# please input the scorce of No.1 student english:




# myscores = {}
# myscores[('tom', 'math')] = 99
# myscores[('tom', 'music')] = 99
# myscores[('tom', 'english')] = 99


# myscores[('eric', 'math')] = 99
# myscores[('eric', 'music')] = 99
# myscores[('eric', 'english')] = 99

# print(myscores)


# scores = {}
# numbers = int(input('please input the number of students: '))
# for i in range(numbers):
#     name = input('No.%d student name:' % int(i+1))
#     scores[(name, 'math')] = float(input('No.%d student math score:' % int(i+1)))
#     scores[(name, 'music')] = float(input('No.%d student music score:' % int(i+1)))
#     scores[(name, 'english')] = float(input('No.%d student english score:' % int(i+1)))

# print(scores)
# {
#     ('tom', 'math'): 32.3, 
#     ('tom', 'music'): 89.9, 
#     ('tom', 'english'): 98.0, 
#     ('Jack', 'math'): 1.0, 
#     ('Jack', 'music'): 3.0, 
#     ('Jack', 'english'): 6.0
# }



# template = 'My name: %(name)s, my age: %(age)d, my email: %(email)s'
# course = {
#     'name':'Tom', 
#     'age': 13, 
#     'email': 'teat@gmail.com'
# }

# print(template % course)

# course = {'name':'Jack', 'age': 20, 'email': 'jack@gmail.com'}
# print(template % course)


# mydic = {
#     'name':'Tom', 
#     'age': 13, 
#     'email': 'teat@gmail.com'
# }
# print(type(mydic))
# print(mydic)

# myset = {"1", "22", "333", "22"}
# print(type(myset))
# print(myset)

# mylist = ["1", "2", "3", "2"]
# print(type(mylist))
# print(mylist)


# myset = {
#     1,
#     2,
#     1,
#     (1,2,3),
#     'c',
#     'c'
# }
# print(myset)
# {
#     1, 
#     2, 
#     'c', 
#     (1, 2, 3)
# }


# set1 = set("01234567890123456789")
# set2 = set([1,2,3,4,5,1,2,3,4,5])
# set3 = set((1,2,3,4,5,6,5,4,3,2,1))
# print("set1:", set1)
# print("set2:", set2)
# print("set3:", set3)

# myset = {1,'c',1,(1,2,3),'c'}
# for ele in myset:
#     print(ele, end = ' ')
# print()

# a = {1,'c',1,(1,2,3),'c'}
# lst = list(a)
# print(lst)


# import copy
# list1 = [[1, 2], (30, 40)]
# list2 = copy.deepcopy(list1)

# list1.append(100)
# print("list1:",list1)
# print("list2:",list2)

# list1[0].append(3)
# print("list1:",list1)
# print("list2:",list2)

# list1[1] += (50, 60)
# print("list1:",list1)
# print("list2:",list2)


# s = {'Python', 'C', 'C++'}
# fs = frozenset(['Java', 'Shell'])
# s_sub = {'PHP', 'C#'}
# #向set集合中添加frozenset
# s.add(fs)
# print('s =', s)
# #向为set集合添加子set集合
# s.add(s_sub)
# print('s =', s)




# s = 0
# for n in range(1, 101):
#     # print('n = %d' % n)
#     # old = s
#     s = s + n
#     # print('s = %d' % s)
#     # print('%d = %d + %d' % (s, old, n))

# print(s)


    

# s = 0
# for n in range(0, 101, 2):
#     print(n)
#     s = s + n

# print(s)


# s = 0
# num = 2
# while num <= 101:
#     s = s + num
#     num += 2
# print(s)


# s = 0
# num = 1
# while num <= 100 :
#     s = s + num
#     num += 1
# print(s)


# dic = {
#     'rubbish': 'ごみ',
#     'chair': 'いす',
#     'dog': 'いぬ',
#     'shoes': 'くつ',
#     'rubbish bin': 'ごみばこ',
#     'house': 'いえ',
#     'room': 'へや',
#     'window': 'まど',
#     'food': 'たぺもの',
#     'photo': 'しゃしん',
#     'bathroom': 'ふろば',
#     'drink': 'のみもの',
#     'kitchen': 'だいどころ',
#     'watch': 'とけい',
#     'clock': 'とけい',
#     'garden': 'にわ',
#     'desk': 'つくえ',
#     'flower': 'はな',
#     'tree': 'き',
#     'picture': 'え',
#     'book': 'ほん',
#     'sweet': 'おかし',
#     'snack': 'おかし',
#     'tv': 'てれび',
#     'japanese cushion': 'ざぷとん',
#     'slippers': 'すりっぱ',
#     'shower': 'しゃわー',
#     'cat': 'ねこ',
#     'tatami mat': 'たたみ',
#     'japanese bedding': 'ふとん',
# }

# print(dic['watch'])


# step 1:
# a = 3
# b = 108

# the total is *****

# a = int(input('Please input your first number: '))
# b = int(input('Please input your second number: '))

# s = 0
# num = a
# while num <= b :
#     s = s + num
#     num += 1
# print(s)





# # step 2
# def sum(a, b):
#     s = 0
#     num = a
#     while num <= b :
#         s = s + num
#         num += 1 # num = num + 1
    
#     return s



# # print(sum(1, 100)) # 5050
# # print(sum(2, 99)) # 4949
# print(sum(22, 9999)) # 4949



# please input the number of a list: 5
# please input number 1: ***
# please input number 2: ***
# please input number 3: ***
# please input number 4: ***
# please input number 5: ***

# save all numbers into a list then print the list.


# n = int(input('please input the number of a list: '))

# lst = []
# for x in range(1, n+1):
#     number = int(input('please input number %d: ' % (x)))
#     lst.append(number)

# # i = 1
# # while i <= n:
# #     number = int(input('please input number %d: ' % (i)))
# #     lst.append(number)
# #     i = i + 1 


# print(lst)
# # min = lst[0]
# # for x in lst:
# #     if min > x:
# #         min = x


# print(min)

    

# def max(numbers):
#     max = numbers[0]
#     for x in numbers:
#         if max <= x:
#             max = x
#     return max



# def min(*numbers):
#     min = numbers[0]
#     for x in numbers:
#         if min > x:
#             min = x
#     return min





# print(max([1,3,55,77,88,99,1000,3,5,6]))
# print(max([1,3,55,77,44,5,4,3,5,6]))
# print(max([1,3,55,77,88,99,6,3,5,6]))

# print(min(0, -1, 3, 4, 55, 77, 100))
# print(min(3, 444, 3, 4, 55, 27, 13))
# print(min(6, -11, 32, 43, 55, 1, 54))




# def sum(*numbers):
#     sum = 0
#     for x in numbers:
#         sum = sum + x

#     return sum




# print(sum(1,2,3,4))
# print(sum(1,2,99))
# print(sum(11,2,99))
# print(sum(11,2,23,444,3,77,88,99))
# print(sum(11,2,3,78,89,77,99))
# print(sum(11,2,3,56,666,77,88,99))


# def product(*numbers):
#     prd = 1
#     for x in numbers:
#         prd = prd * x

#     return prd



# print(product(1,2,3,4))
# print(product(1,2,4))
# print(product(11,2,5))




# def lst(number):
#     s = 0
#     for x in range(1, number +1, 2):
#         s = s + x

#     p = 1
#     for x in range(2, number+1, 2):
#         p = p * x

#     return {"sum":s, "product":p}


# a = int(input('Please input a number of your choice: '))

# result = lst(a)
# print(result['product'])



# dic = {}
# dic['name'] = 'tom'


# print(dic)

# def add(dic, key, value):
#     dic[key] = value

#     return dic

# dic = {}
# name = input('Please input your name: ')
# age = int(input('Please input r age: '))
# email = input('Please input your email: ')

# # dic['name'] = name
# # dic['age'] = age
# # dic['email'] = email

# add(dic, 'name', name)
# add(dic, 'age', age)
# add(dic, 'email', email)

# print(dic)


    


# queue = []

# queue.insert(0,'Kayley')
# queue.insert(0,'Eric')
# queue.insert(0,"Christina")
# queue.insert(0,"Zamira")
# queue.insert(0,"Elena")
# queue.insert(0,"Laila")
# queue.insert(0,"Olivia")
# queue.insert(0,"Aurora")
# print(queue)


# # Elena, Laila, Eric, Christina, Aurora, Zamira, Olivia, Kayley

# print("get the first element: ", queue.pop(0))
# print(queue)
# print("get the first element: ", queue.pop(0))
# print(queue)
# print("get the first element: ", queue.pop(0))
# print(queue)


# lst = [1,4,7,9,44,66]

# print(lst[3])


# stack = []
# stack.append('Mr Smith')
# stack.append('Ms Van Zyl')
# stack.append('Ms Salinger')
# print(stack)

# print("The first element: ", stack.pop(0))
# print(stack)
# print("The second element: ", stack.pop(0))
# print(stack)
# print("The third element: ", stack.pop(0))
# print(stack)

# tup1 = tuple("hello")
# print(tup1)

# list1 = ['Python', 'Java', 'C++', 'JavaScript']
# tup2 = tuple(list1)
# print(tup2)

# dict1 = {'a':100, 'b':42, 'c':9}
# tup3 = tuple(dict1)
# print(tup3)

# range1 = range(1,6)
# tup4 = tuple(range1)
# print(tup4)

# print(tuple())



# scores = {'数学': 95, '语文': 89, '英语': 90}
# # print(scores.keys())
# # print(scores.values())
# # print(scores.items())

# tup = tuple(scores.keys())
# print(tup)

# tup = tuple(scores.values())
# print(tup)

# tup = tuple(scores.items())
# print(tup)

# url = tuple("123456789")
# print(type(url))
# print(url)

# print(url[3])
# print(url[-4])

# print(url[2:5])
# print(url[3: 6: 2])
# print(url[-6: -1 : 2])



# lst = [1,2,3,1,2,3,4,5,6,4,4,4,4,4,4,4,4,4,4,6,7,5,8,9,0]
# newlst = []

# for x in lst:
#     if x not in newlst:
#         newlst.append(x)

# print(newlst)
    


# # def removeDuplicates(lst):
# #     newlst = []
# #     for x in lst:
# #         if x not in newlst:
# #             newlst.append(x)

# #     return newlst


# # # myLst = removeDuplicates(lst)
# # # print(myLst)


# # print(removeDuplicates([1,2,3,2,3,4,534,34,56,67,68,67]))


# # myset = {1,4,3,2,5,2,3,4,5,6,74,7}
# # print(myset)

# lst = list(set(lst))
# print(lst)


# # set(lst)


# def printall(name, age, email):
#     print('%s is stupid, and you are %d, your email is %s.' % (name, age, email))


# name = input('Please input your name: ')
# age = int(input('How old are you? '))
# email = input('Please insert your email: ')

# printall(name, age, email)
# printall('Christina', 13, 'christina.chen@gmail.com')

# # print(name, 'is stupid, and you are', age, ', your email is', email, '.')
# # print('%s is stupid, and you are %d, your email is %s.' % (name, age, email))
# # print(f"{name} is stupid, and you are {age}, your email is {email}.")



# for x in range(1, 8):
#     # if x in (6, 7): break
#     if x == 6 or x == 7: break
#     if x == 4: continue
#     for y in range(1, 10):
#         if y == 4: continue
#         print(f"{x} 0 {y}", end='\t')
#     print()


# if a > b:
#     print('Yeah!!!!')
# else:
#     print('No!!!!')

# print('Yeah!!!!') if a > b else print('No!!!!')

#option 1, code1 if condition else codes2
#option 2, variable = result1 if condition else result2

# levels = floors + 2 if not isFourIncluded else floors + 1

# s = 0

# # if a + b > 40:
# #     s = a + b
# # else:
# #     s = a - b

# s = a + b if a + b > 40 else a - b

# print(s)






# s = 0
# high = 100

# for x in range (1,11):
#     s += high

#     if x != 10:
#         high /= 2  # high = high / 2
#         s += high

# print(s)






# name = "Kelly"
# name2 = name

# name = "jack"
# name3 = name

# id(name),id(name2),id(name3)



# n = 1
# for i in range(1, 31, 2):
#     for k in range(1, 81 - n):
#         print(' ', end = '')
#     for j in range(1, i + 1):
#         print('.', end = '')
    
#     n = n + 4
#     print()


# n = 1
# for i in range(-1, 21, 2):
#     for j in range(1, 31 - n):
#         print(' ', end = '')

#     if i == 13:
#         print('* * * * * * * *', end = '')
#     else:
#         if i != -1:
#             print('*', end = '')

#         for k in range(1, i + 1):
#             print(' ', end = '')

#         print('$', end = '')

#     n= n + 1 


#     print()


# print('                             *')
# print('                            *+*')
# print('                           *+++*')
# print('                          *+++++*')
# print('                         *+++++++*')
# print('                        *+++++++++*')
# print('                       *+++++++++++*')
# print('                      * * * * * * * *')
# print('                     *+++++++++++++++*')
# print('                    *+++++++++++++++++*')
# print('                   *+++++++++++++++++++*')



# n = 1
# for i in range(-1, 21, 2):
#     for j in range(1, 31 - n):
#         print('-', end = '')

#     if i != -1:
#         print('*', end = '')

#     for k in range(1, i + 1):
#         print('=', end = '')

#     print('$', end = '')

#     n= n + 1 
#     print()


# print('*******************************')
# print('*******************************')
# print('*******************************')
# print('*******************************')
# print('*******************************')
# print('*******************************')
# print('*******************************')
# print('*******************************')
# print('*******************************')
# print('*******************************')
# print('*******************************')
# print('*******************************')
# print('*******************************')
# print('*******************************')
# print('*******************************')

# for i in range(16, -1, -1):
#     # print(i)
#     for j in range(1, 35):
#         if j == 18 + i or j == 18 - i:
#             print("*", end = '')
#         else:
#             print(" ", end = '')
#     print('')


# for i in range(0, 18):
#     for j in range(0, 35):
#         if j == i or j == 34 - i:
#             print("*", end = '')
#         else:
#             print(" ", end = '')
#     print('')



# i = 3 
# print(f"i = {i}, {type(i)}")

# dic = {'a':'apple', 'b':'boy', 'c':'cat', 'd':'dog', 'e':'elephant'} 
# print(f"dic = {dic}, {type(dic)}")

# lst = ['books', 'movie', 'restaurant']
# print(f"lst = {lst}, {type(lst)}")

# f = 3.14159265358979328
# print(f"f = {f}, {type(f)}")

# name = "tom"
# print(f"name = {name}, {type(name)}")

# bol = True
# print(f"bol = {bol}, {type(bol)}")

# tup = ("apple", "orange", "strawberry")
# print(f"tup = {tup}, {type(tup)}")

# rang = range(1, 10)
# print(f"rang = {rang}, {type(rang)}")


# numbers = (1,4,5)

# # a = numbers[0]
# # b = numbers[1]
# # c = numbers[2]
# # print(a)
# # print(b)
# # print(c)

# a,b,c = numbers
# print(a,b,c)

# person = {
#     'name': 'Jacky',
#     'age': 100,
#     'wife': {
#         'name':'Ami',
#         'age': 4000
#     },
#     'elder daughter': {
#         'name':'Amazing Person',
#         'age': 13
#     },
#     'young daughter': {
#         'name': 'Dumbpoo',
#         'age': 0
#     }
# }


# # print(person['elder daughter']['age'])
# # print(person['young daughter']['name'])

# name, age, wife, elderDaughter, youngDaughter = person

# # print(name, age, wife, elderDaughter, youngDaughter)
# print(person[name], person[age], person[wife], person[elderDaughter], person[youngDaughter])




# define a dictionary its name is "family", it should includes all your family information.
# e.g.
# family = {
#     "dad": {
#         "name": "sdfsd",
#         "age": "sdfsd",
#         "hobby": "sdfsd",
#         ...
#     },
#     "mum": {
#         "name": "sdfsd",
#         "age": "sdfsd",
#         "hobby": "sdfsd",
#         ...
#     },
#     ...
# }

# then print any information of your family.


# family = {
#     'dad': {
#         'name': 'Jacky',
#         'age': 40
#     },
#     'mum': {
#         'name': 'Amy',
#         'age': 43
#     },
#     'sister': {
#         'name': 'Jacky',
#         'age': 40
#     },
#     'grandpa': {
#         'name': 'Jacky',
#         'age': 40
#     },
#     'grandma': {
#         'name': 'Jacky',
#         'age': 40
#     }
# }

# for person in family:
#     print()


# family = {
#     'dad': {},
#     'mum': {},
#     'sister': {},
#     'grandpa': {},
#     'grandma': {}
# }

# for key in family:
#     family[key]['name'] = input(f"Please input {key}'s name: ")
#     family[key]['age'] = input(f"Please input {key}'s age: ")

# print('\n\nName\tAge')
# print('-----------')
# for person in family:
#     print(f"{family[person]['name']}\t{family[person]['age']}")
# print('-----------')



# 两个数字变量互换
# a = 3
# b = 5



# '''
# 类方法（可调类变量、可被实例调用、可被类调用）
# 1、类方法通过@classmethod装饰器实现，只能访问类变量，不能访问实例变量；
# 2、通过cls参数传递当前类对象，不需要实例化。
# '''
# class Car(object):
#     name = 'BMW'
#     def __init__(self, name):
#         self.name = name
#     @classmethod
#     def run(cls,speed):
#         print(cls.name,speed,'行驶')
# # 访问方式1
# c = Car("宝马")
# c.run("100迈")
# # 访问方式2
# Car.run("100迈")




# '''
# 静态方法（可调类变量、可被实例调用、可被类调用）
# 1、用 @staticmethod 装饰的不带 self 参数的方法；
# 2、静态方法名义上归类管理，实际中在静态方法中无法访问类和实例中的任何属性；
# 3、调用时并不需要传递类或实例。
# '''
# class Car(object):
#     name = 'BMW'
#     def __init__(self, name):
#         self.name = name
#     @staticmethod
#     def run(speed):
#         print(Car.name,speed,'行驶')
		
# # 访问方式1
# c = Car("宝马")
# c.run("100迈")
# # 访问方式2
# Car.run("100迈")



# # 实例方法（可调类变量、可调实例变量、可被实例调用）
# # 第一个参数强制为实例对象 self。
# class Car(object):
#     name = 'BMW'
#     def __init__(self, name):
#         self.name = name
#     def run(self,speed):
#         print(self.name,speed,'行驶')

# # 访问
# c = Car("宝马")
# c.run("100迈")


# def variable_fun(kind, *arguments, **keywords):
#     print("friend : ", kind, ";")
#     print("-" * 40)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])
        
# # # 函数调用
# # variable_fun("xiaoming",
# #              "hello xiaoming", "nice to meet you!",
# #             mother="xiaoma",
# #             father="xiaoba",
# #             son="see you")
            
# # 输出结果
# # first arg:  xiaoming ...
# # ----------------------------------------
# # hello 
# # nice to meet you!
# # ----------------------------------------
# # mother : xiaoma
# # father : xiaoba
# # son : see you

# list01 = ["hello xiaoming", "nice to meet you!"]
# dict01 = {'mother': 'xiaoma', 'father': 'xiaoba', 'son': 'see you'}
# variable_fun("xiaoming", *list01, **dict01)



# # 借用官网例子
# def key_fun(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This key_fun wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")

# # 函数调用  
# key_fun(1000)                                          # 1 positional argument
# print("-" * 40)
# key_fun(voltage=1000)                                  # 1 keyword argument
# print("-" * 40)
# key_fun(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# print("-" * 40)
# key_fun(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# print("-" * 40)
# key_fun('a million', 'bereft of life', 'jump')         # 3 positional arguments
# print("-" * 40)
# key_fun('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword



# from math import factorial

# def square(n):
#     return n ** 2

# # 使用python自带数学函数
# facMap = map(factorial, list(range(10)))
# print(list(facMap))
# # print out: [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

# # 使用自定义函数
# squareMap = map(square, list(range(10)))
# print(list(squareMap))
# # print out: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]




# # 注意，现在 reduce() 函数已经放入到functools包中。
# from functools import reduce

# result = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])

# print(result)
# # print out 15


# # 设定初始参数：
# s = reduce(lambda x, y: x + y, ['1', '2', '3', '4', '5'], "数字 = ")

# print(s)
# # print out：数字 = 12345



# def boy(n):
#     if n % 2 == 0:
#         return True
#     return False

# # 自定义函数
# filterList = filter(boy, list(range(20)))

# print(list(filterList))
# # print out: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# # 自定义函数
# filterList2 = filter(lambda n: n % 2 == 0, list(range(20)))

# print(list(filterList2))
# # print out: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]





# print('Hello')
# a = len('hello') #length
# print(a)

# print(len('hello'))

# myStr = input('Please input a string: ')

# sum = 0
# for char in myStr:
#     sum = sum + 1

# print(sum)


# def my_len(str):
#     sum = 0
#     for char in str:
#         sum = sum + 1

#     return sum


# myStr = input('Please input a string: ')
# print(len(myStr))
# print(my_len(myStr))



# def add(num1, num2):
#     return num1 + num2

# def multiply(num1, num2):
#     return num1 * num2


# print(add(6, 7))
# print(multiply(6, 7))





print_5_times('hello')
print_5_times('Christna')
print_5_times('Kelly')
