"""
This module contains the solution to the Day 7 Advent of Code challenge.
"""
import os
import time
from collections import Counter
import math

def classifier(hand):
    """
    Classifies a hand of cards into a rank based on the frequency of card values.

    Args:
    hand (tuple): A tuple containing the hand string and an associated value.

    Returns:
    tuple: A tuple containing the original hand string, its rank, and the associated value.
    """
    hand_split = list(hand[0])
    hand_dict = Counter(hand_split)
    num = math.prod(hand_dict.values())
    if num == 5:
        rank = 0
    elif num == 4:
        if len(hand_dict.values()) == 2:
            rank = 1
        else:
            rank = 4
    elif num == 6:
        rank = 2
    elif num == 3:
        rank = 3
    elif num == 2:
        rank = 5
    else:
        rank = 6
    return (hand[0], rank, hand[1])

def classifier2(hand):
    """#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 03:04:14 2024

@author: auro
"""

    Classifies a hand of cards into a rank based on the frequency of card values,
    accounting for 'J' as a wildcard.

    Args:
    hand (tuple): A tuple containing the hand string and an associated value.

    Returns:
    tuple: A tuple containing the original hand string, its rank, and the associated value.
    """
    hand_wo_j = hand[0].replace("J", "")
    num_j = 5 - len(hand_wo_j)
    if num_j == 5:
        hand_split = list(hand[0])
        hand_dict = Counter(hand_split)
        num = math.prod(hand_dict.values())
    else:
        hand_split = list(hand_wo_j)
        hand_dict = Counter(hand_split)
        max_key = max(hand_dict, key=hand_dict.get)
        hand_dict[max_key] += num_j
        num = math.prod(hand_dict.values())
    if num == 5:
        rank = 0
    elif num == 4:
        if len(hand_dict.values()) == 2:
            rank = 1
        else:
            rank = 4
    elif num == 6:
        rank = 2
    elif num == 3:
        rank = 3
    elif num == 2:
        rank = 5
    else:
        rank = 6
    return (hand[0], rank, hand[1])

def typer(hand1, hand2, order_dict):
    """
    Compares two hands based on their ranks and uses a secondary comparison if ranks are equal.

    Args:
    hand1 (tuple): A tuple containing a hand string, its rank, and an associated value.
    hand2 (tuple): A tuple containing a hand string, its rank, and an associated value.
    order_dict (dict): A dictionary defining the order of card values.

    Returns:
    bool: True if hand1 is ranked higher or equal to hand2, False otherwise.
    """
    if hand1[1] < hand2[1]:
        return True
    if hand1[1] > hand2[1]:
        return False
    return hander(hand1, hand2, order_dict)

def hander(hand1, hand2, order_dict):
    """
    Performs a secondary comparison between two hands based on card values.

    Args:
    hand1 (tuple): A tuple containing a hand string, its rank, and an associated value.
    hand2 (tuple): A tuple containing a hand string, its rank, and an associated value.
    order_dict (dict): A dictionary defining the order of card values.

    Returns:
    bool: True if hand1 is ranked higher or equal to hand2 based on card values, False otherwise.
    """
    hand1 = hand1[0]
    hand2 = hand2[0]
    length = len(hand1)
    for i in range(length):
        if order_dict[hand1[i]] == order_dict[hand2[i]]:
            continue
        if order_dict[hand1[i]] < order_dict[hand2[i]]:
            return True
        return False
    return False

def quicksort(lista, order_dict):
    """
    Sorts a list of hands using the quicksort algorithm based on their ranks and card values.

    Args:
    lista (list): A list of tuples, each containing a hand string, its rank,
    and an associated value.
    order_dict (dict): A dictionary defining the order of card values.

    Returns:
    list: A sorted list of hands.
    """
    if len(lista) < 2:
        return lista
    pivot = lista[0]
    left = [x for x in lista if typer(pivot, x, order_dict)]
    right = [x for x in lista if typer(x, pivot, order_dict)]
    return quicksort(left, order_dict) + [pivot] + quicksort(right, order_dict)

def solution(card_bids, order_dict, classifier_func):
    """
    Classifies and sorts a list of card bids, then calculates the total score
    based on their positions.

    Args:
    card_bids (list): A list of tuples, each containing a hand string and an associated value.
    order_dict (dict): A dictionary defining the order of card values.
    classifier_func (function): A function to classify each hand.

    Returns:
    int: The total score calculated based on the sorted positions of the card bids.
    """
    tuples = []
    for hand in card_bids:
        tuples.append(classifier_func(hand))
    sorted_tuples = quicksort(tuples, order_dict)
    ans = 0
    for i, hand in enumerate(sorted_tuples):
        ans += (i + 1) * hand[2]
    return ans

#Solution
if __name__ == "__main__":

    #Code to open the input file
    path = os.getcwd()
    FILE = "day7.txt"

    with open(path + '/' + FILE, encoding = 'utf-8') as f:
        lines = f.read().strip()
        lines = lines.split('\n')

    card_bids_input = [(x.split(' ')[0], int(x.split(' ')[1])) for x in lines]

    order_dict_input = {'A': 0,
             'K': 1,
             'Q': 2,
             'J': 3,
             'T': 4,
             '9': 5,
             '8': 6,
             '7': 7,
             '6': 8,
             '5': 9,
             '4': 10,
             '3': 11,
             '2': 12}

    order_dict_2_input ={'A': 0,
             'K': 1,
             'Q': 2,
             'T': 4,
             '9': 5,
             '8': 6,
             '7': 7,
             '6': 8,
             '5': 9,
             '4': 10,
             '3': 11,
             '2': 12,
             'J': 13}

    start_time = time.time()
    #Part 1
    print("Solution part 1: ", solution(card_bids_input, order_dict_input, classifier))
    #Part 2
    print("Solution part 2: ", solution(card_bids_input, order_dict_2_input, classifier2))
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
