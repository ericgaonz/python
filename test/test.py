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



lst = [1,2,3,1,2,3,4,5,6,4,4,4,4,4,4,4,4,4,4,6,7,5,8,9,0]
newlst = []

for x in lst:
    if x not in newlst:
        newlst.append(x)

print(newlst)
    


# def removeDuplicates(lst):
#     newlst = []
#     for x in lst:
#         if x not in newlst:
#             newlst.append(x)

#     return newlst


# # myLst = removeDuplicates(lst)
# # print(myLst)


# print(removeDuplicates([1,2,3,2,3,4,534,34,56,67,68,67]))


# myset = {1,4,3,2,5,2,3,4,5,6,74,7}
# print(myset)

lst = list(set(lst))
print(lst)


# set(lst)