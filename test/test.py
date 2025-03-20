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





# def repeat(content, times):
#     # i = 1
#     # while (i <= times):
#     #     print(content)
#     #     i = i + 1


#     for i in range(times):
#         print(content)


# repeat('Eric', 5)













# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         reply = input(prompt)
#         if reply in {'y', 'ye', 'yes'}:
#             return True
#         if reply in {'n', 'no', 'nop', 'nope'}:
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)


# # #只给出必选实参：
# # print(ask_ok('Do you really want to quit? '))

# # #给出一个可选实参：
# # print(ask_ok('OK to overwrite the file? ', 2))

# # #给出所有实参：
# print(ask_ok('OK to overwrite the file? ', 3, 'Come on, only yes or no!'))





# def factorial(number):
#     s = 1
#     for num in range(number, 0, -1): # range(start, end, step)
#         s = s * num

#     return s


# n = int(input('Please input a number: '))
# f = factorial(n)
# print('f = ', f)

# print(list(range(1, 15)))



#def f(a, L=[]):
#    L.append(a)
#    return L
#
#print(f(1))
#print(f(2))
#print(f(3))

# def f(a, L=None):
#     print(L)
#     if L is None:
#         L = []
#     L.append(a)
#     return L

# a = f(1)
# print(a)

# b = f(2, a)
# print(b)

# c = f(3, b)
# print(c)





# def repeat(myname = 'christina', times = 5):
#     for c in range(times):
#         print(myname)

# # repeat(times = 4, myname = 'abc')
# repeat(3, 'aaa')


# def standard_arg(arg):
#     print(arg)

# standard_arg(2)
# standard_arg(arg=2)


# def pos_only_arg(arg, /):
#     print(arg)

# pos_only_arg(2)
# # pos_only_arg(arg=2)


# def kwd_only_arg(*, arg):
#     print(arg)

# # kwd_only_arg(2)
# kwd_only_arg(arg=2)



# def combined_example(pos_only, /, standard, *, kwd_only):
#     print(pos_only, standard, kwd_only)


# combined_example(1, 2, kwd_only=3)
# combined_example(1, standard=2, kwd_only=3)

# 1, int 1,2,3,4
# 2, str 'tom', 'sdfs'
# 3, float 3.5, 6.77777
# 4, dict {name='tom', age=23}
# 5, list [2,4,5,'sdfsd']
# 6, tuple (1,3,4,'sdfs')
# 7, bool true, false




# def test(**arg):         # dict parameters
#     print(type(arg))
#     print(arg)


# test(name='tom', age=88, email='test@gmail.com')


# def test2(*arg):         # tuple parameters
#     print(type(arg))
#     print(arg)


# test2('2222', True, 3, (2,5,7))   # ('2222', True, 3, (2,5,7))


# def test(*arg, **args):
#     for value in arg:
#         print('- ', value)
    
#     for key, value in args.items():
#         print(key, ": ", value)

# test(2,3,4,5,'end', name='tom', age=88, email='test@gmail.com')

# def getMaxScoreKey(**data):
#     max = data.values()
#     print(data)
#     # result = data.keys()[0]
#     # for key,value in data:
#     #     if max > value:
#     #         max = value
#     #         result = key

#     # return result


# print(getMaxScoreKey(tom=23,jack=88,kelly=99,eric=22))


# lst = []

# lst.append('apple')
# lst.append('pear')
# lst.insert(1, 'pineapple')
# lst.append('kiwi friut')

# lst.extend(['strawberry', 'blueberry', 'pear', 'blackberry'])

# # lst.remove('pear')
# # lst.pop()
# # lst.pop(1)

# # lst.clear()
# # lst.append('pear')

# # print(len(lst))
# # idx = lst.index('pear', 3, 7)
# # print(idx)

# lst.sort()
# # lst.reverse()

# # lst.remove('blueberry')
# # lst.pop(2)
# del(lst[2])

# print(lst)



# --------------------------------
# cars = ['Ford', 'BMW', 'Volvo']

# # cars.sort()
# cars.sort(reverse=True)




#Syntax
#list.sort(reverse=True|False, key=myFunc)

# def myFunc(e):
#   return len(e)

# cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
# cars.sort(key=myFunc, reverse=True)


# def myFunc(e):
#   return e['year']

# cars = [
#   {'car': 'Ford', 'year': 2005},
#   {'car': 'Mitsubishi', 'year': 2000},
#   {'car': 'BMW', 'year': 2019},
#   {'car': 'VW', 'year': 2011}
# ]

