n = int(input())
arr = [int(i) for i in input().split()]
arr.sort()
print(arr[n // 2])
