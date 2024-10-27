t = int(input())

for _ in range(t):
  n = int(input())

  right_zeros = 0
  ones = 0

  aux = n

  while True:
    if aux % 2 == 0:
      right_zeros += 1
      aux >>= 1
    else:
      break

  while aux:
    if aux % 2 == 1:
      ones += 1
    aux >>= 1

  if (right_zeros + ones) % 2 == 1:
    print('Richard')
  else:
    print('Louise')
