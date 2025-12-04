# Day 2: Part 1 Solution - Sum of Invalid IDs
def is_invalid_id(num):
    """Check if a number is made of a pattern repeated twice."""
    s = str(num)
    length = len(s)
    
    if length % 2 != 0:
        return False
    
    mid = length // 2
    return s[:mid] == s[mid:]


def solve_day2(input_string):
    """
    Find sum of all invalid IDs in the given ranges.
    
    Args:
        input_string: Comma-separated ranges like "11-22,95-115,..."
    
    Returns:
        int: Sum of all invalid IDs
    """
    # Parse the input - remove whitespace and split by comma
    ranges_str = input_string.replace('\n', '').replace(' ', '')
    ranges = ranges_str.split(',')
    
    total_sum = 0
    
    for range_str in ranges:
        # Parse start and end of range
        start, end = map(int, range_str.split('-'))
        
        # Check each ID in the range
        for id_num in range(start, end + 1):
            if is_invalid_id(id_num):
                total_sum += id_num
    
    return total_sum


# Test with the example
example_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""

result = solve_day2(example_input)
print(f"Example result: {result}")  # Should be 1227775554

# Solve with your actual input
with open('input.txt', 'r') as f:
    puzzle_input = f.read()

answer = solve_day2(puzzle_input)
print(f"Part 1 answer: {answer}")