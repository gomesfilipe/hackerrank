n = int(input())
arr = [int(x) for x in input().split()]

count = {
  -1: 0,
  0: 0,
  1: 0,
}

for i in arr:
  if i > 0:
    count[1] += 1
  elif i < 0:
    count[-1] += 1
  else:
    count[0] += 1

print(f'{count[1] / n:.6f}')
print(f'{count[-1] / n:.6f}')
print(f'{count[0] / n:.6f}')
