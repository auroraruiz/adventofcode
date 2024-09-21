"""
This module contains the solution to the Day 11 Advent of Code challenge.
"""
import os
import time

def galaxier(universe, rows, columns):
    """
    Identifies galaxies in the universe and removes rows and columns
    without them from the lists.

    Args:
    universe (list of list of str): A 2D list representing the universe,
    where each element is either '.' or '#'.
    rows (list of int): A list of row indices.
    columns (list of int): A list of column indices.

    Returns:
    list of tuple: A list of tuples, where each tuple represents the coordinates
    of a galaxy in the universe.
    """
    galaxies = []
    length =  len(universe)
    for i in range(length):
        for j in range(len(universe[0])):
            if universe[i][j] == "#":
                galaxies.append((i, j))
                if i in rows:
                    rows.remove(i)
                if j in columns:
                    columns.remove(j)
    return galaxies

def distancer(galaxies, rows, cols, expansion):
    """
    Calculates the total distance between galaxies,
    including expansions due to specified rows and columns.

    Args:
    galaxies (list of tuple): A list of tuples representing the coordinates of galaxies.
    rows (list of int): A list of row indices that add to the expansion distance.
    cols (list of int): A list of column indices that add to the expansion distance.
    expansion (int): The expansion distance to be added for each row and column
    in the specified ranges.

    Returns:
    int: The total calculated distance between galaxies with added expansion distances.
    """
    distances = []
    while galaxies:
        galaxy = galaxies.pop()
        for gal in galaxies:
            a = min(galaxy[0], gal[0])
            b = max(galaxy[0], gal[0])
            c = min(galaxy[1], gal[1])
            d = max(galaxy[1], gal[1])
            dist = b - a + d - c
            for row in rows:
                if row in range(a + 1, b):
                    dist += expansion
            for col in cols:
                if col in range(c + 1, d):
                    dist += expansion
            distances.append(dist)
    return sum(distances)

#Solution
if __name__ == "__main__":

    #Code to open the input file
    path = os.getcwd()
    FILE = "day11.txt"

    with open(path + '/' + FILE, encoding = 'utf-8') as f:
        lines = f.read().strip()
        lines = lines.split('\n')

    universe_input = [list(line) for line in lines]

    rows_input = set(range(0, len(universe_input)))
    cols_input = set(range(0, len(universe_input[0])))

    galaxy_output = galaxier(universe_input, rows_input, cols_input)

    start_time = time.time()
    # Part 1
    EXPANSION_INPUT_1 = 1
    print("Solution part 1: ", distancer(galaxy_output,
                                         rows_input,
                                         cols_input,
                                         EXPANSION_INPUT_1))
    # Part 2
    galaxy_output = galaxier(universe_input, rows_input, cols_input)
    EXPANSION_INPUT_2 = 999999
    print("Solution part 2: ", distancer(galaxy_output,
                                         rows_input,
                                         cols_input,
                                         EXPANSION_INPUT_2))
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
