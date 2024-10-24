t = int(input())

for _ in range(t):
  n = int(input())
  arr = [int(i) for i in input().split()]

  res = 0

  for i in range(len(arr)):
    if (i + 1) * (len(arr) - i) % 2 == 1:
      res ^= arr[i]
  print(res)
