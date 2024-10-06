def strings_xor(s: str, t: str):
  res = ''
  for i in range(len(s)):
    if s[i] == t[i]:
      res += '0'
    else:
      res += '1'

  return res

s = input()
t = input()
print(strings_xor(s, t))
