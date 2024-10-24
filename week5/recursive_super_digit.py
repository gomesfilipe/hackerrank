def sum_digits(n: str) -> int:
  summ = 0

  for c in n:
    summ += int(c)

  return summ

def super_digit(n: int) -> int:
  if n < 10:
    return n

  return super_digit(sum_digits(str(n)))

n, k = input().split()

print(super_digit(sum_digits(n) * int(k)))
