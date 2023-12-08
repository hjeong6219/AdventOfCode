filename = "data.txt"
data = open(filename,'r').read().split('\n')

total = 0

for line in data:
  str = line.split(" ")
  game = int(str[1][:-1])
  sets = line[line.index(":")+2:].split("; ")
  cubes = {"red": 0, "green": 0, "blue": 0}
  for set in sets:
    possible = True
    round = set.split(" ")
    power = 0
    for i in range(0, len(round)):
      for cube in cubes:
        if round[i].startswith(cube):
          cubes[cube] = max(cubes[cube], int(round[i-1]))
  for cube in cubes:
    if power == 0:
      power = cubes[cube]
    else:
      power *= cubes[cube]
  total += power

print(total)