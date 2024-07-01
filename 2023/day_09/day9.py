"""
This module contains the solution to the Day 9 Advent of Code challenge.
"""
import os
import time

def solution(report_list):
    """
    Processes a list of reports to compute the next logical value
    of each report.

    For each report, it repeatedly calculates the difference
    between consecutive elements until all elements in the report
    are the same. It then sums the last elements obtained 
    in each iteration, which correspond with the following logical
    value of the input report, and adds it to the overall sum.

    Args:
    report_list (list): A list of lists, where each inner list
    is a report containing integers.

    Returns:
    int: The sum of the computed values from each report.
    """
    ans = 0
    for report in report_list:
        values = []
        values.append(report[-1])
        while len(set(report)) > 1:
            j = 0
            while j < len(report) - 1:
                report[j] = report[j + 1] - report[j]
                j += 1
            report = report[:-1]
            values.append(report[-1])
        next_value = sum(values)
        ans += next_value
    return ans

def looper(values):
    """
    Computes a final value by iteratively subtracting elements in a list
    from an accumulator.

    Args:
    values (list): A list of integers.

    Returns:
    int: The final computed value after iterating through the list.
    """
    act = 0
    for value in values:
        act = value - act
    return act

def solution2(report_list):
    """
    Processes a list of reports to compute a sum of values derived from each report.

    For each report, it repeatedly calculates the difference between consecutive elements 
    until all elements in the report are the same. It then reverses the list of the first 
    elements obtained in each iteration and computes a final value using the looper function.
    This final vlaue corresponds to the previous logical value of each report.

    Args:
    report_list (list): A list of lists, where each inner list is a report containing integers.

    Returns:
    int: The sum of the computed values from each report.
    """
    ans = 0
    for report in report_list:
        values = []
        values.append(report[0])
        while len(set(report)) > 1:
            j = 0
            while j < len(report) - 1:
                report[j] = report[j + 1] - report[j]
                j += 1
            report = report[:-1]
            values.append(report[0])
        values.reverse()
        next_value = looper(values)
        ans += next_value
    return ans


#Solution
if __name__ == "__main__":

    #Code to open the input file
    path = os.getcwd()
    FILE = "day9.txt"

    with open(path + '/' + FILE, encoding = 'utf-8') as f:
        lines = f.read().strip()
        lines = lines.split('\n')

    reports_input = [x.split(" ") for x in lines]
    reports_input = [[int(x) for x in report] for report in reports_input]

    start_time = time.time()
    # Part 1
    print("Solution part 1: ", solution(reports_input))
    # Part 2
    reports_2_input = [x.split(" ") for x in lines]
    reports_2_input = [[int(x) for x in report] for report in reports_2_input]
    print("Solution part 2: ", solution2(reports_2_input))
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
