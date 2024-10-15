n = int(input())
k = int(input())
arr = [int(input()) for i in range(n)]
arr.sort()

minn = arr[k - 1] - arr[0]

for i in range(1, n - k + 1):
  minn = min(minn, arr[i + k - 1] - arr[i])

print(minn)
