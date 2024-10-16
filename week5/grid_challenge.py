def solve(mat: list[list[str]], n: int, m: int):
  for j in range(m):
    for i in range(1, n):
      if mat[i][j] < mat[i - 1][j]:
        return False
  return True

t = int(input())

for _ in range(t):
  n = int(input())
  mat = []
  for __ in range(n):
    mat.append(sorted(input()))

  m = len(mat[0])

  if solve(mat, n, m):
    print('YES')
  else:
    print('NO')
