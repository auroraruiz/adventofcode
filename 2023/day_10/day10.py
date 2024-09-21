"""
This module contains the solution to the Day 10 Advent of Code challenge.
"""
import os
import time
from collections import namedtuple

def find_start(pipes):
    """
    Finds the starting position 'S' in a grid of pipes.

    Args:
    pipes (list): A list of strings where each string represents a row of pipes in the grid.

    Returns:
    tuple: A tuple (i, j) representing the coordinates of the start position 'S'.
    None: If 'S' is not found in the grid.
    """
    for i, pipe in enumerate(pipes):
        for j, char in enumerate(pipe):
            if char == "S":
                return (i, j)
    return None

def determiner(pipes, position, directions, coords):
    """
    Determines the possible pipe connections from the current position.
    Function to determine the shape of the starting pipe 'S'.
    Updates the 'coords' dict with the found 'S' coordinates.

    Args:
    pipes (list): A list of strings where each string represents a row of pipes in the grid.
    position (tuple): A tuple (x, y) representing the current position in the grid.
    directions (list): A list of direction vectors.
    coords (dict): A dictionary mapping pipe symbols to their connection coordinates.

    Returns:
    list: A list of possible pipe connections from the current position.
    """
    x, y = position
    candidates = [[x+dx, y+dy] for [dx, dy] in directions]
    pipe_coords = []
    for i in range(4):
        symbol = pipes[candidates[i][0]][candidates[i][1]]
        pipe_coords.append(coords[symbol][(i+2)%4])
    coords['S'] = pipe_coords
    return pipe_coords

def solution(args):
    """
    Traverses the pipe grid starting from a given position and collects vertices of special pipes.
    Calculates the distance to the furthest pipe from the starting pipe 'S'.

    Args:
    args (Args): A namedtuple containing the following:
        pipes (list): A list of strings where each string represents a row of pipes in the grid.
        position (tuple): A tuple (x, y) representing the starting position in the grid.
        directions (list): A list of direction vectors.
        coords (dict): A dictionary mapping pipe symbols to their connection coordinates.
        visited (set): A set of visited positions.
        vertices (list): A list of vertices of special pipes.

    Returns:
    tuple: A tuple containing the updated set of visited positions, the list of vertices,
    and the distance to the furthest pipe from the starting pipe 'S'.
    """
    count = 0
    current_pipe = args.position
    while current_pipe not in args.visited:
        args.visited.add(current_pipe)
        candidates = [(current_pipe[0] + dx, current_pipe[1] + dy) for [dx, dy] in args.directions]
        symbol_current = args.pipes[current_pipe[0]][current_pipe[1]]
        if symbol_current in ['L', 'J', 'F', '7']:
            args.vertices.append(current_pipe)
        for i in range(4):
            symbol_cand = args.pipes[candidates[i][0]][candidates[i][1]]
            if (args.coords[symbol_cand][(i + 2) % 4] + args.coords[symbol_current][i] == 2 and
                candidates[i] not in args.visited):
                current_pipe = candidates[i]
                count += 1
                break
    return args.visited, args.vertices, count // 2 + 1

def create_file_with_loop_data(pipes, visited):
    """
    Creates a file with a visual representation of the visited nodes in the pipe grid.

    Args:
    pipes (list): A list of strings where each string represents a row of pipes in the grid.
    visited (set): A set of visited positions.

    Writes:
    A file 'out.txt' with 'x' marking visited nodes and ' ' marking unvisited nodes.
    """
    with open('out.txt', 'w', encoding='utf-8') as file:
        for i in range(len(pipes)):
            line = ""
            for j in range(len(pipes[0])):
                if (i, j) in visited:
                    line += "x"
                else:
                    line += ' '
            file.write(line + "\n")

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
        y_i1 = vertices[(i+1) % len(vertices)][1]
        y_1i = vertices[(i-1) % len(vertices)][1]
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


#Solution
if __name__ == "__main__":

    #Code to open the input file
    path = os.getcwd()
    FILE = "day10.txt"

    with open(path + '/' + FILE, encoding = 'utf-8') as f:
        lines = f.read().strip()
        lines = lines.split('\n')

    pipes_input = [list(line) for line in lines]

    # coordinates = [N,E,S,W]
    map_coords = {
        '|': [1,0,1,0],
        '-': [0,1,0,1],
        'L': [1,1,0,0],
        'J': [1,0,0,1],
        '7': [0,0,1,1],
        'F': [0,1,1,0],
        '.': [0,0,0,0]
        }

    directions_input  = [[-1,0],[0,1],[1,0],[0,-1]]

    s = find_start(pipes_input)

    coords_s = determiner(pipes = pipes_input,
                          position = s,
                          directions=directions_input,
                          coords = map_coords)

    visited_input = set()
    vertices_input = []

    start_time = time.time()

    Args = namedtuple('Args', ['pipes', 'position', 'directions', 'coords', 'visited', 'vertices'])

    args_input = Args(pipes=pipes_input,
                position=s,
                directions=directions_input,
                coords=map_coords,
                visited=visited_input,
                vertices=vertices_input)

    visited_output, vertices_output, furthest = solution(args_input)

    if coords_s in [[1,1,0,0],
                    [1,0,0,1],
                    [0,0,1,1],
                    [0,1,1,0]]:
        vertices_output.append(s)

    area = shoelace(vertices_output)

    #create_file_with_loop_data(pipes=pipes, visited=visited)

    # Part 1
    print("Solution part 1: ", furthest)
    # Part 2
    print("Solution part 2: ", pick_theorem(area,len(visited_output)))
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
