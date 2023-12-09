filename = "data.txt"
data = open(filename,'r').read().split('\n')

total = 0

card_value = {
  "A": 13,
  "K": 12,
  "Q": 11,
  "J": 10,
  "T": 9,
  "9": 8,
  "8": 7,
  "7": 6,
  "6": 5,
  "5": 4,
  "4": 3,
  "3": 2,
  "2": 1,
}

hand_value = {
  "5": 7,
  "41": 6,
  "32": 5,
  "311": 4,
  "221": 3,
  "2111": 2,
  "11111": 1,
}

sorted_hands = []

def join_and_convert(hand):
  hand_map = {}
  for i in range(0, len(hand[0])):
    hand_map[hand[0][i]] = hand_map.get(hand[0][i], 0) + 1
  hand_map = {card_value[k]: v for k, v in hand_map.items()}
  converted_hand = [card_value[k] for k in hand[0]]
  sorted_hand_map = sorted(hand_map.items(), key=lambda item: (item[1], item[0]), reverse=True)
  joined_values = ''.join([str(v) for k, v in sorted_hand_map])
  return {
    "hand": converted_hand,
    "value": joined_values,
    "bid": int(hand[1])
  }

def compare_hands(hand1, hand2):
  hand1_value = hand_value[hand1['value']]
  hand2_value = hand_value[hand2['value']]
  if hand1_value > hand2_value:
    return 1
  if hand1_value == hand2_value:
    for i in range(len(hand1['hand'])):
      if hand1['hand'][i] > hand2['hand'][i]:
        return 1
      if hand1['hand'][i] < hand2['hand'][i]:
        return -1
  return -1


for index, hands in enumerate(data):
  hand = join_and_convert(hands.split(" "))
  sorted_hands.append(hand)

for hand in range(0, len(sorted_hands)):
  for compare in range(hand + 1, len(sorted_hands)):
    if compare_hands(sorted_hands[hand], sorted_hands[compare]) == 1:
      sorted_hands[hand], sorted_hands[compare] = sorted_hands[compare], sorted_hands[hand]

for index in range(0, len(sorted_hands)):
  total += ((index + 1) * sorted_hands[index]['bid'])
print(total)