# cars.sort(key=myFunc)


# print(cars)


# def myFunc(e):
#   return e['math'] + e['English'] + e['Chinese']

# students = [
#   {'name': 'Tom', 'math': 66, 'English': 88, 'Chinese': 80},
#   {'name': 'Kelly', 'math': 55, 'English': 99, 'Chinese': 30},
#   {'name': 'Christna', 'math': 99, 'English': 22, 'Chinese': 95},
#   {'name': 'Jacky', 'math': 0, 'English': 22, 'Chinese': 99},
# ]

# students.sort(key=myFunc, reverse=True)
# print(students)

# lst = []
# for x in range(10):
#     lst.append(x+x+1)

# print(lst)


# comprehension
# lst = [x+x+1 for x in range(10)]
# print(lst)



# lst = []
# for x in range(10):
#     if x % 2 == 0:
#         lst.append(x*x)

# print(lst)

# lst = [x * x for x in range(10) if x % 2 == 0]
# print(lst)


#把1到100之间的所有5的倍数的立方值保存在一个列表里打印出来。
#print out a list of all cubic number of Multiples of 5 between 1 and 100.

#e.g.
# [1,2,3,4,5,6,7,8,9,10,11..........100]
# [5,10,15.....100]
# [5*5*5,10*10*10,....100*100*100]


# lst = [x * x * x for x in range(1,101) if x % 5 == 0]
# print(lst)


# def myfunc(number):
#     # lst = [x * x * x for x in range(1,number+1) if x % 5 == 0]
#     lst = []
#     for x in range(1, number + 1):
#         if x % 5 == 0:
#             lst.append(x * x * x)
#     print(lst)


# myfunc(100)


# 偏函数 (partial function)

# from functools import partial

# def display(name,age):
#     print("name:",name,"age:",age)

# GaryFun = partial(display,name = 'Gary')

# GaryFun(age = 13)


# from functools import partial

# def mod( n, m ):
#   return n % m

# print(mod(100, 7))

# mod_by_100 = partial(mod, 100)
# print(mod_by_100(7))



# print(mod(51, 4))

# mod_by_51 = partial(mod, 51)
# print(mod_by_51(4))



# comprehension
# values = [x**2 for x in range(1, 6)]
# print(values)

# values = []
# for x in range(1, 6):
#     values.append(x**2)

# print(values)


# values = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# print(values)


# values = []

# for x in [1,2,3]:
#   for y in [3,1,4]:
#     if x != y:
#       values.append((x, y))

# print(values)


# 1 * 1 = 1 
# 1 * 2 = 2  2 * 2 = 4
# 1 * 3 = 3  2 * 3 = 6  3 * 3 = 9
# .....


# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d * %d = %d\t' % (j, i, i * j), end='')
#     print()



# vec = [-4, -2, 0, 2, 4]
# # print([x*2 for x in vec])
# print([x**2 for x in vec])
# print([x for x in vec if x >= 0])
# print([x**3 for x in vec if x >= 0])
# print([abs(x) for x in vec])


# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# print([weapon.strip() for weapon in freshfruit])
# # print([weapon.lstrip().rstrip() for weapon in freshfruit])

# #[(0, 0, 0),(1,1,1),(2,4,8),(3,9,27)...]
# print([(x, x**2, x**3) for x in range(6)])

# print([[x, x**2] for x in range(6)])



# vec = [[1,2,3], [4,5,6], [7,8,9]]
# print([num for elem in vec for num in elem])

# values = []
# for elem in vec:
#   for num in elem:
#     values.append(num)
# print(values)



# scores = {'math': 98, 'English': 88}
# for k, v in scores.items():
#     # print(k, v)
#     print("%s:%d" % (k, v))

# lst = ['tic', 'tac', 'toe']
# for i, v in enumerate(lst):
#     print(i, v)


# print(lst[2])



# lst = ['000','101','202','301','402','504','608','709','807','909']
# for i, v in enumerate(lst):
#     if (i % 2 == 0):
#         print(i, v)
#     else:
#         print(i, 'null')




# questions = ['name', 'age', 'favorite color']
# answers = ['tom', '23', 'blue']
# for q, a in zip(questions, answers):
#     # print('{0}?  Answer:{1}'.format(q, a))
#     print('%s?  Answer:%s' % (q, a))

