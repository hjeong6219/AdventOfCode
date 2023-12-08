filename = "data.txt"
data = open(filename,'r').read().split('\n')

total = 0

for line in data:
  str = line.split(" ")
  game = int(str[1][:-1])
  possible = True
  sets = line[line.index(":")+2:].split("; ")
  for set in sets:
    round = set.split(" ")
    for i in range(0, len(round)):
      cubes = {"red": 12, "green":13, "blue": 14}
      if not possible:
        continue
      for cube in cubes:
        if round[i].startswith(cube):
          cubes[cube] -= int(round[i-1])
          if cubes[cube] < 0:
            possible = False
            continue
  if possible:
    total += game

print(total)