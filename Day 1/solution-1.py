
# Day 1: Part 1 Solution - Direct Calculation Approach 
def solve_safe_puzzle(instructions):
    """
    Solve the safe dial puzzle.
    
    Args:
        instructions: List of rotation strings like ['L68', 'R48', ...]
    
    Returns:
        int: Number of times the dial points at 0
    """
    position = 50  # Starting position
    zero_count = 0  # Count of times we land on 0
    
    for instruction in instructions:
        direction = instruction[0]  # 'L' or 'R'
        distance = int(instruction[1:])  # Extract the numeric distance
        
        # Update position based on direction
        if direction == 'L':
            position = (position - distance) % 100
        else:  # direction == 'R'
            position = (position + distance) % 100
        
        # Check if we landed on 0
        if position == 0:
            zero_count += 1
    
    return zero_count

# Example from the puzzle
example_instructions = [
    'L68', 'L30', 'R48', 'L5', 'R60',
    'L55', 'L1', 'L99', 'R14', 'L82'
]

password = solve_safe_puzzle(example_instructions)
print(f"Password: {password}")  # Should output 3

# Now try with actual input

def read_input(filename='input.txt'):
    """Read puzzle input from file."""
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

# Solve with your actual input
instructions = read_input('input.txt')
password = solve_safe_puzzle(instructions)
print(f"The actual password is: {password}")

