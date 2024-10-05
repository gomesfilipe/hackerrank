def next_multiple_of_5(i: int) -> int:
  return i + 5 - (i % 5)

def round_grade(grade: int) -> int:
  nextt = next_multiple_of_5(grade)

  if grade < 38:
    return grade
  elif nextt - grade < 3:
    return nextt
  else:
    return grade

n = int(input())

for i in range(n):
  grade = int(input())

  print(round_grade(grade))
