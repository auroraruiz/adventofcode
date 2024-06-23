"""
This module contains the solution to the Day 5 Advent of Code challenge.
"""
import os
import time

def lowest_location(seeds,dict_maps):
    """
    Calculates the lowest location among the locations of all seeds.

    Parameters:
        seeds (List[int]): List of seed numbers.
        dict_maps (dict): Dictionary mapping categories to lists of lists. 
                          Each list contains (destination, start, range).

    Returns:
        int: The lowest location found.
    """
    min_dest = float('inf')
    for seed in seeds:
        seed_input = seed
        for _, list_value in dict_maps.items():
            for value in list_value:
                dest = int(value[0])
                start = int(value[1])
                rang = int(value[2])
                if start <= seed_input < start + rang:
                    seed_input = dest + (seed_input - start)
                    break
        min_dest = min(min_dest, seed_input)
    return min_dest

def lowest_location_2(seed_ranges, dict_maps, list_maps):
    """
    Calculates the lowest location among the locations of all seed ranges.

    Parameters:
        seeds (List[int, int]): List of seed ranges.
        dict_maps (dict): Dictionary mapping categories to lists of lists. 
                          Each list contains (destination, start, range).
        list_maps (List[strings]): List with the names of the dict_maps keys to iterate

    Returns:
        int: The lowest location found.
    """
    seeds = seed_ranges
    for name in list_maps:
        list_values = dict_maps[name]
        outputs = []
        while len(seeds) > 0:
            s,e = seeds.pop()
            for dest, start, rang in list_values:
                dest, start, rang = int(dest), int(start), int(rang)
                ost = max(s, start)
                oe = min(e, start + rang)
                if ost < oe:
                    outputs.append((ost - start + dest, oe - start + dest))
                    if ost>s:
                        seeds.append((s,ost))
                    if e>oe:
                        seeds.append((oe,e))
                    break
            else:
                outputs.append((s,e))
        seeds = outputs
    return min(seeds)[0]

#Solution
if __name__ == "__main__":

    #Code to open the input file
    path = os.getcwd()
    FILE = "day5.txt"

    with open(path + '/' + FILE, encoding = 'utf-8') as f:
        lines = f.read().strip()
        lines = lines.split('\n\n')

    seeds_input = lines[0].split(": ")[1].split(" ")
    seeds_input = [int(x) for x in seeds_input]

    dict_maps_input = {}
    for i in range(1,len(lines)):
        parts = lines[i].split(":\n")
        dict_maps_input[parts[0]] = [x.split(" ") for x in lines[i].split(":\n")[1].split("\n")]

    seed_ranges_input = [(seeds_input[i],seeds_input[i] + seeds_input[i+1])
                         for i in range(0,len(seeds_input),2)]

    list_maps_input = [
        "seed-to-soil map",
        "soil-to-fertilizer map",
        "fertilizer-to-water map",
        "water-to-light map",
        "light-to-temperature map",
        "temperature-to-humidity map",
        "humidity-to-location map"
    ]
    start_time = time.time()
    #Part 1
    print("Solution part 1: ", lowest_location(seeds_input,
                                               dict_maps_input))
    #Part 2
    print("Solution part 2: ", lowest_location_2(seed_ranges_input,
                                                 dict_maps_input,
                                                 list_maps_input))
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