# #range(start, end, step)
# for i in reversed(range(1, 10, 2)):
#     print(i)

# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for i in sorted(basket):
#     print(i)


# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for f in sorted(set(basket)):
#     print(f)


# import math

# raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
# filtered_data = []
# for value in raw_data:
#     if not math.isnan(value):
#         filtered_data.append(value)

# print(filtered_data)


# #HOMEWORK:

# # 学生名单 (Student names list)
# names = ['Tom', 'Kellay', 'Eric', 'Jacky', 'Amy', 'Christina', 'Aurora']
# # 每个学生的选课列表，按顺序一对一 (Each students chose subjects, one by one mapping in order)
# subjects = [
#     ['Math'],
#     ['Math', 'English', 'Music'],
#     ['English', 'Music'],
#     ['Math', 'English'],
#     ['Math', 'Music'],
#     ['Math', 'English', 'Music'],
#     ['Music']
# ]

# # 1，把所有学数学，英语或者音乐的学生名单，单独保存在三个set变量中，并打印到屏幕上(Save all the math, English, or music students individually into three set variables and print it on the screen.)。
# # 2，找到最简单的方法，把所有选择了3门课程的学生名单也打印出来(Find the easiest/quick way to print out a list of all the students who have chosen the 3 subjects.)。

# math_students = set()
# english_students = set()
# music_students = set()
# for name, subs in zip(names, subjects):
#     if 'Math' in subs:
#         math_students.add(name)
#     if 'English' in subs:
#         english_students.add(name)
#     if 'Music' in subs:
#         music_students.add(name)

# print('Math:', math_students)
# print('English:', english_students)
# print('Music:', music_students)

# print('All:', math_students & english_students & music_students)










# # 学生名单 (Student names list)
# names = ['Tom', 'Kellay', 'Eric', 'Jacky', 'Amy', 'Christina', 'Aurora']
# # 每个学生的选课列表，按顺序一对一 (Each students chose subjects, one by one mapping in order)
# subjects = [
#     ['Math'],
#     ['Math', 'English', 'Music'],
#     ['English', 'Music'],
#     ['Math', 'English'],
#     ['Math', 'Music'],
#     ['Math', 'English', 'Music'],
#     ['Music']
# ]
# math_students = set([names[i] for i in range(len(subjects)) if 'Math' in subjects[i]])

# math_students = set()
# math_students = set([])
# math_students = set([
#   names[i] 
#   for i in range(len(subjects)) 
#      if 'Math' in subjects[i]
# ])

# math_students = set()
# for i in range(len(subjects)): # 0 - 6
#     if ('Math' in subjects[i]):
#         math_students.add(names[i])          






# import mymath

# # print(mymath.plus(3,6))
# # print(mymath.minus(3,6))
# # print(mymath.devide(6,3))
# # print(mymath.multiple(3,6))
# # print(mymath.mod(6,3))


# # mymath.fib(100)

# lst = mymath.fib2(100)
# print(lst)


# import math

# print(math.pi)
# print(math.sqrt(4))



# import mymath

# # # print(mymath.plus(8,3))

# print(mymath.PI)


# import myLib

# # print(type(myLib.person1))

# print(myLib.person1['name'])



# # import mymath
# from mymath import fib, plus

# fib(11)
# print(plus(3,9))

# # import mymath
# from mymath import *
# fib(11)
# print(plus(3,9))


# # import mymath
# import mymath as mm
# mm.fib(11)


# from mymath import fib, plus
# from mymath import fib as myfib, plus as myplus
# from yourmath import fib as yourfib, plus as yourplus

# myfib(11)
# yourfib(11)
# print(myplus(3,9))
# print(yourplus(3,9))


# f = open('while.py', 'r', encoding="utf-8")
# # read_data = f.read()
# data = f.readline()
# print(data)

# with open('while.py', 'r') as file:
#     content = file.read()
#     print(content)

# f = open('test_file.py', 'w', encoding="utf-8")
# f.write('This is a test\n')
# f.close()

# with open('test_file.py', 'r') as file:
#     content = file.read()
#     print(content)
# with open('test_file.py', 'r') as file:
#     for i in range(5):
#         line = file.readline()
#         print(line)


# read_data = f.read()
# data = f.readline()
# print(data)


# f = open('test_workfile', 'w')
# f.write('11111111111111')
# f = open('test_workfile', 'w')
# f.write('abcdefghijklmnopq')
# f.close()

