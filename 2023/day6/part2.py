from collections import defaultdict
import re


def get_nums(nums):
  return int(''.join(re.findall('\d', nums)))


def get_possible_records(time, distance):
  possible_record = 0
  for i in range(time):
    attempt = i * (time - i)
    if attempt >= distance:
      possible_record += 1
  return possible_record


filename = "data.txt"

with open(filename, 'r') as file:
  _data = file.read().split('\n')

data = defaultdict(int)

data['time'] = get_nums(_data[0])
data['distance'] = get_nums(_data[1])

answer = get_possible_records(data['time'], data['distance'])

print(answer)
