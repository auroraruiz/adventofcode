import os
import time

def roll_all(grid, n, m, direction):
    """
    Rolls the objects ('O') in the grid in the specified direction, stopping at obstacles ('#').

    Args:
    grid (list of list of str): The grid where the objects and obstacles are placed.
    n (int): The number of rows in the grid.
    m (int): The number of columns in the grid.
    direction (str): The direction in which to roll the objects. Can be 'north', 'south', 'west', or 'east'.

    Returns:
    None: The grid is modified in place by moving the objects ('O') according to the rules.
    """
    if direction == 'north':
        for j in range(m):
            empty_x = 0
            for x in range(n):
                if grid[x][j] == "#":
                    empty_x = x + 1
                elif grid[x][j] == "O":
                    if empty_x != x:
                        grid[empty_x][j] = "O"
                        grid[x][j] = '.'
                    empty_x += 1

    elif direction == 'south':
        for j in range(m):
            empty_x = n - 1
            for x in range(n - 1, -1, -1):
                if grid[x][j] == "#":
                    empty_x = x - 1
                elif grid[x][j] == "O":
                    if empty_x != x:
                        grid[empty_x][j] = "O"
                        grid[x][j] = '.'
                    empty_x -= 1

    elif direction == 'west':
        for i in range(n):
            empty_y = 0
            for y in range(m):
                if grid[i][y] == "#":
                    empty_y = y + 1
                elif grid[i][y] == "O":
                    if empty_y != y:
                        grid[i][empty_y] = "O"
                        grid[i][y] = '.'
                    empty_y += 1

    elif direction == 'east':
        for i in range(n):
            empty_y = m - 1
            for y in range(m - 1, -1, -1):
                if grid[i][y] == "#":
                    empty_y = y - 1
                elif grid[i][y] == "O":
                    if empty_y != y:
                        grid[i][empty_y] = "O"
                        grid[i][y] = '.'
                    empty_y -= 1

def roll_all_directions(grid, n, m):
    """
    Performs one full cycle of rolling objects ('O') in all four directions: north, west, south, and east.

    Args:
    grid (list of list of str): The grid where the objects and obstacles are placed.
    n (int): The number of rows in the grid.
    m (int): The number of columns in the grid.

    Returns:
    None: The grid is modified in place by moving the objects ('O') according to the rules.
    """
    roll_all(grid, n, m, 'north')
    roll_all(grid, n, m, 'west')
    roll_all(grid, n, m, 'south')
    roll_all(grid, n, m, 'east')

def points(grid, n, m):
    """
    Calculates the total points in the grid based on the position of the objects ('O').

    Points are awarded based on how far up the column the 'O' is located, with higher positions earning more points.

    Args:
    grid (list of list of str): The grid where the objects and obstacles are placed.
    n (int): The number of rows in the grid.
    m (int): The number of columns in the grid.

    Returns:
    int: The total points based on the positions of the objects ('O').
    """
    return sum(n - x for y in range(m) for x in range(n) if grid[x][y] == "O")

def grid_to_tuple(grid):
    """
    Converts the grid to a tuple of tuples, making it hashable for storage in a set or dictionary.

    Args:
    grid (list of list of str): The grid where the objects and obstacles are placed.

    Returns:
    tuple of tuples: A hashable representation of the grid.
    """
    return tuple(map(tuple, grid))

def detect_cycle(grid, n, m, target_cycle=1_000_000_000):
    """
    Detects the cycle in the grid transformation and calculates the points after the target cycle.

    This function identifies repeating patterns in the grid transformation, finds the cycle length, and 
    computes the points after a large number of cycles efficiently using modulo arithmetic.

    Args:
    grid (list of list of str): The grid where the objects and obstacles are placed.
    n (int): The number of rows in the grid.
    m (int): The number of columns in the grid.
    target_cycle (int): The number of cycles after which to calculate the points. Defaults to 1,000,000,000.

    Returns:
    int: The points after the target cycle.
    """
    seen_grids = {}  # Stores grid states and their corresponding cycle number
    points_history = []  # Stores points for each cycle
    cycle_num = 0

    while True:
        current_grid_tuple = grid_to_tuple(grid)

        # If the grid state repeats, a cycle is detected
        if current_grid_tuple in seen_grids:
            cycle_start = seen_grids[current_grid_tuple]
            cycle_length = cycle_num - cycle_start
            target_cycle = (target_cycle - cycle_start) % cycle_length + cycle_start
            return points_history[target_cycle]

        # Store the current grid state and points for this cycle
        seen_grids[current_grid_tuple] = cycle_num
        points_history.append(points(grid, n, m))

        # Perform a full roll in all directions
        roll_all_directions(grid, n, m)
        cycle_num += 1

def points_part1(grid_str):
    """
    Calculates the total points for Part 1 by rolling all columns north and computing the points.

    Args:
    grid_str (str): The input grid in string format, where each row is separated by a newline.

    Returns:
    int: The total points based on the positions of the objects ('O') after rolling north.
    """
    grid = [list(line) for line in grid_str.split('\n')]
    n = len(grid)
    m = len(grid[0])
    roll_all(grid,n,m,'north')
    return points(grid, n, m)

def points_part2(grid_str):
    """
    Calculates the total points for Part 2.

    Args:
    grid_str (str): The input grid in string format, where each row is separated by a newline.

    Returns:
    int: The total points based on the positions of the objects ('O') after rolling 1_000_000_000 times.
    """
    grid = [list(line) for line in grid_str.split('\n')]
    n = len(grid)
    m = len(grid[0])
    return detect_cycle(grid, n, m)

# Solution
if __name__ == "__main__":

    # Code to pen the input file
    path = os.getcwd()
    FILE = "day14.txt"
    
    with open(path + '/' + FILE, encoding='utf-8') as f:
        lines = f.read().strip()
        grids = lines.split('\n\n')

    start_time = time.time()
    # Part 1 solution
    print("Solution part 1: ", points_part1(grids[0]))
    # Part 2 solution
    print("Solution part 2: ", points_part2(grids[0]))
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