# f = open('test_workfile', 'r')
# f.seek(10)
# print(f.read(5))
# print(f.read(10))

# f = open('test_workfile', 'ab') # abcdefghijklmnopqrstuvwxyz
# f.seek(-3, 2)  # f.seek(offset, whence) 
# print(f.read(1))


# 指定目录读写文件
# homework：input many students names, ages, emails and save all into a file.

# -> % please input the number of students: 3
# -> % please input student1's name: Tom
# -> % please input student1's age: 23
# -> % please input student1's email: ttt@tgmail.com
# -> % please input student2's name: Tomson
# -> % please input student2's age: 233
# -> % please input student3's email: ttt0002@tgmail.com
# ....

# write all information into a file.






# f = open('students.csv', 'w')

# number = int(input('please input the number of students: '))
# for i in range(number):
#     name = input('please input student{0}\'s name: '.format(i + 1))
#     age = input('please input student{0}\'s age: '.format(i + 1))
#     email = input('please input student{0}\'s email: '.format(i + 1))

#     f.write('{0},{1},{2}\n'.format(name, age, email))

# f.close()

# print()
# print()
# print('File contents:')
# with open('students.csv', 'r') as file:
#     content = file.read()
#     print(content)

# f = open('students.csv', 'r')
# content = f.read()
# print(content)
# f.close()



# with open('students.csv', 'r') as file:
#     for line in file:
#         print(line, end='')

# f = open('students.csv', 'r')
# for line in f:
#     print(line, end='')
# f.close()



# def divide(x, y):
#     result = x / y
#     print(result)

# divide(42, 0)

# def divide(x, y):
#     try:
#         result = x / y
#         print("result is", result)
#     except ZeroDivisionError:
#         print("division by zero!")
#     except TypeError:
#         print("division type is wrong!")
#     except:
#         print("Unknown exception occurred")
#     else:
#         print("Success")
#     finally:
#         print("-- END --")

# divide(2, 1)
# print()
# divide(2, 0)
# print()
# divide("2", "1")

# Results:
# result is 2.0
# Success
# -- END --

# division by zero!
# -- END --

# Unknown exception occurred
# -- END --




# class Dog:

#     kind = 'canine'         # 类变量被所有实例所共享

#     def __init__(self, name):
#         self.name = name    # 实例变量为每个实例所独有

#     def set_kind(self, kind):
#         self.kind = kind

# d = Dog('Fido')
# d.set_kind('ttt')


# print(d.kind)




# class Person:
#     name = 'no name'
#     age = 10
#     iq = 90
#     birthday = '2001-01-01'

#     def __init__(self, name, age = 99):
#         self.name = name
#         self.age = age

#     def print_info(self):
#         print(self.name, self.age, self.iq, self.birthday)

#     def set_age(self, age):
#         self.age = age

#     def set_iq(self, iq):
#         self.iq = iq

#     def set_birthday(self, birthday):
#         self.birthday = birthday


# person1 = Person('Tom')
# person1.set_age(18)
# person1.set_iq(10)
# person1.set_birthday('2022-12-12')
# person1.birthday = '2002-12-12'
# person1.print_info()


# person2 = Person('Kelly', 11)
# person2.print_info()




# class Dog:

#     kind = 'canine'         # 类变量被所有实例所共享
#     # leg_number = 4

#     def __init__(self, name):
#         self.name = name    # 实例变量为每个实例所独有
#         self.kind = ''


# dog1 = Dog('Fido')
# dog2 = Dog('Buddy')

# # print(dog1.name)
# # print(dog2.name)

# print(dog1.kind)
# print(dog2.kind)

# print(id(dog1.kind))
# print(id(dog2.kind))

# dog2.kind = 'poodle'

# print(dog1.kind)
# print(dog2.kind)

# print(id(dog1.kind))
# print(id(dog2.kind))





# class Dog:

#     # tricks = []             # 类变量的错误用法

#     def __init__(self, name):
#         self.name = name
#         self.tricks = []    # 为每个 Dog 实例新建一个空列表

#     def add_trick(self, trick):
#         self.tricks.append(trick)




# dog1 = Dog('Fido')
# dog2 = Dog('Buddy')

# dog1.add_trick('roll over')
# dog1.add_trick('play thx')

# dog2.add_trick('play dead')

# print(dog1.tricks)
# print(dog2.tricks)





# class CLanguage:
#     # 下面定义了2个类变量
#     name = "C语言中文网"
#     add = "http://c.biancheng.net"

