# Day 2: Part 2 Solution - Pattern Repetition Check
def is_invalid_id_part2(num):
    """Check if a number is made of a pattern repeated at least twice."""
    s = str(num)
    length = len(s)
    
    # Try each possible pattern length (must have at least 2 repetitions)
    for pattern_len in range(1, length // 2 + 1):
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            if s == pattern * (length // pattern_len):
                return True
    
    return False


def solve_day2_part2(input_string):
    """
    Find sum of all invalid IDs (repeated pattern at least twice).
    
    Args:
        input_string: Comma-separated ranges
    
    Returns:
        int: Sum of all invalid IDs
    """
    ranges_str = input_string.replace('\n', '').replace(' ', '')
    ranges = ranges_str.split(',')
    
    total_sum = 0
    
    for range_str in ranges:
        start, end = map(int, range_str.split('-'))
        
        for id_num in range(start, end + 1):
            if is_invalid_id_part2(id_num):
                total_sum += id_num
    
    return total_sum


# Test with the example
example_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""

result = solve_day2_part2(example_input)
print(f"Example result: {result}")  # Should be 4174379265

# Solve with your actual input
with open('input.txt', 'r') as f:
    puzzle_input = f.read()

answer = solve_day2_part2(puzzle_input)
print(f"Part 2 answer: {answer}")