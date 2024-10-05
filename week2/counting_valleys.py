n = int(input())
path = input()

height = 0
count = 0

for step in path:
  if step == 'U':
    height += 1
  else:
    height -= 1

  if height == 0 and step == 'U':
    count += 1

print(count)
