from math import sqrt

n, m = [int(i) for i in input().split()]
arr1 = [int(i) for i in input().split()]
arr2 = [int(i) for i in input().split()]

common = set([i for i in range(1, 101)])

for i in arr2:
  curr = set()

  for j in range(1, int(sqrt(i)) + 1):
    if i % j == 0:
      curr.add(j)
      curr.add(i // j)

  common = common.intersection(curr)

for i in arr1:
  for j in common.copy():
    if j % i != 0:
      common.remove(j)

print(len(common))