#     # 下面定义了一个say实例方法
#     def say(self, content):
#         print(content)




#使用类名直接调用
# print(CLanguage.name)
# print(CLanguage.add)

# #修改类变量的值
# CLanguage.name = "Python教程"
# CLanguage.add = "http://c.biancheng.net/python"
# print(CLanguage.name)
# print(CLanguage.add)

# create a class object
# clang = CLanguage()
# print(clang.name)
# print(clang.add)







# print("-- 修改前，各类对象中类变量的值 --")
# a = CLanguage()
# print(a.name)
# print(a.add)
# b = CLanguage()
# print(b.name)
# print(b.add)
# print("-- END --")

# print("-- 修改后，各类对象中类变量的值 --")
# CLanguage.name = "tttttt"
# CLanguage.add = "python"
# print(a.name)
# print(a.add)
# print(b.name)
# print(b.add)
# print("-- END --")




# class Language :
#     name = "default name"
#     address = "default address"
#     def __init__(self, name, address):
#         self.address = address

#     def display(self):
#         print(self.name, self.address)


# a = Language("AAAA", "A address") #automatically
# print(a.name)
# print(id(a.name))
# print(a.address)
# print(id(a.address))

# b = Language("BBBB", "B address")
# print(b.name)
# print(id(b.name))
# print(b.address)
# print(id(b.address))

# # c = Language("CCCC", "C address")
# # print(c.name)
# # print(id(c.name))
# # print(c.address)
# # print(id(c.address))

# print(Language.name)
# print(id(Language.name))
# print(Language.address)
# print(id(Language.address))



# class CLanguage:
#     #类构造方法，也属于实例方法
#     def __init__(self):
#         self.name = "C语言中文网"
#         self.add = "http://c.biancheng.net"
#     # 下面定义了一个say实例方法
#     def say(self):
#         print("正在调用 say() 实例方法")




# class CLanguage:
#     #类构造方法，也属于实例方法
#     def __init__(self):
#         self.name = "C语言中文网"
#         self.add = "http://c.biancheng.net"
#     #下面定义了一个类方法
#     @classmethod
#     def info(cls):
#         print("正在调用类方法",cls)


# class CLanguage:
#     # 静态方法
#     @staticmethod
#     def info(name,add):
#         print(name,add)



# userName = input("Please enter your name: ")

# if all(x.isalpha() or x.isspace() for x in userName):
#     print("Welcome %s!" % userName)
# else:
#     print("Only alphabetical letters and spaces are allowed in your names.")



# x.isalpha() and x.isspace() for x in userName


# print([x.isalpha() or x.isspace() for x in userName])



# print('  || = = = = = = = = = = = = = =')
# print('  |  /                 |')
# print('  |/                   |')
# print('  ||                 {$ $}')
# print('  ||               /{  :  }\\')
# print('  ||                  |||')
# print('  ||                 <===>')
# print('  ||')
# print('  ||')
# print('  ||')
# print('  ||')
# print('  ||')


# def draw_tree(times):
#     if times <= 3:
#         draw_repeat_part(times)

#     if times == 4:
#         print('  || = =')
#         print('  |  /')
#         print('  |/')
#         print('  ||')
#         draw_repeat_part(3)

#     if times == 5:
#         print('  || = = = = = = = = = = = = = =')
#         print('  |  /')
#         print('  |/')
#         print('  ||')
#         draw_repeat_part(3)
    
#     if times == 6:
#         print('  || = = = = = = = = = = = = = =')
#         print('  |  /                 |')
#         print('  |/                   |')
#         print('  ||                 {$ $}')
#         draw_repeat_part(3)

#     if times == 7:
#         print('  || = = = = = = = = = = = = = =')
#         print('  |  /                 |')
#         print('  |/                   |')
#         print('  ||                 {$ $}')
#         print('  ||               /{  :  }\\')
#         print('  ||                  |||')
#         print('  ||                 <===>')
#         draw_repeat_part(2)

# def draw_repeat_part(times):
#     for i in range(times):
#         print('  ||')
#         print('  ||')
#         print('  ||')


# draw_tree(7)


# for i, letter in enumerate('PoPabc'):
#     print(i, letter)


indices = [i for i, letter in enumerate('PoPabca') if letter == 'a']
print(indices)


new_state = list('_______')
print(new_state)
for i in indices:
    new_state[i] = 'a'

print(new_state)

