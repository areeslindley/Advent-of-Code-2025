# Day 1: Part 2 Solution - Simulation Approach
def solve_with_simulation(instructions):
    """Solve by actually simulating every click."""
    position = 50
    total_zeros = 0
    
    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])
        
        for _ in range(distance):
            if direction == 'R':
                position = (position + 1) % 100
            else:
                position = (position - 1) % 100
            
            if position == 0:
                total_zeros += 1
    
    return total_zeros

# Test with example
example_instructions = [
    'L68', 'L30', 'R48', 'L5', 'R60',
    'L55', 'L1', 'L99', 'R14', 'L82'
]

print("Simulation result:", solve_with_simulation(example_instructions))


def read_input(filename='input.txt'):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

# Solve Part 2 with your actual input
instructions = read_input('input.txt')
password = solve_with_simulation(instructions)
print(f"The password (Part 2) is: {password}")
