def sos(i: int):
  if i % 3 == 1:
    return 'O'
  return 'S'

s = input()
count = 0

for i in range(len(s)):
  if s[i] != sos(i):
    count += 1

print(count)
