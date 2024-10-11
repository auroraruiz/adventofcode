import os
import time

def frontier(dirs, start, directions):
    """
    Calculates the number of frontier points and the vertices of a polygon based on given directions.

    Args:
    dirs (list): A list of tuples containing direction identifiers and step counts.
    start (tuple): The starting coordinates (x, y).
    directions (dict): A dictionary mapping direction identifiers to coordinate changes.

    Returns:
    tuple: A tuple containing:
        - dug_list (list): A list of tuples representing the vertices of the polygon formed by the dug points.
        - frontier_points_count (int): The total count of frontier points dug, including the starting point.
    """
    dug_list = []
    frontier_points_count = 1
    dug_list.append(start)
    next = start
    for dir in dirs:
        direction = directions[dir[0]]
        steps = dir[1]
        nx = direction[0]
        ny = direction[1]
        x = next[0]
        y = next[1]
        next = (x + nx * int(steps), y + ny * int(steps))
        frontier_points_count += int(steps)
        dug_list.append(next)
    return dug_list, frontier_points_count

def shoelace(vertices):
    """
    Calculates the area of a polygon using the shoelace formula.

    Args:
    vertices (list): A list of tuples representing the vertices of the polygon.

    Returns:
    float: The area of the polygon.
    """
    area_pol = 0
    i = 0
    while i < len(vertices):
        x_i = vertices[i][0]
        y_i1 = vertices[(i + 1) % len(vertices)][1]
        y_1i = vertices[(i - 1) % len(vertices)][1]
        area_pol += x_i * (y_i1 - y_1i)
        i += 1
    return 0.5 * abs(area_pol)

def pick_theorem(area_pol, boundary_points):
    """
    Calculates the number of interior points of a polygon using Pick's theorem.

    Args:
    area_pol (float): The area of the polygon.
    boundary_points (int): The number of boundary points on the polygon.

    Returns:
    int: The number of interior points of the polygon.
    """
    interior_points = area_pol - (boundary_points / 2) + 1
    return int(interior_points)

if __name__ == "__main__":
    # Code to open the input file
    path = os.getcwd()
    FILE = "day18.txt"
    
    with open(os.path.join(path, FILE), encoding='utf-8') as f:
        lines = f.read().strip()
        dirs = [tuple(line.split(" ")[:2]) for line in lines.split('\n')]
        dirs2 = [(line.split(" ")[-1:][0][7:8], int(line.split(" ")[-1:][0][2:7], 16)) for line in lines.split('\n')]

    start_time = time.time()

    # Define direction mappings for both sets of directions
    directions = {'D': (1, 0), 'U': (-1, 0), 'L': (0, -1), 'R': (0, 1)}
    directions2 = {'1': (1, 0), '3': (-1, 0), '2': (0, -1), '0': (0, 1)}
    start = (0, 0)

    # Calculate frontier points and counts for both sets of directions
    dug_frontier, frontier_points_count = frontier(dirs, start, directions)
    dug_frontier2, frontier_points_count2 = frontier(dirs2, start, directions2)
    
    # Calculate areas and interior points for both sets of dug points
    area = shoelace(dug_frontier)
    inside_points = pick_theorem(area, frontier_points_count)
    area2 = shoelace(dug_frontier2)
    inside_points2 = pick_theorem(area2, frontier_points_count2)

    # Part 1 solution
    print("Solution part 1: ", frontier_points_count + inside_points)
    # Part 2 solution
    print("Solution part 2: ", frontier_points_count2 + inside_points2)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
