n = int(input())
arr = [int(i) for i in input().split()]

d = {}
count = 0

for i in arr:
  if i in d:
    d[i] += 1
  else:
    d[i] = 1

  if d[i] % 2 == 0:
    count += 1

print(count)
