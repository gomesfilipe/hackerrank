n = int(input())
arr = [int(x) for x in input().split()]

min_break = 0
max_break = 0

maxx = arr[0]
minn = arr[0]

for i in range(1, n):
  if arr[i] < minn:
    minn = arr[i]
    min_break += 1

  elif arr[i] > maxx:
    maxx = arr[i]
    max_break += 1

print(f'{max_break} {min_break}')
