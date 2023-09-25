numbers = []
sum = 0
for i in range(0, 5):
  num = float(input('Number {0}: '.format(i+1)))
  numbers.append(num)
  sum = sum + numbers[i]
avy = sum / 5

print('sum=', sum)
print('avy=', avy)
print('numbers=', numbers)
print('numbers[2]=', numbers[2])

