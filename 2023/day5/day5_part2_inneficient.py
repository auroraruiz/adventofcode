"""
This module contains the solution to the Day 5 Advent of Code challenge.
"""
import os
import time

def check_seed(candidate, seeds):
    """
    Checks if the candidate falls within any range defined by the seeds list.
    
    Args:
    candidate (int): The candidate value to be checked.
    seeds (list): A list where every other element is a start value and
    the following element is the range.

    Returns:
    int/bool: The candidate value if it falls within any of the ranges; 
    otherwise, False.
    """
    for k, seed in enumerate(seeds[::2]):
        seed_range = seeds[2*k + 1]
        if seed <= candidate < seed + seed_range:
            return candidate
    return False

def check_range(candidate, list_values):
    """
    Translates the candidate through a series of mappings defined in list_values.
    
    Args:
    candidate (int): The candidate value to be translated.
    list_values (list): A list of tuples/lists, where each sublist contains
    three integers (dest, start, range).

    Returns:
    int: The translated candidate value.
    """
    for value in list_values:
        dest = int(value[0])
        start = int(value[1])
        rang = int(value[2])
        if dest <= candidate < dest + rang:
            return start + (candidate - dest)
    return candidate

def reverse_finding(dictionary, seeds, key_names, start):
    """
    Finds a candidate value that, after a series of translations, falls within
    a range defined by the seeds list.
    
    Args:
    dictionary (dict): A dictionary containing the mappings for translations.
    seeds (list): A list where every other element is a start value and 
    the following element is the range.
    key_names (list): A list of keys to access specific mappings in 
    the dictionary.

    Returns:
    int: The found candidate value.
    """
    found =  False
    l = start
    while not found:
        candidate = l
        key_names_lenght = len(key_names)
        j = 0
        while j < key_names_lenght:
            candidate = check_range(candidate, dictionary[key_names[j]])
            j += 1
        if j == len(key_names):
            candidate = check_seed(candidate,seeds)
            if candidate:
                found = True
                return l
        l += 1
    return l

#Solution
if __name__ == "__main__":

    #Code to open the input file
    path = os.getcwd()
    FILE = "day5.txt"

    with open(path + '/' + FILE, encoding = 'utf-8') as f:
        lines = f.read().strip()
        lines = lines.split('\n\n')

    # Inefficient solution
    start_time = time.time()
    seeds_input = lines[0].split(": ")[1].split(" ")
    seeds_input = [int(x) for x in seeds_input]

    dict_maps_input = {}
    for i in range(len(lines)-1,0,-1):
        parts = lines[i].split(":\n")
        dict_maps_input[parts[0]] = [x.split(" ")
                                     for x in lines[i].split(":\n")[1].split("\n")]

    key_names_input = [str(key) for key in dict_maps_input]

    print("Inneficient solution to part 2: ",
          reverse_finding(dict_maps_input,
                          seeds_input,
                          key_names_input,
                          start = 0))
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
