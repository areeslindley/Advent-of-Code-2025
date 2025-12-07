"""
Advent of Code 2025 - Day 4 Part 2: Printing Department
Iteratively remove accessible paper rolls.
"""

def count_adjacent_rolls(grid, row, col):
    """
    Count how many adjacent positions contain paper rolls (@).
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # All 8 directions
    directions = [
        (-1, 0), (-1, 1), (0, 1), (1, 1),
        (1, 0), (1, -1), (0, -1), (-1, -1)
    ]
    
    count = 0
    
    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc
        
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if grid[new_row][new_col] == '@':
                count += 1
    
    return count


def find_accessible_rolls(grid):
    """
    Find all positions of accessible rolls in the current grid state.
    
    Args:
        grid: 2D list representing current paper roll layout
    
    Returns:
        list: List of (row, col) tuples of accessible positions
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    accessible = []
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '@':
                adjacent_rolls = count_adjacent_rolls(grid, row, col)
                if adjacent_rolls < 4:
                    accessible.append((row, col))
    
    return accessible


def remove_rolls(grid, positions):
    """
    Remove rolls at the given positions by replacing with '.'.
    
    Args:
        grid: 2D list representing the paper roll layout
        positions: List of (row, col) tuples to remove
    
    Returns:
        2D list: Updated grid with rolls removed
    """
    # Create a copy to avoid modifying original
    new_grid = [row[:] for row in grid]
    
    for row, col in positions:
        new_grid[row][col] = '.'
    
    return new_grid


def solve_day4_part2(input_string, verbose=False):
    """
    Find total number of rolls that can be removed iteratively.
    
    Args:
        input_string: Grid layout as string
        verbose: If True, print state after each removal round
    
    Returns:
        int: Total number of rolls removed
    """
    # Parse the grid
    lines = input_string.strip().split('\n')
    grid = [list(line) for line in lines]
    
    total_removed = 0
    round_num = 0
    
    if verbose:
        print("Initial state:")
        print('\n'.join([''.join(row) for row in grid]))
        print()
    
    while True:
        # Find all accessible rolls in current state
        accessible = find_accessible_rolls(grid)
        
        # If no accessible rolls, we're done
        if not accessible:
            break
        
        # Remove the accessible rolls
        grid = remove_rolls(grid, accessible)
        
        num_removed = len(accessible)
        total_removed += num_removed
        round_num += 1
        
        if verbose:
            print(f"Round {round_num}: Removed {num_removed} rolls")
            print('\n'.join([''.join(row) for row in grid]))
            print()
    
    return total_removed


def solve_day4_part1(input_string):
    """
    Part 1: Find how many paper rolls can be accessed initially.
    """
    lines = input_string.strip().split('\n')
    grid = [list(line) for line in lines]
    
    accessible = find_accessible_rolls(grid)
    return len(accessible)


def main():
    """Main function to solve both parts of Day 4."""
    
    # Example test
    example_input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
    
    print("=" * 50)
    print("Testing with example input:")
    print("=" * 50)
    
    # Part 1
    part1_result = solve_day4_part1(example_input)
    print(f"Part 1: {part1_result} accessible rolls (expected: 13)")
    print()
    
    # Part 2
    print("Part 2 - Iterative removal:")
    part2_result = solve_day4_part2(example_input, verbose=True)
    print(f"Part 2: {part2_result} total rolls removed (expected: 43)")
    print()
    
    # Solve with actual input
    print("=" * 50)
    print("Solving with actual input:")
    print("=" * 50)
    
    try:
        with open('input.txt', 'r') as f:
            puzzle_input = f.read()
        
        part1_answer = solve_day4_part1(puzzle_input)
        part2_answer = solve_day4_part2(puzzle_input)
        
        print(f"Part 1 Answer: {part1_answer}")
        print(f"Part 2 Answer: {part2_answer}")
        
    except FileNotFoundError:
        print("Error: input.txt not found!")
        print("Please create input.txt with your puzzle input.")


if __name__ == "__main__":
    main()