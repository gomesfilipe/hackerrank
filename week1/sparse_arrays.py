n = int(input())

strs = []
for _ in range(n):
  strs.append(input())


m = int(input())
queries = []
for _ in range(m):
  queries.append(input())

counter = {}

for s in strs:
  if s in counter:
    counter[s] += 1
  else:
    counter[s] = 1

for q in queries:
  print(counter.get(q, 0))
