def count_chars(s: str):
  d = {}

  for c in s:
    if c in d:
      d[c] += 1
    else:
      d[c] = 1

  return d

def solve(s: str):
  lenn = len(s)

  if lenn % 2 == 1:
    print(-1)
    return

  mid = lenn // 2
  left =  s[:mid]
  right = s[mid:]

  count_left = count_chars(left)

  ans = mid
  for c in right:
    if count_left.get(c, 0) > 0:
      count_left[c] -= 1
      ans -= 1

  print(ans)

q = int(input())

for _ in range(q):
  solve(input())
