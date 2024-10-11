def same_signal(a: int, b: int) -> bool:
  return a * b > 0 or a == 0 and b == 0

x1, v1, x2, v2 = [int(i) for i in input().split()]

if x1 == x2:
  yes = True
elif v1 == v2:
  yes = False
elif same_signal(x1 - x2, v2 - v1):
  t = (x1 - x2) / (v2 - v1)
  yes = t == int(t)
else:
  yes = False

print('YES' if yes else 'NO')
