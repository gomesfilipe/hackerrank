n = int(input())

count = 0

while n:
  if not (n & 1):
    count += 1
  n >>= 1

print(1 << count)
