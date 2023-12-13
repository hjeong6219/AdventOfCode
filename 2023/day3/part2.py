import math

def get_neighbors(r, j, k):
  start = (r - 1 if r != 0 else 0, j - 1 if j != 0 else 0)
  end = (r + 1 if r != row - 1 else r, k + 1 if k != col - 1 else k)
  return start, end

def get_gear_neighbors(r, c):
  start = (r - 1 if r != 0 else 0, c - 1 if c != 0 else 0)
  end = (r + 1 if c != row - 1 else r, c + 1 if c != col - 1 else c)
  return start, end

def ranges_overlap(start, end, num):
  for pos in range(num['pos'][0], num['pos'][1] + 1):
    if start[0] <= num['row'] <= end[0] and start[1] <= pos <= end[1]:
      return int(''.join(grid[num["row"]][num["pos"][0]: num["pos"][1] + 1]))

filename = "data2.txt"

with open(filename, 'r') as file:
    data = file.read().split('\n')

special_char = ['!', '@', '#', '$', '%', '^', '&', '(', ')', '-', '_', '/', '+', '=', '*']
total = 0
grid = [[char for char in line] for line in data]
row, col = len(grid), len(grid[0])

nums = []
potential_gear = []
j, k = float('inf'), float('inf')

for r in range(row):
  for c in range(col):
    if grid[r][c] == '*':
      start, end = get_gear_neighbors(r, c)
      potential_gear.append({"start": start, "end": end, "pos": (r, c)})
    if j == float('inf') and grid[r][c].isnumeric():
      j = c
    if j != float('inf') and (grid[r][c] == '.' or c == col - 1 or grid[r][c] in special_char):
      k = c - 1 if grid[r][c] == '.' or grid[r][c] in special_char else c
      start, end = get_neighbors(r, j, k)
      nums.append({"start": start, "end": end, "row": r, "pos": (j, k)})
      j, k = float('inf'), float('inf')

for gear in potential_gear:
  potential_list = []
  for num in nums:
    potential = ranges_overlap(gear["start"], gear["end"], num)
    if potential:
      potential_list.append(potential)
  if len(potential_list) == 2:
    total += math.prod(potential_list)
  potential_list = []

print(total)