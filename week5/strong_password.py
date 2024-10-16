def solve(s: str) -> bool:
  report = {
    'numeric': False,
    'lower': False,
    'upper': False,
    'special': False,
  }

  special = '!@#$%^&*()-+'

  for c in s:
    if c.isnumeric():
      report['numeric'] = True
    elif c.islower():
      report['lower'] = True
    elif c.isupper():
      report['upper'] = True
    elif c in special:
      report['special'] = True

  count = 0

  for passed in report.values():
    if not passed:
      count += 1

  if len(s) + count >= 6:
    return count
  return 6 - len(s)

n = int(input())
s = input()

print(solve(s))
