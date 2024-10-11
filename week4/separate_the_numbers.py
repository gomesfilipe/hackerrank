from typing import Tuple, Optional

def is_beautiful(s: str) -> Optional[int]:
  first = None
  curr = ''
  for i in range(1, len(s)):
    first = s[:i]

    if first[0] == '0' and i != 1:
      continue

    first = int(first)

    prev = first
    curr = ''
    for j in range(i, len(s)):
      curr += s[j]

      if curr[0] == '0':
        break

      curr_int = int(curr)
      if curr_int == prev + 1:
        prev = curr_int
        curr = ''

    if curr == '':
      return first
  return None

q = int(input())

for _ in range(q):
  first = is_beautiful(input())

  if first is None:
    print('NO')
  else:
    print(f'YES {first}')
