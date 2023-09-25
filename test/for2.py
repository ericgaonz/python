
n = 0
for i in range(1, 40, 2):
  for k in range(1, 20 - n):
    print(' ', end = '')
  n = n + 1
  for j in range(1, i+1):
    print('*', end = '')
  print('')

