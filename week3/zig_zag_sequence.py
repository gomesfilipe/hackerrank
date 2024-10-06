t = int(input())

for _ in range(t):
  n = int(input())
  arr = [int(i) for i in input().strip().split()]
  arr.sort()
  mid = n // 2
  half1 = arr[:mid]
  half2 = arr[mid:]
  half2.reverse()
  print(' '.join([str(i) for i in half1 + half2]).strip())
