"""
This module contains the solution to the Day 4 Advent of Code challenge.
"""
import os
import time

def scratchcards(card_lines):
    """
    Process the cards to count the total number of points won.
    Process the cards to count the total number of scratchcards won.

    Parameters:
        card_lines (List[str]): List of strings representing each a scratchcard

    Returns:
        Tuple[int, int]:
            - total_wins (int): The total points provided by the cards.
            - total_cards (int): The total number of cards won.
    """
    total_wins = 0
    dict_wins = {}
    total_cards = 0

    for i, numbers in enumerate(card_lines):
        win_numbers = numbers[0].split(" ")
        have_numbers = numbers[1].split(" ")
        points_pow = -1
        check = False
        for num in have_numbers:
            if num.isalnum() and num in win_numbers:
                check = True
                points_pow += 1
        dict_wins[i] = [points_pow+1, 1]
        if check:
            total_wins += 2**points_pow

    for key, value in dict_wins.items():
        for key2 in range(key + 1, key + 1 + value[0]):
            if key2 in dict_wins:
                dict_wins[key2][1] += value[1]
        total_cards += value[1]

    return total_wins, total_cards

#Solution
if __name__ == "__main__":

    #Code to open the input file
    path = os.getcwd()
    FILE = "day4.txt"

    with open(path + '/' + FILE, encoding = 'utf-8') as f:
        lines = f.read().strip()
        lines = lines.split('\n')

    # Special split for Day4
    lines = [x.split(':')[1].split("|") for x in lines]

    start_time = time.time()
    solution = scratchcards(lines)
    #Part 1
    print("Solution part 1: ", solution[0])
    #Part 2
    print("Solution part 2: ",solution[1])
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
