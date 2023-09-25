# scores = [
#     [1, [12,13,14,[15,34,67,78]]],
#     [2, [23,45,67,[45,87,89,111]]],
#     [3, [45,7878,56,[45]]],
#     [4, [67,7,7,[78,67]]]
# ]


# for score in scores:
#     for level1 in score:
#         if type(level1) != list:
#             print('(%10d),' % level1, end = '')
#         else:
#             for level2 in level1:
#                 if type(level2) != list:
#                     print('(%10d),' % level2, end = '')
#                 else:
#                     for level3 in level2:
#                         print('(%10d),' % level3, end='')
#     print()