n = int(input())
arr = [int(i) for i in input().split()]
arr.sort()

min_diff = arr[1] - arr[0]
x = [arr[0], arr[1]]

for i in range(2, len(arr)):
  diff = arr[i] - arr[i - 1]

  if diff < min_diff:
    min_diff = diff
    x = [arr[i - 1], arr[i]]
  elif diff == min_diff:
    x.append(arr[i - 1])
    x.append(arr[i])

for i in range(len(x)):
  if i == len(x) - 1:
    end = '\n'
  else:
    end = ' '

  print(x[i], end = end)
