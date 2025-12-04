"""
Advent of Code 2025 - Day 2: Gift Shop
Find and sum invalid product IDs in given ranges.
"""

def is_invalid_id_part1(num):
    """
    Check if a number is made of a pattern repeated exactly twice.
    
    Args:
        num: The ID number to check
    
    Returns:
        bool: True if invalid (pattern repeated twice), False otherwise
    """
    s = str(num)
    length = len(s)
    
    # Must have even length to be split in half
    if length % 2 != 0:
        return False
    
    # Check if first half equals second half
    mid = length // 2
    return s[:mid] == s[mid:]


def is_invalid_id_part2(num):
    """
    Check if a number is made of a pattern repeated at least twice.
    
    Args:
        num: The ID number to check
    
    Returns:
        bool: True if invalid (repeating pattern), False otherwise
    """
    s = str(num)
    length = len(s)
    
    # Try each possible pattern length (must have at least 2 repetitions)
    for pattern_len in range(1, length // 2 + 1):
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            if s == pattern * (length // pattern_len):
                return True
    
    return False


def solve_day2(input_string, part=1):
    """
    Find sum of all invalid IDs in the given ranges.
    
    Args:
        input_string: Comma-separated ranges like "11-22,95-115,..."
        part: 1 for Part 1 rules, 2 for Part 2 rules
    
    Returns:
        int: Sum of all invalid IDs
    """
    # Choose the appropriate validation function
    is_invalid = is_invalid_id_part1 if part == 1 else is_invalid_id_part2
    
    # Parse the input - remove whitespace and split by comma
    ranges_str = input_string.replace('\n', '').replace(' ', '')
    ranges = ranges_str.split(',')
    
    total_sum = 0
    
    for range_str in ranges:
        # Parse start and end of range
        start, end = map(int, range_str.split('-'))
        
        # Check each ID in the range
        for id_num in range(start, end + 1):
            if is_invalid(id_num):
                total_sum += id_num
    
    return total_sum


def main():
    """Main function to solve both parts."""
    
    # Example test
    example_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
    1698522-1698528,446443-446449,38593856-38593862,565653-565659,
    824824821-824824827,2121212118-2121212124"""
    
    print("Testing with example input:")
    example_part1 = solve_day2(example_input, part=1)
    example_part2 = solve_day2(example_input, part=2)
    print(f"  Part 1: {example_part1} (expected: 1227775554)")
    print(f"  Part 2: {example_part2} (expected: 4174379265)")
    print()
    
    # Read actual input
    try:
        with open('input.txt', 'r') as f:
            puzzle_input = f.read()
        
        # Solve both parts
        print("Solving with actual input:")
        part1_answer = solve_day2(puzzle_input, part=1)
        part2_answer = solve_day2(puzzle_input, part=2)
        
        print(f"  Part 1: {part1_answer}")
        print(f"  Part 2: {part2_answer}")
        
    except FileNotFoundError:
        print("Error: input.txt not found!")
        print("Please create input.txt with your puzzle input.")


if __name__ == "__main__":
    main()