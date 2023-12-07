filename = "data.txt"
input = open(filename,'r').read().split('\n')

nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
total = 0

for line in input:
  digits = []
  n = 0
  for index, char in enumerate(line):
    if char in nums:
      if n == 0 or n == 1:
        digits.append(char)
        n += 1
      if n == 2:
        digits[-1] = char
    if index == len(line) - 1:
      if n == 1:
        digits.append(digits[0])
  total += int(digits[0] + digits[1])

print(total)