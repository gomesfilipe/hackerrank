t = int(input())

for _ in range(t):
  n, m = [int(i) for i in input().split()]

  if m == 1 or n % 2 == 0:
    print(2)
  else:
    print(1)
