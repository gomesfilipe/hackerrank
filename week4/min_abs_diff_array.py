n = int(input())
arr = [int(i) for i in input().split()]
arr.sort()

min_diff = arr[1] - arr[0]

for i in range(2, len(arr)):
  min_diff = min(min_diff, arr[i] - arr[i - 1])

print(min_diff)
