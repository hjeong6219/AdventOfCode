from collections import deque

def get_nums(nums):
  return set(int(num) for num in nums.split(' ') if num != '')

filename = "data.txt"

with open(filename, 'r') as file:
  data = file.read().split('\n')

total = 0
copies = deque()

for line in data:
  count = 0
  _cards, _nums = line.split('|')
  cards = get_nums(_cards[_cards.index(':') + 1:])
  nums = get_nums(_nums)
  if copies:
    current_score = copies.popleft() + 1
  else:
    current_score = 1
  for num in nums:
    if num in cards:
      count += 1
  if count:
    for index in range(count):
      try:
        copies[index] += current_score
      except IndexError:
        copies.append(current_score)
  total += current_score

print(total)