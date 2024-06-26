"""
This module contains the solution to the Day 6 Advent of Code challenge.
"""
import os
import time

def possibilities(time_p, distance):
    """
    Calculates the number of possible ways to cover a given distance
    within a specified time. Speed increases proportionately to time.

    Args:
    time_p (int): The total time available.
    distance (int): The distance to be covered.

    Returns:
    int: The number of possible ways to cover the distance.
    """
    pos = 0
    for ms in range(0, time_p + 1):
        speed = ms
        sail_time = time_p - ms
        distance_ps = sail_time * speed
        if distance_ps > distance:
            pos += 1
    return pos

def solution(list_times, list_distances):
    """
    Calculates the total number of possible ways to cover given distances
    within specified times.

    Args:
    list_times (list): A list of total times available for each distance.
    list_distances (list): A list of distances to be covered for each time.

    Returns:
    int: The total number of possible ways to cover all distances.
    """
    pos_total = 1
    length = len(list_times)
    for i in range(0, length):
        pos_total *= possibilities(list_times[i], list_distances[i])
    return pos_total

#Solution
if __name__ == "__main__":

    #Code to open the input file
    path = os.getcwd()
    FILE = "day6.txt"

    with open(path + '/' + FILE, encoding = 'utf-8') as f:
        lines = f.read().strip()
        lines = lines.split('\n')

    times = [int(x) for x in lines[0].split(' ')[1:] if x != '']
    distances =  [int(x) for x in lines[1].split(' ')[1:] if x != '']

    times2 = int(lines[0].split(':')[-1].replace(" ",""))
    distances2 =  int(lines[1].split(':')[-1].replace(" ",""))

    start_time = time.time()
    #Part 1
    print("Solution part 1: ", solution(times, distances))
    #Part 2
    print("Solution part 2: ", solution([times2],[distances2]))
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
