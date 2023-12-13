def get_position(r, j, k, row, col):
  start = (r - 1 if r != 0 else 0, j - 1 if j != 0 else 0)
  end = (r + 1 if r != row - 1 else r, k + 1 if k != col - 1 else k)
  return start, end

filename = "data.txt"

with open(filename, 'r') as file:
  data = file.read().split('\n')

special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '/', '+', '=']
total = 0

grid = [[char for char in line] for line in data]
row, col = len(grid), len(grid[0])

nums = []
j, k = float('inf'), float('inf')

for r in range(row):
  for c in range(col):
    if j == float('inf') and grid[r][c].isnumeric():
      j = c
    if j != float('inf') and (grid[r][c] == '.' or c == col - 1 or grid[r][c] in special_char):
      k = c - 1 if grid[r][c] == '.' or grid[r][c] in special_char else c
      start, end = get_position(r, j, k, row, col)
      nums.append({"start": start, "end": end, "row": r, "num": (j, k)})
      j, k = float('inf'), float('inf')

for num in nums:
  for r in range(num["start"][0], num["end"][0] + 1):
    for c in range(num["start"][1], num["end"][1] + 1):
      if grid[r][c] in special_char:
          total += int(''.join(grid[num["row"]][num["num"][0]: num["num"][1] + 1]))

print(total)