"""
This module contains the solution to the Day 15 Advent of Code challenge.
"""
import os
import time

def trans(string):
    """
    Computes a HASH value for a given string based on the specified algorithm.

    The HASH algorithm transforms a string into a single number in the range 0 to 255. 
    It starts with a current value of 0 and processes each character by:
    1. Adding the ASCII code of the character to the current value.
    2. Multiplying the current value by 17.
    3. Taking the remainder when divided by 256.

    Args:
    string (str): The input string to be hashed.

    Returns:
    int: The computed HASH value for the input string, ranging from 0 to 255.
    """
    current_value = 0
    for item in string:
        current_value = (current_value + ord(item)) * 17 % 256
    return current_value

def initializator(lines):
    """
    Initializes the configuration of boxes from the initialization sequence.

    Each line specifies an operation for a box that modifies the lenses contained within.
    Operations include adding or removing lenses based on the parsed label and focal length.
    
    Args:
    lines (list of str): The initialization sequence, a list of strings representing steps.

    Returns:
    dict: A dictionary mapping box numbers (0-255) to lists of lens configurations 
          (each lens represented as [label, focal_length]).
    """
    boxes = {}
    for line in lines:
        if "=" in line:
            label, lens_length = line.split("=")
            box = trans(label)
            if box not in boxes:
                boxes[box] = []
            if label in boxes[box]:
                # Replace existing lens with the new one
                index = boxes[box].index(label)
                boxes[box][index + 1] = lens_length  # Update focal length
            else:
                # Add new lens
                boxes[box].extend([label, lens_length])
        elif "-" in line:
            label = line.split("-")[0]
            box = trans(label)
            if box in boxes and label in boxes[box]:
                index = boxes[box].index(label)
                del boxes[box][index:index + 2]  # Remove the lens and its focal length

    return boxes

def lens_power(boxes):
    """
    Calculates the total lens focusing power based on the current configuration of boxes.

    Each lens contributes to the total focusing power based on its position in the box and its focal length.
    The formula used is:
    (1 + box number) * (slot number) * (focal length)

    Args:
    boxes (dict): A dictionary of box configurations with lenses.

    Returns:
    int: The total focusing power of all lenses across all boxes.
    """
    total_power = 0
    for box_num, lenses in boxes.items():
        for slot_num in range(0, len(lenses), 2):
            label = lenses[slot_num]
            focal_length = int(lenses[slot_num + 1])
            slot_index = slot_num // 2 + 1  # 1-based slot index
            total_power += (1 + box_num) * slot_index * focal_length
    return total_power

# Solution
if __name__ == "__main__":
    # Code to open the input file
    path = os.getcwd()
    FILE = "day15.txt"
    
    with open(os.path.join(path, FILE), encoding='utf-8') as f:
        lines = f.read().strip().split(',')

    start_time = time.time()
    
    # Part 1 solution
    part1_solution = (sum(trans(line) for line in lines))
    print("Solution part 1: ", part1_solution)
    # Part 2 solution
    boxes = initializator(lines)
    part2_solution = lens_power(boxes)
    print("Solution part 2: ", part2_solution)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
