# students = [
#     ['Tom',13,[65, 77, 88, 90, 100]],
#     [
#         'Lily',
#         12,
#         [99, 75, 98, 90, 99]
#     ],
#     ['Lucy', 13, [80, 88, 88, 95, 98]],
#     ['Eric', 11, [78, 89, 80, 92, 78]],
#     ['Christina', 13, [99, 89, 100, 100, 98]],
# ]





# print('-----------------------------------------------------------------------')
# print('|    NAME   |  AGE  |   Math  | English |  Coding | Drawing |  Music  |')
# print('-----------------------------------------------------------------------')
# for student in students:
#     print('| %-10s' % student[0], end = '')
#     print('|%10d   ' % student[1], end = '')
#     for score in student[2]:
#         print('|%6d   ' % score, end = '')
#     print('｜')
#     print('-----------------------------------------------------------------------')



# students = {}

# number = int(input('please input the number of students: '))
# for i in range(1, number + 1):
#     name = input('The name of No.%d student: ' % i)

#     students[name] = {}
#     students[name]['age'] = input('No.%d student\'s age: ' % i)
#     students[name]['gender'] = input('No.%d student\'s gender: ' % i)
#     students[name]['email'] = input('No.%d student\'s email: ' % i)
#     students[name]['id'] = input('No.%d student\'s ID: ' % i)
#     students[name]['phone'] = input('No.%d student\'s phone: ' % i)

# print(students)




# students = []

# number = int(input('Please input the number of students: '))
# for i in range(0, number):
#     student = {}
#     student['name'] = input('please input the name of No.%d: ' % (i+1))
#     student['age'] = input('please input the age of No.%d: ' % (i+1))
#     student['gender'] = input('please input the gender of No.%d: ' % (i+1))
#     student['email'] = input('please input the email of No.%d: ' % (i+1))
#     student['id'] = input('please input the id of No.%d: ' % (i+1))
#     student['phone'] = input('please input the phone of No.%d: ' % (i+1))

#     students.append(student)


# students = 
# [
#     {'name': 'l', 'age': '8', 'gender': 'f', 'email': 'mm', 'id': 'mmmnmnmnm', 'phone': '0274126031'},
#     {'name': 'm', 'age': '9', 'gender': 'm', 'email': 'lllll', 'id': 'ghgh', 'phone': 'k'}
# ] 

# print(students[87]['email'])

# {
#     'popo': {'age': '9', 'gender': 'f', 'email': 'popo@gmail.com', 'id': '27803931', 'phone': '0274126031'},
#     'lol': {'age': '10', 'gender': 'f', 'email': 'lol@gmail.com', 'id': '10101010', 'phone': '83749201'}
# }

# print(students['popo']['email'])


{
    1, 
    2, 
    3, 
    (4,5,6), 
    True, 
    'test', 
    3.33
}


# students = []

# number = int(input('Please input the number of students: '))
# for i in range(0, number):
#     student = {}
#     student['name'] = input('please input the name of No.%d: ' % (i+1))
#     student['age'] = input('please input the age of No.%d: ' % (i+1))
#     student['gender'] = input('please input the gender of No.%d: ' % (i+1))
#     student['email'] = input('please input the email of No.%d: ' % (i+1))
#     student['id'] = input('please input the id of No.%d: ' % (i+1))
#     student['phone'] = input('please input the phone of No.%d: ' % (i+1))

#     students.append(student)

# for student in students:
#     # print(student.items())
#     for key,value in student.items():
#         print("\n-----------------------")
#         print(key ," ", value)


# students = {
#     'eric': {
#         'age': '9', 
#         'gender': 'm', 
#         'email': 'popo@gmail.com', 
#         'id': '27803931', 
#         'phone': '0274126031'
#         },
#     'christina': {'age': '10', 'gender': 'f', 'email': 'lol@gmail.com', 'id': '10101010', 'phone': '83749201'}
# }

# print(students['eric']['age'])






