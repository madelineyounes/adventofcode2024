import re

def parse_corrupted_memory(memory):
   """
   Parse currupted memory to find valid mul(X,Y) instructions where X,Y are 1-3 digit integers.
   Returns the sum of all the valid multiplications.
   """

   pattern_mul = r'mul\((\d{1,3}),(\d{1,3})\)'
   pattern_do = r'do()'
   pattern_dont = r'don\'t()'
   
   mul_matches = [(m.span()[0], 'mul', m) for m in re.finditer(pattern_mul, memory)]
   do_matches = [(m.span()[0], 'do', m) for m in re.finditer(pattern_do, memory)]
   dont_matches = [(m.span()[0], 'dont', m) for m in re.finditer(pattern_dont, memory)]

   all_instructions = sorted(mul_matches + do_matches + dont_matches)

   total = 0
   mul_enabled = True
   mul = []

   for pos, inst_type, match in all_instructions:
      if inst_type == 'do':
         mul_enabled = True
      elif inst_type == 'dont':
         mul_enabled = False
      elif mul_enabled == True:
         x = int(match.group(1))
         y = int(match.group(2))
         result = x * y
         total += result
         mul.append((x, y, result))
    
   return total

# Test with the example from the problem
example = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)do()?mul(8,5))"
total = parse_corrupted_memory(example)
print(f"\nExample total: {total}")

# Process the actual input file
with open('day3_input.txt', 'r') as file:
    memory = file.read().strip()
    result = parse_corrupted_memory(memory)
    print(f"\nFinal result: {result}")