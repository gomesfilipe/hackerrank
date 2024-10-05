from typing import List, Dict
from abc import ABC

class Formatter(ABC):
  def combine(self, words: List[str]) -> str:
    var: str = ''

    for i, word in enumerate(words):
      if i != 0:
        var += word[0].upper() + word[1:]
      else:
        var += word
    return var

  def split(self, var: str) -> List[str]:
    words: List[str] = []
    curr_word: str = ''

    for c in var:
      if c.isupper():
        words.append(curr_word)
        curr_word = c.lower()
      else:
        curr_word += c

    words.append(curr_word)
    return words

class VariableFormatter(Formatter):
  pass

class MethodFormatter(Formatter):
  def combine(self, words: List[str]) -> str:
    return super().combine(words) + '()'

  def split(self, var: str) -> List[str]:
    return super().split(var[:-2])

class ClassFormatter(Formatter):
  def combine(self, words: List[str]) -> str:
    combined: str = super().combine(words)
    return combined[0].upper() + combined[1:]

  def split(self, var: str) -> List[str]:
    return super().split(var[0].lower() + var[1:])

formatter: Dict[str, Formatter] = {
  'V': VariableFormatter(),
  'M': MethodFormatter(),
  'C': ClassFormatter(),
}

while True:
  try:
    command, type, param = input().split(';')
    param = param.strip()

    if command == 'C':
      print(formatter[type].combine(param.split()))
    else:
      print(' '.join(formatter[type].split(param)))
  except:
    break
