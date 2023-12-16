from collections import defaultdict


def get_nums(nums):
  return [int(num) for num in nums.replace(nums[:nums.index(':') + 1], '').split(' ') if num != '']


def get_possible_records(time, distance, i=0, ):
  if i == time:
    return 0
  count = 0
  if i * (time - i) > distance:
    count += 1
  return count + get_possible_records(time, distance, i + 1)


filename = "data.txt"

with open(filename, 'r') as file:
  _data = file.read().split('\n')

data = defaultdict(list)

data['time'] = get_nums(_data[0])
data['distance'] = get_nums(_data[1])

answer = 1

for i in range(len(data['time'])):
  answer *= get_possible_records(data['time'][i], data['distance'][i])

print(answer)
