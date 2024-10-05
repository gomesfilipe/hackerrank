n = int(input())

for i in range(1, n + 1):
  mult3 = i % 3 == 0
  mult5 = i % 5 == 0

  if mult3 and mult5:
    print('FizzBuzz')
  elif mult3:
    print('Fizz')
  elif mult5:
    print('Buzz')
  else:
    print(i)
