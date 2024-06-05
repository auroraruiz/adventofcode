"""
This module contains the solution to the Day 2 Advent of Code challenge.
"""

#Importing necessary modules
import re
from functools import reduce
import os
import time

def map_red_lines(list_, map_function, red_function):
    """
    This is a map-reduce function.
    To use it, you need to import reduce from functools.

    Parameters:
        list_ (Iterable): an iterable object
        map_function (function): map fuction
        red_function (function): reduce fuction

    Returns:
        The result of applying map-reduce to the interable.
    """
    return reduce(red_function,(map(map_function,list_)))

#Part 1

#Configuration
colors = ["red","green","blue"]
numbers = [12, 13, 14]
config = dict(zip(colors,numbers))

def str_process(game_str):
    """
    This function processes a game string input.

    Parameters:
        game_str (str): Game string input

    Returns:
        game_num, game_list (int, list)

    Example:
        In: 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
        Out: (1, ['3 blue', '4 red', '1 red', '2 green', '6 blue', '2 green'])

    """
    div = game_str.split(": ")
    game_num = div[0].strip("Game ")
    pattern = r', |; '
    game_list = re.split(pattern, div[1])
    return int(game_num), game_list

def base_case(subset_base, dictionary):
    """
    This function returns a True bool if the input subset's number of 
    cubes of a certain color is equal or less than the one present
    in the dictionary. Returns False otherwise.
    
    Parameters:
        subset_base (string): A simple subset
        dictionary (dict): The configuration of the maximun number of cubes per color.
    
    Returns:
        result (bool): True if the case is possible. False otherwise.
    
    Example:
        In: '8 blue', config
        Out: True
    
    """
    sub_num = subset_base.split()[0]
    sub_col = subset_base.split()[1]
    result = int(sub_num) <= dictionary[sub_col]
    return result

def checks(game_str, base_func=base_case, red_func = lambda a,b: a and b,
           proc_func = str_process, dictionary = None):
    """
    This function checks whether the whole game is possible or not. If possible,
    returns the id of the game. If not possible, returns 0.
    
    Parameters:
        game_str (string):  Game string input 
        base_func (function): Base case function to apply to game's subsets
        red_func(function): Reduce function
        proc_func(function): String processing function
        dictionary (dict): The configuration of the maximun number of cubes per color
        
    Returns:
        result (int): If the game is possible, returns the id of the game. 
        If not possible, returns 0.

    Example:
        In: 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
        Out: 1

    """
    if dictionary is None:
        dictionary = config

    game_num, game_list = proc_func(game_str)
    check = map(lambda x: base_func(x,dictionary), game_list)
    red_check = reduce(red_func, check)
    if red_check:
        result = game_num
    else:
        result = 0
    return result

#Part 2

def maxs(game_str):
    """
    This function finds the minimum set of cubes that must have been present for
    the game to be possible and returns the power of that set of cubes, which is equal 
    to the numbers of red, green, and blue cubes multiplied together.
    
    Parameters:
        game_str (string):  Game string input 

    Returns:
        result (int): Numbers of red, green, and blue cubes multiplied together.
        
    Example:
        In: 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
        Out: 48

    """
    game_list = str_process(game_str)[1]
    blue_max = 0
    green_max = 0
    red_max = 0
    for i in game_list:
        power =  int(i.split()[0])

        if "blue" in i:
            blue_max = max(blue_max,power)
        elif "green" in i:
            green_max = max(green_max,power)
        else:
            red_max = max(red_max,power)
    result = blue_max * green_max * red_max
    return result

#Solution
if __name__ == "__main__":

    #Code to open the input file
    path = os.getcwd()
    FILE = "day2.txt"

    with open(path + '/' + FILE, encoding = 'utf-8') as f:
        lines = f.readlines()
        lines = [item.strip("\n") for item in lines]

    #Part 1
    time_0 = time.time()
    print("Solution part 1: ", map_red_lines(lines, checks, lambda a,b: a+b))
    time_1 = time.time()
    print("Time ex. of part 1: ", time_1-time_0)

    #Part 2
    time_0 = time.time()
    print("Solution part 2: ", map_red_lines(lines, maxs, lambda a,b: a+b))
    time_2 = time.time()
    print("Time ex. of part 2: ", time_2-time_0)
