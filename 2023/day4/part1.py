def get_nums(nums):
  return set(int(num) for num in nums.split(' ') if num != '')

filename = "data.txt"

with open(filename, 'r') as file:
  data = file.read().split('\n')

total = 0

for line in data:
  count = 0
  _cards, _nums = line.split('|')
  cards = get_nums(_cards[_cards.index(':') + 1:])
  nums = get_nums(_nums)
  for num in nums:
    if num in cards:
      count = count * 2 if count else 1
  total += count

print(total)