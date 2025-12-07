"""
Advent of Code 2025 - Day 4: Printing Department
Find accessible paper rolls based on neighbor count.
"""

def count_adjacent_rolls(grid, row, col):
    """
    Count how many adjacent positions contain paper rolls (@).
    
    Args:
        grid: 2D list representing the paper roll layout
        row: Row index of current position
        col: Column index of current position
    
    Returns:
        int: Number of adjacent positions with paper rolls
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # All 8 directions: N, NE, E, SE, S, SW, W, NW
    directions = [
        (-1, 0),   # N
        (-1, 1),   # NE
        (0, 1),    # E
        (1, 1),    # SE
        (1, 0),    # S
        (1, -1),   # SW
        (0, -1),   # W
        (-1, -1)   # NW
    ]
    
    count = 0
    
    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc
        
        # Check if position is within bounds
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if grid[new_row][new_col] == '@':
                count += 1
    
    return count


def solve_day4_part1(input_string):
    """
    Find how many paper rolls can be accessed by forklifts.
    
    Args:
        input_string: Grid layout as string
    
    Returns:
        int: Number of accessible paper rolls
    """
    # Parse the grid
    lines = input_string.strip().split('\n')
    grid = [list(line) for line in lines]
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    accessible_count = 0
    
    # Check each position in the grid
    for row in range(rows):
        for col in range(cols):
            # Only check positions with paper rolls
            if grid[row][col] == '@':
                adjacent_rolls = count_adjacent_rolls(grid, row, col)
                
                # Accessible if fewer than 4 adjacent rolls
                if adjacent_rolls < 4:
                    accessible_count += 1
    
    return accessible_count


def visualize_accessible(input_string):
    """
    Visualize which rolls are accessible (for debugging).
    
    Args:
        input_string: Grid layout as string
    
    Returns:
        str: Grid with accessible rolls marked as 'x'
    """
    lines = input_string.strip().split('\n')
    grid = [list(line) for line in lines]
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    result_grid = [row[:] for row in grid]  # Copy grid
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '@':
                adjacent_rolls = count_adjacent_rolls(grid, row, col)
                
                if adjacent_rolls < 4:
                    result_grid[row][col] = 'x'
    
    return '\n'.join([''.join(row) for row in result_grid])


def main():
    """Main function to solve Day 4."""
    
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
    
    print("Testing with example input:")
    example_result = solve_day4_part1(example_input)
    print(f"  Accessible rolls: {example_result} (expected: 13)")
    
    print("\nVisualization:")
    print(visualize_accessible(example_input))
    print()
    
    # Solve with actual input
    try:
        with open('input.txt', 'r') as f:
            puzzle_input = f.read()
        
        answer = solve_day4_part1(puzzle_input)
        print(f"Part 1 Answer: {answer}")
        
    except FileNotFoundError:
        print("Error: input.txt not found!")
        print("Please create input.txt with your puzzle input.")


if __name__ == "__main__":
    main()

