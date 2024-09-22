"""
This module contains the solution to the Day 13 Advent of Code challenge.
"""
import os
import time

def transpose_strings(strings):
    """
    Transposes a list of strings, treating each string as a row of characters.

    Args:
    strings (list of str): A list of strings, where each string represents a row of characters.

    Returns:
    list of str: A list of strings where each string is a column from the input, effectively 
    transposing the original list of rows into columns.
    """
    return [''.join(row) for row in zip(*strings)]

def reflection(pattern):
    """
    Finds the largest reflection symmetry in a pattern (string).

    Args:
    pattern (str): A string representing the pattern in which to look for symmetrical reflection.

    Returns:
    int: The index of the largest reflection's center. Returns -1 if no reflection is found.
    """
    best_reflection_index = -1
    i = 0
    while i<len(pattern)-1:
        if pattern[i] == pattern[i+1] and reflection_check(pattern,i):
            best_reflection_index = i
        i+=1
    return best_reflection_index

def reflection_check(pattern,i):
    """
    Verifies if a reflection symmetry exists around the specified index.
    
    This function checks whether characters on either side of the center 
    (starting at index `i`) mirror each other. It checks for symmetry 
    by comparing characters moving outward from the center until the 
    edges of the pattern are reached.

    Args:
    pattern (str): A string representing the pattern to be checked.
    i (int): The index in the pattern where the reflection check should start.

    Returns:
    bool: True if a reflection exists, False otherwise.
    """
    offset  = 1
    while i>-1 and (i+offset)<len(pattern):
        if pattern[i] != pattern[i+offset]:
            return False
        i-=1
        offset += 2
    return True

def note_summary(patterns):
    """
    Summarizes the reflection properties of the patterns and calculates a score.

    This function calculates the total score for a list of patterns based on 
    vertical and horizontal reflection lines.

    Args:
    patterns (list of list of str): A list of patterns where each pattern is a list of strings representing 
    rows of characters (e.g., `"#.##..##."`).

    Returns:
    int: The total summary score, which includes the sum of the number of columns to the left of the 
    vertical reflection line and 100 multiplied by the number of rows above the horizontal reflection line.
    """
    total  = 0
    for pattern in patterns:
        candidate = reflection(pattern)
        total += 100*(candidate+1)

        if candidate == -1:
            trans_pattern = transpose_strings(pattern)
            candidate = reflection(trans_pattern)
            total += (candidate+1)

    return total


def smudge_reflection(pattern):
    """
    Finds the first reflection in the pattern that allows one smudge (minor difference).

    Args:
    pattern (list of str): The list of strings representing the pattern rows.

    Returns:
    int: The index of the reflection found or -1 if none is found.
    """
    for i in range(len(pattern) - 1):
        if smudge_check(pattern, i):
            return i
    return -1


def smudge_row(line1, line2):
    """
    Compares two rows and checks if they differ by exactly one character.

    Args:
    line1, line2 (str): Two strings representing rows to be compared.

    Returns:
    bool: True if the rows differ by exactly one character, False otherwise.
    """
    diffs = sum(1 for a, b in zip(line1, line2) if a != b)
    return diffs == 1

def smudge_check(pattern, i):
    """
    Checks for reflection symmetry at index `i` with at most one smudge.

    Args:
    pattern (list of str): The list of strings representing the pattern rows.
    i (int): The index at which to start checking for reflection.

    Returns:
    bool: True if a reflection with at most one smudge is found, False otherwise.
    """
    offset = 1
    smudge = 0
    
    while i >= 0 and (i + offset) < len(pattern):
        if pattern[i] != pattern[i + offset]:
            if smudge_row(pattern[i], pattern[i + offset]):
                smudge += 1
            else:
                return False
        if smudge > 1:
            return False
        i -= 1
        offset += 2
    
    return smudge == 1

def smudge_note_summary(patterns):
    """
    Calculates the summary score of patterns based on smudged reflections.

    Args:
    patterns (list of list of str): A list of patterns, each being a list of strings representing rows.

    Returns:
    int: The total score based on horizontal and vertical smudged reflections.
    """
    total = 0
    for pattern in patterns:
        # Check horizontal reflection
        candidate = smudge_reflection(pattern)
        total += 100 * (candidate + 1)

        # If no horizontal smudge reflection, check vertical smudge reflection 
        if candidate == -1:
            trans_pattern = transpose_strings(pattern)
            candidate = smudge_reflection(trans_pattern)
            total += (candidate + 1)
    
    return total

#Solution
if __name__ == "__main__":

    #Code to open the input file
    path = os.getcwd()
    FILE = "day13.txt"

    
    with open(path + '/' + FILE, encoding = 'utf-8') as f:
        lines = f.read().strip()
        lines = lines.split('\n\n')
    
    patterns = [pattern.split('\n') for pattern in lines]

    start_time = time.time()
    # Part 1
    print("Solution part 1: ", note_summary(patterns))
    # Part 2
    print("Solution part 2: ", smudge_note_summary(patterns))
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")

