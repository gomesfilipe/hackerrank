def freq(arr: list[int]) -> dict[int, int]:
  f = {}

  for i in arr:
    f[i] = f.get(i, 0) + 1

  return f

n = int(input())
arr = [int(i) for i in input().split()]
m = int(input())
brr = [int(i) for i in input().split()]

count_a = freq(arr)
count_b = freq(brr)

ans = []

for i, f in count_b.items():
  if f > count_a.get(i, 0):
    ans.append(i)

ans.sort()
print(' '.join([str(s) for s in ans]))
