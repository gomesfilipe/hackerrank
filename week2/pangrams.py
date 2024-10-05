s = input()

letters = set()

for c in s:
  if c == ' ':
    continue

  letters.add(c.lower())

if len(letters) == 26:
  print('pangram')
else:
  print('not pangram')
