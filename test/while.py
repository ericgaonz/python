

i = 1
while i <= 5:
  num = float(input('Please input the value of number {:d}: '.format(i)))

  # how to break loop or continue next loop
  if (i == 1):
    max = num
    min = num

    i += 1
    continue

  if (num >= max):
    max = num

  if (num <= min):
    min = num

  i += 1

print('The biggest num is:', max)
print('The smallest num is:', min)



