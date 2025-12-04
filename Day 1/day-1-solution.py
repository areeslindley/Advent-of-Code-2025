# Day 1: Safe Dial Puzzle Solutions
def solve_part1(instructions):
    """Count times dial lands on 0 after completing rotations."""
    position = 50
    zero_count = 0
    
    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])
        
        if direction == 'L':
            position = (position - distance) % 100
        else:
            position = (position + distance) % 100
        
        if position == 0:
            zero_count += 1
    
    return zero_count


def solve_part2(instructions):
    """Count every time any click causes dial to point at 0."""
    position = 50
    total_zeros = 0
    
    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])
        
        # Simulate each click
        for _ in range(distance):
            if direction == 'R':
                position = (position + 1) % 100
            else:
                position = (position - 1) % 100
            
            if position == 0:
                total_zeros += 1
    
    return total_zeros


# Read and solve
def read_input(filename='input.txt'):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

instructions = read_input('input.txt')
print(f"Part 1: {solve_part1(instructions)}")
print(f"Part 2: {solve_part2(instructions)}")