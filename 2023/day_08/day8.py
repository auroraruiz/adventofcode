"""
This module contains the solution to the Day 8 Advent of Code challenge.
"""
import os
import time
from functools import reduce
import math

def dict_constructor(nodes):
    """
    Constructs a dictionary from a list of nodes where each node is a string
    in the format 'key = value1, value2'.

    Args:
    nodes (list): A list of strings where each string represents a node
    in the format 'key = value1, value2'.

    Returns:
    dict: A dictionary where keys are node identifiers and values
    are tuples of the form (value1, value2).
    """
    result = {}
    for node in nodes:
        node_pos = node.split(" = ")
        left = node_pos[1].split(', ')[0][-3:]
        right = node_pos[1].split(', ')[1][:-1]
        result[node_pos[0]] = (left, right)
    return result

def solution(dictionary, paths, start, end):
    """
    Finds the number of steps to reach the end node from the start node
    following a given path.

    Args:
    dictionary (dict): A dictionary where keys are node identifiers and values
    are tuples of the form (left, right).
    paths (list): A list of directions ('L' for left, 'R' for right)
    to traverse the nodes.
    start (str): The starting node identifier.
    end (str): The ending node identifier.

    Returns:
    int: The number of steps required to reach the end node from the start node.
    """
    found = False
    s = start
    e = end
    count = 0
    while not found:
        length = len(paths)
        for i in range(length):
            if paths[i] == 'L':
                if dictionary.get(s)[0].endswith(e):
                    found = True
                else:
                    s = dictionary.get(s)[0]
            else:
                if dictionary.get(s)[1].endswith(e):
                    found = True
                else:
                    s = dictionary.get(s)[1]
            count += 1
    return count

def starts(dictionary):
    """
    Extracts a list of node identifiers that end with 'A' from a given dictionary.

    Args:
    dictionary (dict): A dictionary where keys are node identifiers.

    Returns:
    list: A list of node identifiers that end with 'A'.
    """
    starts_list = []
    for key in dictionary.keys():
        if key.endswith('A'):
            starts_list.append(key)
    return starts_list

def lcm(a, b):
    """
    Calculates the Least Common Multiple (LCM) of two numbers a and b.

    Args:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The LCM of the two numbers.
    """
    return abs(a * b) // math.gcd(a, b)

def lcm_of_list(numbers):
    """
    Calculates the Least Common Multiple (LCM) of a list of numbers.

    Args:
    numbers (list): A list of integers.

    Returns:
    int: The LCM of the list of numbers.
    """
    return reduce(lcm, numbers)

def solution2(dictionary, paths, starts_list):
    """
    Calculates the LCM of the number of steps required to reach
    the end node 'Z' from each start node in starts_list.

    Args:
    dictionary (dict): A dictionary where keys are node identifiers
    and values are tuples of the form (left, right).
    paths (list): A list of directions ('L' for left, 'R' for right)
    to traverse the nodes.
    starts_list (list): A list of starting node identifiers.

    Returns:
    int: The LCM of the number of steps required to reach
    the end node 'Z' from each start node.
    """
    start_count = []
    for start in starts_list:
        start_count.append(solution(dictionary, paths, start, 'Z'))
    return lcm_of_list(start_count)

#Solution
if __name__ == "__main__":

    #Code to open the input file
    path = os.getcwd()
    FILE = "day8.txt"

    with open(path + '/' + FILE, encoding = 'utf-8') as f:
        lines = f.read().strip()
        lines = lines.split('\n\n')

    instructions_input = lines[0]
    nodes_input = list(lines[1].split("\n"))

    maps_input = dict_constructor(nodes_input)

    starts_list_input = starts(maps_input)

    start_time = time.time()
    # Part 1
    print("Solution part 1: ", solution(maps_input,
                                        instructions_input,
                                        start='AAA',
                                        end='ZZZ'))
    # Part 2
    print("Solution part 2: ", solution2(maps_input,
                                         instructions_input,
                                         starts_list_input))
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
