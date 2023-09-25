# def 函数名(参数列表):
#     //实现特定功能的多行代码
#     [return [返回值]]

# def func_name(parameters):
#     //codes
#     [return [value]]



# 1, make a function which name is sum, it will calculate the total of three values.
# e.g.    
# print(sum(3,6,8)) # 17
# print(sum(1,9,8)) # 18



# def sum(num1, num2, num3):
#     total = num1 + num2 + num3
#     return total

# # a = int(input('Please input a: '))
# # b = int(input('Please input b: '))
# # c = int(input('Please input c: '))
# # print('The total of %d, %d and %d is %d.' % (a, b, c, sum(a, b, c)))


# print(sum(1,2,3))
# print(sum(1,22,3))
# print(sum(1,2,33))
# print(sum(1,2,34))
# print(sum(1,2,35))
# print(sum(1,2,36))














# 2, make a function which name is max, it return the max value of these three numbers.
# e.g.
# print('the max number of %d, %d and %d is %d.' % (a,b,c,max(a,b,c)))





# def maxNumber(*numbers):
#     max = numbers[0]
#     for number in numbers:
#         if max < number:
#             max = number
    
#     return max


# print(maxNumber(1,3,6,8,9,0,99,66,44,88,77))
# print(maxNumber(34,12,56,89,98,32,14,56,32))
# print(maxNumber(9,11,4,77,3,67,35,23,25,47))




# numbers = (1,22,33,14,5,16,7)
# max = numbers[0]
# for number in numbers:
#     if max < number:
#         max = number

# print(max)



# newlist = [i for i in range(2, 100) if i % 2 != 1]
# print(newlist)





# number = int(input('Please input a number '))

# if number % 2 == 0:
#     print('no')
# else:
#     print('yes')


# number = int(input('Please input a number '))

# if number % 2 == 1:
#     print('yes, your number is a odd number')
# else:
#     print('no, your number is not a odd number')



# def maxEvenNumber(*numbers):
#     maxEven = 3
#     for number in numbers:
#         if number % 2 == 0:
#             maxEven = number
#             break

#     if maxEven == 3:
#         return 'It does not have a even number.'
#     else:
#         return 'It has a even number.'

#         # if maxEven < number:
#         #     maxEven = number
    
#     # return max


# print(maxEvenNumber(1,3,6,8,9,0,99,66,44,88,77))
# print(maxEvenNumber(33,11,51,89,93,31,13,55,31))
# print(maxEvenNumber(9,11,4,77,3,67,35,23,25,47))




    # evenlist = []
    # for number in numbers:
    #     if number % 2 == 0:
    #         evenlist.append(number)
    
    # # evenlist = [number for number in numbers if number % 2 == 0]

    # if len(evenlist) == 0:



# def maxEvenNumber(*numbers):
#     # lstEven = []
#     # for number in numbers:
#     #     if number % 2 == 0:
#     #         lstEven.append(number)

#     lstEven = [number for number in numbers if number % 2 == 0]

#     if len(lstEven) == 0:
#         return None
#     else:
#         max = lstEven[0]
#         for value in lstEven:
#             if max < value:
#                 max = value
#         return max



# # maxEvenNumber(1,3,6,8,9,0,99,66,44,88,77)
# # maxEvenNumber(33,11,51,89,93,31,13,55,31)
# # maxEvenNumber(9,11,4,77,3,67,35,23,8,47)
# print(maxEvenNumber(1,3,6,8,9,0,99,66,44,88,77))
# print(maxEvenNumber(33,11,51,89,93,31,13,55,31))
# print(maxEvenNumber(9,11,4,77,3,67,35,23,25,47))



# str = 'abcdefg'

# for char in str:
#     print(char)


# str = input('please input a string: ')
# # print(len(str))

# n = 0
# for char in str:
#     n = n + 1

# print(n)



# def my_len(myString):
#     n = 0
#     for char in myString:
#         n = n + 1
#     return n



# str = input('please input a string: ')
# print(my_len(str))


# 作业1：定义一个函数sum(number1, number2, number3), 用如下代码调用函数。
#     print(sum(1, 2, 3)) #输出结果：6
#     print(sum(11, 22, 33)) #输出结果：66
#     print(sum(31, 23, 35)) #输出结果：89


# def sum(number1, number2, number3):
#     return number1 + number2 + number3


# print(sum(3, 5, 8))
# print(sum(12, 34, 56))
# print(sum(9, 11, 15))









# 作业2：定义一个函数max(number1, number2, number3), 用如下代码调用函数。
#     print(max(1, 22, 3)) #输出结果：22
#     print(max(111, 22, 33)) #输出结果: 111
#     print(max(31, 23, 35)) #输出结果：35

# def maxNumber(number1, number2, number3):
#     if number1 < number2:
#         if number2 < number3:
#             return number3
#         else:
#             return number2
#     else:
#         if number1 > number3:
#             return number1
#         else:
#             return number3
    
# print(maxNumber(3, 5, 8))
# print(maxNumber(12, 34, 56))
# print(maxNumber(9, 11, 15))



# Practice 1: define a function, it's name is checkAge(age), 
# age <= 11 return 'Child'
# age < 18 return 'Teenager'
# age <= 49 return 'Adult'
# all else return 'Elder'

# def checkAge(age):
#     if age <= 11:
#         return 'Child'
#     if age < 18:
#         return 'Teenager'
#     if age <= 49:
#         return 'Adult'
#     else:
#         return 'Elder'


# # #input an age, print the value of the function returned.
# age = int(input('Please input your age '))
# print(checkAge(age))




# lst = [1,2,3,4,5,'234','4455',4,5]    
# # print(len(lst))

# # n = 0
# # for element in lst:
# #     n = n + 1

# # print(n)



# def lenList(lst):
#     n = 0
#     for ele in lst:
#         n = n + 1

#     return n





# print(lenList([1,4,5,'234','4455',5,6,7,8,9]))
# print(lenList(lst))




# for n in range(15):
#     for n in range(10):
#         print('*', end = '')
#     print('')



# for n in range(15):
#     for n in range(10):
#         print('*', end = '')
#     print('')

# print(range(8))


# 1, ********************
# lst = [1,2,3,1,2,3,4,5,6,4,4,4,4,4,4,4,4,4,4,6,7,5,8,9,0]
# test = []
# for x in lst:
#     if x not in test:
#         test.append(x)

# print(test)

# print(list(set(lst)))

# 2, ********************
# name = 'Tom'
# print(f"{name} is stupid")

# 3, ********************
# 门牌号 （101 - 508）

# 4, ********************
# 小球从100米高度下坠，每次反弹原来高度的一半，10次后落地不再弹起，问一共经历的多少米？



