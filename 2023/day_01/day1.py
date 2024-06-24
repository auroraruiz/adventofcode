"""
This module contains the solution to the Day 1 Advent of Code challenge.
"""

# importing functools for reduce()
from functools import reduce as red
import re
import time
import os
import operator

path =  os.getcwd()
FILE = "day1.txt"

with open(path + "/" + FILE, encoding="utf-8") as f:
    lines = f.readlines()
    lines = [item.strip("\n") for item in lines]

#Part 1

def numbers_in_word(word):
    """
    Parameters
    ----------
    word : string
        String that contains at least one integer.

    Returns
    -------
    output : int
    
        Combines the first digit and the last digit contained in the word 
    (in that order) to form a single two-digit number.
    """
    word_len = len(word)
    i = word_len - 1
    #print(word)
    while i > -1:
        try:
            digit2 = int(word[i])
            break
        except ValueError:
            i -= 1

    i = 0
    while i < word_len:
        try:
            digit1 = int(word[i])
            break
        except ValueError:
            i += 1

    return digit1*10+digit2

def map_red_lines(list_, map_function, red_function):
    """
    Applies a map function to each element in a list and then reduces the result
    using a reduce function.
    
    Args:
        list_ (list): The input list to be processed.
        map_function (function): A function to be applied to each element in the list.
        red_function (function): A function to be used to reduce the mapped results.
    
    Returns:
        The result of applying the reduce function to the mapped elements of the list.
    """
    return red(red_function,(map(map_function,list_)))

#Part 2

digits = [4,5,6,7,9,2,1,3,8]
digits_str =  ["four", "five", "six", "seven", "nine", "two", "one", "three", "eight"]
digits_dict = dict(zip(digits, digits_str))

digits_back = [4,6,8, 1, 2, 3, 9, 7,5]
digits_str_back =  ["four", "six", "eight", "one", "two", "three", "nine", "seven", "five"]
digits_dict_back = dict(zip(digits_back, digits_str_back))


def translator(word, dictionary1=None, dictionary2=None):
    """
    Translate a word containing numeric representations of digits into their 
    numeric form.
    
    This function takes a string `word` as input, where numeric digits are 
    represented by English words, and translates them into their corresponding
    numeric form. It utilizes two dictionaries, `dictionary1` and `dictionary2`,
    for mapping word representations of digits to their numeric equivalents.
    
    Args:
        word (str): The input word to be translated.
        dictionary1 (dict): A dictionary containing mappings for the first 
        part of the word. The keys are integers representing digits,
        and the values are their corresponding English word representations.
        Defaults to `digits_dict`.
        
        dictionary2 (dict): A dictionary containing mappings for the last part
        of the word. The keys are integers representing digits, and the values
        are their corresponding English word representations.
        Defaults to `digits_dict_back`.
    
    Returns:
        str: The translated word with numeric digits.
    
    Special Cases:
        The function handles special cases where "eightwo" is translated to 
        "8wo" and "eighthree" is translated to "8hree" in the first part of 
        the word, and "eightwo" is translated to "eigh2" and "eighthree" is
        translated to "eigh3" in the last part of the word.
    """
    if dictionary1 is None:
        dictionary1 = digits_dict
    if dictionary2 is None:
        dictionary2 = digits_dict_back

    #Preprocess word
    pattern = re.compile(r'([1-9])')
    word_list = re.split(pattern, word)

    word_i = word_list[0]
    word_f = word_list[-1]

    #Special case: threeight, eighthree
    word_i = re.sub("eightwo", "8wo", word_i)
    word_i = re.sub("eighthree", "8hree", word_i)

    for i in dictionary1:
        word_i = re.sub(dictionary1[i], str(i), word_i)

    word_list[0] = word_i

    if len(word_list)>1:
        word_f = re.sub("eightwo", "eigh2", word_f)
        word_f = re.sub("eighthree", "eigh3", word_f)

        for i in dictionary2:
            word_f = re.sub(dictionary2[i], str(i), word_f)
        word_list[-1] = word_f

    word = "".join(word_list)

    return word


def numbers_in_word_2(word, func_trans = translator):
    """
    Parameters
    ----------
    word : string
        String that contains at least one integer.
    dictionary: dict
        Dictionary. Its keys must be integers.

    Returns
    -------
    output : int
    
        Combines the first digit and the last digit contained in the word (
        either as an integer or as a string) in that order to form a single
        two-digit number.
    """
    word = func_trans(word)

    word_len = len(word)
    i = word_len-1

    while i > -1:
        try:
            digit2 = int(word[i])
            break
        except ValueError:
            i -= 1

    i = 0
    while i < word_len:
        try:
            digit1 = int(word[i])
            break
        except ValueError:
            i += 1

    #print(digit1*10+digit2,"\n")
    return digit1*10+digit2

#Solution
if __name__ == "__main__":

    #Part 1
    time_0 = time.time()
    print("Solution part 1: ", map_red_lines(lines, numbers_in_word, lambda a,b: a+b))
    time_1 = time.time()
    print("Time ex. of part 1: ", time_1-time_0)

    #Part 2
    time_0 = time.time()
    print("Solution part 2: ", map_red_lines(lines, numbers_in_word_2, operator.add))
    time_2 = time.time()
    print("Time ex. of part 2: ", time_2-time_0)
