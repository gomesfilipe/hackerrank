n, q = [int(i) for i in input().split()]
queries = [input().split() for _ in range(q)]
arr = [[] for _ in range(n)]
last_answer = 0

for query in queries:
  tyype, x, y = query
  x = int(x)
  y = int(y)
  idx = (x ^ last_answer) % n

  if tyype == '1':
    arr[idx].append(y)
  else:
    last_answer = arr[idx][y % len(arr[idx])]
    print(last_answer)
