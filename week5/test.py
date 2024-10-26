t1, t2, n = [int(i) for i in input().split()]
print(t1, t2, n)
for i in range(3, n + 1):
  k = t2
  t2 = t1 + t2 * t2
  t1 = k

ans = ''
while t2:
  ans = str(t2 % 10) + ans
  t2 //= 10


print(ans)
