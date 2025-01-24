def is_safe_sequence(levels):
    """
    Check if a sequence of levels is safe according to the rules:
    1. Levels must be all increasing or all decreasing
    2. Adjacent differences must be between 1 and 3 inclusive
    """
    if len(levels) < 2:
        return True
    
    # Check first difference to determine if we should be increasing or decreasing
    is_increasing = levels[1] > levels[0]
    
    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]
        
        # Check if difference is between 1 and 3
        if abs(diff) < 1 or abs(diff) > 3:
            return False
            
        # Check if direction matches throughout
        if is_increasing and diff <= 0:
            return False
        if not is_increasing and diff >= 0:
            return False
    
    return True

def is_safe_report_with_dampener(levels):
    """
    Check if a report is safe, considering the Problem Dampener which can remove one level.
    Returns True if either:
    1. The original sequence is safe
    2. Removing any single level makes the sequence safe
    """
    # First check if it's safe without removing any level
    if is_safe_sequence(levels):
        return True
    
    # Try removing each level one at a time
    for i in range(len(levels)):
        # Create new sequence without the current level
        dampened_levels = levels[:i] + levels[i+1:]
        if is_safe_sequence(dampened_levels):
            return True
    
    return False

# Process the input file
safe_counter = 0
total_reports = 0

with open('day2_input.txt', 'r') as file:
    for line in file:
        levels = list(map(int, line.strip().split()))
        if is_safe_report_with_dampener(levels):
            safe_counter += 1
        total_reports += 1

print(f"Out of {total_reports} reports, {safe_counter} are safe with Problem Dampener.")

# Test cases from the problem statement
test_cases = [
    "7 6 4 2 1",    # Safe without removing any level
    "1 2 7 8 9",    # Unsafe regardless of which level is removed
    "9 7 6 2 1",    # Unsafe regardless of which level is removed
    "1 3 2 4 5",    # Safe by removing 3
    "8 6 4 4 1",    # Safe by removing one 4
    "1 3 6 7 9",    # Safe without removing any level
]

print("\nTesting example cases:")
for test in test_cases:
    levels = list(map(int, test.split()))
    result = "Safe" if is_safe_report_with_dampener(levels) else "Unsafe"
    print(f"{test}: {result}")