for i in range(1, 10):
  for j in range(1, i+1):
    print('{:d} * {:d} = {:d}'.format(j, i, j*i), end = '')
    if j != i:
      print(',', end = '')
    print('\t', end = '')
  print('')

