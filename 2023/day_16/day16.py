"""
This module contains the solution to the Day 16 Advent of Code challenge.
"""
import os
import time

def calculate_next(point_dir, grid):
    """
    Calculates the next position and direction based on the current position and direction.

    Args:
    point_dir (tuple): A tuple containing the current position (x, y) and direction (dir_x, dir_y).
    grid (list of list): The grid representing the contraption.

    Returns:
    tuple: The next position and direction as a tuple, along with any split option if applicable.
    """
    x, y = point_dir[0]
    dir_x, dir_y = point_dir[1]
    next_dir_x, next_dir_y = dir_x, dir_y
    next_x, next_y = x + dir_x, y + dir_y
    option = None

    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        if grid[x][y] == '\\':
            next_dir_x, next_dir_y = dir_y, dir_x
        elif grid[x][y] == '/':
            next_dir_x, next_dir_y = -dir_y, -dir_x
        elif grid[x][y] == '-':
            if dir_x != 0:
                next_dir_x, next_dir_y = dir_y, dir_x
                option = (x - dir_y, y - dir_x), (-dir_y, -dir_x)
        elif grid[x][y] == '|':
            if dir_y != 0:
                next_dir_x, next_dir_y = dir_y, dir_x
                option = (x - dir_y, y - dir_x), (-dir_y, -dir_x)

        next_x, next_y = x + next_dir_x, y + next_dir_y

    return ((next_x, next_y), (next_dir_x, next_dir_y)), option

def calculate_stream(start, grid, visited):
    """
    Calculates the path of the beam through the grid and keeps track of energized tiles.

    Args:
    start (tuple): The starting position and direction of the beam.
    grid (list of list): The grid representing the contraption.

    Returns:
    dict: A dictionary of visited tiles with their energized status.
    """
    queue = [start]
    while queue:
        current = queue.pop(0)
        while current not in visited:
            visited[current] = visited.get(current,0)+1
            next, option = calculate_next(current,grid)
            if option != None and option[0][0] in range(0, len(grid)) and option[0][1] in range(0,len(grid[0])):
                queue.append(option)
            if next[0][0]<0 or next[0][0]>=len(grid) or next[0][1]<0 or next[0][1]>= len(grid[0]):
                break
            current = next
    return visited

def energizer(start,grid):
    """
    Calculates the number of energized tiles starting from a specific position.

    Args:
    start (tuple): The starting position and direction of the beam.
    grid (list of list): The grid representing the contraption.

    Returns:
    int: The number of energized tiles.
    """
    visited = {}
    visited = calculate_stream(start,grid, visited)
    visited2 = set()
    for key,value in visited:
        visited2.add(key)
    return (len(visited2))

def max_energizer(starts, grid):
    """
    Finds the maximum number of energized tiles from all possible starting positions.

    Args:
    starts (list): A list of starting positions and directions.
    grid (list of list): The grid representing the contraption.

    Returns:
    int: The maximum number of energized tiles from any starting position.
    """
    return max(energizer(start, grid) for start in starts)

# Solution
if __name__ == "__main__":
    # Code to open the input file
    path = os.getcwd()
    FILE = "day16.txt"
    
    with open(os.path.join(path, FILE), encoding='utf-8') as f:
        lines = f.read().strip()
        grid = [list(x) for x in lines.split('\n')]

    start = ((0,0),(0,1))

    starts = ([((x,0),(0,1)) for x in range(0, len(grid))]+
              [((0,y),(1,0)) for y in range(0,len(grid[0]))]+
              [((x,len(grid[0])-1),(0,-1)) for x in range(0, len(grid))]+
              [((len(grid)-1,y),(-1,0)) for y in range(0,len(grid[0]))])

    start_time = time.time()    
    # Part 1 solution
    print("Solution part 1: ", energizer(start, grid))
    # Part 2 solution
    print("Solution part 2: ", max_energizer(starts,grid))
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
