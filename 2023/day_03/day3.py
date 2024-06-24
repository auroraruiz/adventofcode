"""
This module contains the solution to the Day 3 Advent of Code challenge.
"""
import os
import time

def check_valid(grid_lines, start_row, start_col, num_length):
    """    
    Check the region next to a number to see if it's a part number.
    If it is, check if there's a gear (*) next to the number,
    and if positive returns the gear's coordinates.

    Parameters:
        grid_lines (List[str]): List of strings representing the grid.
        start_row (int): Starting row index.
        start_col (int): Starting column index.
        num_length (int): Length of the number to check from the starting column index.

    Returns:
        Tuple[bool, bool, Tuple[int, int]]:
            - check (bool): True if a non-digit, non-dot character is found.
            - gear (bool): True if a gear ('*') is found.
            - gear_pos (Tuple[int, int]): Position of the gear, or (-1, -1) if no gear is found.
    """
    check = False
    gear = False
    gear_pos = (-1, -1)

    row_min = max(start_row, 1)
    row_max = min(start_row, len(grid_lines) - 2)

    col_min = max(start_col, 1)
    col_max = min(start_col + num_length, len(grid_lines[0]) - 1)

    for row in range(row_min - 1, row_max + 2):
        for col in range(col_min - 1, col_max + 1):
            char = grid_lines[row][col]
            if char != '.' and not char.isdigit():
                check = True
                if char == '*':
                    gear = True
                    gear_pos = (row, col)
                return check, gear, gear_pos

    return check, gear, gear_pos


def read_numbers(grid_lines):
    """
    Process the grid grid_lines to identify and sum up part numbers.
    Additionally, process the grid grid_lines to identify and sum up part gears ('*').

    Parameters:
        grid_grid_lines (List[str]): List of strings representing the grid.

    Returns:
        Tuple[int, int]:
            - total_sum (int): The total sum of all part numbers found in the grid.
            - gear_sum (int): The total product sum of gears ('*').
    """
    visited = set()
    gear_dict = {}
    total_sum = 0

    for i, line in enumerate(grid_lines):
        j = 0
        while j < len(line):
            if (i, j) in visited:
                j += 1
                continue

            if line[j].isdigit():
                number_str = line[j]
                start_col = j
                while (j + 1) < len(line) and line[j + 1].isdigit():
                    j += 1
                    visited.add((i, j))
                    number_str += line[j]

                check_number, gear, gear_pos = check_valid(grid_lines,
                                                           i, start_col,
                                                           len(number_str))
                if gear:
                    if gear_pos in gear_dict:
                        gear_dict[gear_pos][0] += 1
                        gear_dict[gear_pos][1] *= int(number_str)
                    else:
                        gear_dict[gear_pos] = [1, int(number_str)]

                if check_number:
                    total_sum += int(number_str)

            j += 1

    gear_sum = sum(value[1] for value in gear_dict.values() if value[0] >= 2)

    return total_sum, gear_sum

#Solution
if __name__ == "__main__":

    #Code to open the input file
    path = os.getcwd()
    FILE = "day3.txt"

    with open(os.path.join(path, FILE), encoding='utf-8') as f:
        lines = f.readlines()
        lines = [item.strip("\n") for item in lines]

    start_time = time.time()
    solution = read_numbers(lines)
    #Part 1
    print("Solution part 1: ", solution[0])
    #Part 2
    print("Solution part 2: ",solution[1])
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
