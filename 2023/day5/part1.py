from collections import defaultdict

filename = "data.txt"

with open(filename, 'r') as file:
  data = file.read().split('\n')

answer = float('inf')
almanac_data = defaultdict(list)
almanac_map = defaultdict(list)
categories = defaultdict(list)

for index, line in enumerate(data):
  if index == 0:
    seeds = [int(seed) for seed in line[line.index(':') + 2:].split(' ')]
  else:
    if line:
      if not line[0].isnumeric():
        category1, category2 = line[:line.index(' ')].split('-to-')
        almanac_data[category1] = {category2: []}
      else:
        to_num, from_num, range_num = line.split(' ')
        almanac_data[category1][category2].append(
          {'to': int(to_num), 'from': int(from_num), 'range': int(range_num)})

category1 = list(almanac_data.keys())
category2 = [key for subdict in almanac_data.values() for key in subdict]

for seed in seeds:
  for index in range(len(category1)):
    if index == 0:
      key = seed
    almanac_entries = almanac_data[category1[index]][category2[index]]
    in_range = False
    for entry in almanac_entries:
      if in_range == False:
        from_num = entry['from']
        to_num = entry['to']
        range_num = entry['range']
        if key in range(from_num, from_num + range_num):
          key += (to_num - from_num)
          in_range = True
      else:
        continue
  answer = min(answer, key)

print(answer)
