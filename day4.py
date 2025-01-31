
def load_file():
   # Reads in input file converts into a grid
   grid = []
   with open('day4_input.txt', 'r') as file:
      for line in file:
         row = list(line.strip())
         grid.append(row)
   return grid

def find_word(grid, word):
   """
   Return a tuple for all possible directions of a word.
   """
   height = len(grid)
   width = len(grid[0])
   word_count = 0
   x_pattern_count = 0 
   word_step = len(word) - 1 
   
   # All possible directions: right, down-right, down, down-left, left, up-left, up, up-right
   directions = [
      (0, 1),   # right
      (1, 1),   # down-right
      (1, 0),   # down
      (1, -1),  # down-left
      (0, -1),  # left
      (-1, -1), # up-left
      (-1, 0),  # up
      (-1, 1)   # up-right
   ]

   def is_valid_position(row, col):
        return 0 <= row < height and 0 <= col < width

   def check_direction(start_row, start_col, direction):
      """Check if word exists starting from (start_row, start_col) going in direction"""
      row_delta, col_delta = direction
      current_row, current_col = start_row, start_col
      
      # Check each character of the word
      for char in word:
         if not is_valid_position(current_row, current_col):
               return False
         if grid[current_row][current_col] != char:
               return False
         current_row += row_delta
         current_col += col_delta
      return True
   
   def check_x_pattern(row, col):
      """Check if there's an X pattern of 'MAS' starting at this position"""
      # Check both diagonal directions for "MAS"
      dir1 = (1, 1)   # down-right
      dir2 = (1, -1)  # down-left
      dir3 = (-1, 1)   # up-right
      dir4 = (-1, -1)   # up-left
      forward_check = check_direction(row, col, dir1) and check_direction(row, col + 2, dir2)
      backward_check = check_direction(row, col, dir1) and check_direction(row + 2, col, dir3)
      double_back_check = check_direction(row+2, col+2, dir4) and check_direction(row + 2, col, dir3)
      backward_forward_check = check_direction(row+2, col+2, dir4) and check_direction(row, col + 2, dir2)
      return (forward_check or backward_check or double_back_check or backward_forward_check)


      
   # Try each starting position
   for row in range(height):
      for col in range(width):
         # Try each direction
         for direction in directions:
            if check_direction(row, col, direction):
               word_count += 1

         # For part 2, check X pattern if we're looking for "MAS"
         if word == "MAS" and is_valid_position(row, col + 2):
            if check_x_pattern(row, col):
               x_pattern_count += 1

   return word_count, x_pattern_count

word_count, _ = find_word(load_file(),"XMAS")
print(f"Part 1: Word Count for XMAS is {word_count}")

_, x_pattern_count  = find_word(load_file(),"MAS")
print(f"Part2: Word Count for an X of MAS is {x_pattern_count}")


