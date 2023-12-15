from collections import defaultdict

filename = "data.txt"

with open(filename, "r") as file:
  data = file.read().split("\n")

answer = float("inf")
count = 0
almanac_data = defaultdict(list)
almanac_map = defaultdict(list)
categories = defaultdict(list)
seeds = []

for index, line in enumerate(data):
  if index == 0:
    _seeds = line[line.index(":") + 2:].split(" ")
    for j in range(len(_seeds)):
      if j % 2 == 1:
        seeds.append(
            (int(_seeds[j - 1]),
             int(_seeds[j - 1]) + int(_seeds[j]), 1)
        )
  else:
    if line:
      if not line[0].isnumeric():
        category1, category2 = line[: line.index(" ")].split("-to-")
        almanac_data[category1] = {category2: []}
      else:
        to_num, from_num, range_num = line.split(" ")
        almanac_data[category1][category2].append(
            (int(from_num), int(from_num) + int(range_num), int(to_num))
        )

category1 = list(almanac_data.keys())
category2 = [key for subdict in almanac_data.values() for key in subdict]

while seeds:
  start, end, count = seeds.pop()
  if count == len(category1) + 1:
    answer = min(start, answer)
    continue
  for conversion in almanac_data[category1[count - 1]][category2[count - 1]]:
    conversion_start, conversion_end, conversion_target = conversion
    difference = conversion_target - conversion_start
    if end <= conversion_start or conversion_end <= start:
      continue
    if start < conversion_start:
      seeds.append((start, conversion_start, count))
      start = conversion_start
    if conversion_end < end:
      seeds.append((conversion_end, end, count))
      end = conversion_end
    seeds.append((start + difference, end + difference, count + 1))
    break
  else:
    seeds.append((start, end, count + 1))

print(answer)
