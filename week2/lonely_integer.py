d = {}

n = int(input())
arr = [int(i) for i in input().split()]

for i in arr:
  if i in d:
    del d[i]
  else:
    d[i] = True

print(list(d.keys())[0])
