# Day 1: Historian Hysteria
from collections import Counter

left = []
right = []
right_counter = Counter()

with open('day1_input.txt', 'r') as file:
    # Read each line in the file
    for line in file:
      distances = line.strip().split('   ')
      left.append(int(distances[0]))
      right.append(int(distances[1]))
      right_counter[int(distances[1])] += 1

sorted_left = sorted(left)
sorted_right = sorted(right)

freq_dict1 =  {}
freq_dict2 = {}

total = 0
similarity = 0

for i in range (0, len(sorted_left)):
   l = sorted_left[i]
   r = sorted_right[i]

   diff = l - r
   total += abs(diff)
   similarity += l * right_counter.get(l,0)

print (f"total: {total}")
print (f"similarity: {similarity}")