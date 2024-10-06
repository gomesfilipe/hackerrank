n = int(input())
arr = [int(i) for i in input().split()]

counter = [0, 0, 0, 0, 0]

for i in arr:
  counter[i - 1] += 1

max_id = 1
max_qtd = 0

for i, c in enumerate(counter):
  if c > max_qtd:
    max_id = i + 1
    max_qtd = c

print(max_id)
