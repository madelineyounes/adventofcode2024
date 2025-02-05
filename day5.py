import re

def load_file():
   pair_char = re.compile('|')
   update_char = re.compile(',')
   page_pairs = []
   page_updates = []

   with open('day5_input.txt', 'r') as file:
      for line in file:
         if (re.search(r'\|',  line) != None):
            page_pairs.append(line.strip().split('|'))
         elif (re.search(r',', line) != None):
            page_updates.append(line.strip().split(','))
   return page_pairs, page_updates

def check_update_order(rules, update):
    # For each rule
    for x, y in rules:
        # If both pages are in this update
        if x in update and y in update:
            # Check if they're in correct order
            if update.index(x) > update.index(y):
                return False
    return True

def fix_update_order(page_pairs, update):
    # Keep swapping items until order is correct
    while not check_update_order(page_pairs, update):
        for x, y in page_pairs:
            if x in update and y in update:
                if update.index(x) > update.index(y):
                    # Swap to fix order
                    i = update.index(x)
                    j = update.index(y)
                    update[i], update[j] = update[j], update[i]
    return update

def swap_items(lst, pos1, diff):
   pos2 = pos1 - diff
   temp = lst[pos1]
   lst[pos1] = lst[pos2]
   lst[pos2] = temp
   return lst

def sort_update_order(page_pairs, update):
   for pair in page_pairs:
      X, Y = pair[0], pair[1]
      diff = 1
      try:
         while update.index(X) > update.index(Y):
            print(update.index(X), diff)
            print(X, Y, update)
            update = swap_items(update, update.index(X), diff)
            diff += 1
         #sort_update_order(page_pairs, update)
      except ValueError:
         pass
   print(update)

def check_update_lines(page_pairs, page_updates):
   total = 0
   part2_total = 0
   correct = False
   for update in page_updates:
      for pair in page_pairs:
         X, Y = pair[0], pair[1]
         try:
            if update.index(X) < update.index(Y):
               correct = True
            else:
               fix_update_order(page_pairs, update)
               correct = False
               break
         except ValueError:
            pass
      middle = int(len(update)/2)
      if correct:
         total += int(update[middle])
      else:
         part2_total += int(update[middle])
   return total, part2_total

print("Day 5")
page_pairs, page_updates = load_file()
#print(page_pairs)
total, part2_total = check_update_lines(page_pairs, page_updates)
print(f"Part 1 Total: {total} Part 2 Total: {part2_total}")
