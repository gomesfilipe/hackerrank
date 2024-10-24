class Item():
  def __init__(self, integer: int, string: str, id: int) -> None:
    self.integer = integer
    self.string = string
    self.id = id

class ItemManager():
  def __init__(self, items: list[Item]) -> None:
    self.items = items

  def should_replace(self, item: Item) -> bool:
    return item.id <= (len(self.items) - 1) / 2

  def format(self, item: Item) -> str:
    return '-' if self.should_replace(item) else item.string

  def sort(self) -> None:
    self.items.sort(key = lambda item: item.integer)

  def __str__(self) -> str:
    return ' '.join([self.format(item) for item in self.items])

n = int(input())

items = []

for id in range(n):
  integer, string = input().split()
  items.append(Item(int(integer), string, id))

manager = ItemManager(items)
manager.sort()
print(manager)
