n = int(input())
arr = [int(i) for i in input().split()]
arr.sort()

i = 0
j = 1
maxx = 1

while j < n:
  if arr[j] - arr[i] <= 1:
    maxx = max(maxx, j - i + 1)
    j += 1
  else:
    i += 1

print(maxx)
