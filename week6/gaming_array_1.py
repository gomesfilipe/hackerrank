def init_index_of(arr: list[int]):
  d = {}
  for i in range(len(arr)):
    d[arr[i]] = i
  return d


g = int(input())

for _ in range(g):
  # print('------------------')
  n = int(input())
  arr = [int(i) for i in input().split()]
  index_of = init_index_of(arr)
  arr.sort(reverse = True)
  # print(index_of, arr)
  count = 0
  biggest_index = float('inf')

  for i in arr:
    if index_of[i] < biggest_index:
      biggest_index = index_of[i]
      count += 1

  if count & 1:
    print('BOB')
  else:
    print('ANDY')
