#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 19:55:56 2024

@author: auro
"""
import os

#Code to open the input file
path = os.getcwd()
FILE = "day3.txt"

with open(path + '/' + FILE, encoding = 'utf-8') as f:
    lines = f.readlines()
    lines = [item.strip("\n") for item in lines]
    
def check_valid(lines,i,j,j_len):
    check = False
    gear = False
    gear_pos = (-1,-1)
    
    row_min = max(i,1)
    row_max = min(i, len(lines)-2)
    
    col_min = max(j,1)
    col_max = min(j+j_len, len(lines[0])-1)
    
    for i in range(row_min-1, row_max+2):
        for j in range(col_min-1, col_max+1):
            char = lines[i][j]
            if char != '.' and (not char.isdigit()):
                #print(char)
                check = True
                if char == '*':
                    gear = True
                    gear_pos = (i,j)
                return check, gear, gear_pos
            #print(i,j, lines[i][j])

    return check, gear, gear_pos
    
def read_num(lines):
    visited = set()
    gear_dict  = dict()
    count = 0
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if (i,j) in visited:
                continue
            if char.isdigit():
                visited.add((i,j))
                j_start = j
                number = char
                while (j+1)<len(line) and lines[i][j+1].isdigit():
                    visited.add((i,j+1))
                    number += lines[i][j+1]
                    j += 1
                check_number, gear, gear_pos = check_valid(lines,i,j_start,j-j_start+1)
                if gear:
                    if gear_dict.get(gear_pos,[0,0])[0] >= 1:
                        gear_dict[gear_pos][0] += 1
                        gear_dict[gear_pos][1] = gear_dict.get(gear_pos)[1]*int(number)
                    else:
                        gear_dict[gear_pos] = [1, int(number)]              
                #print(number, check_number)
                if check_number:
                    count += int(number)
                #print(number, i,j_start, j-j_start+1)
    print(count)
    #print(gear_dict)
    sum_gear = 0
    for key in gear_dict:
        if gear_dict[key][0]>=2:
            sum_gear+=gear_dict[key][1]

    print(sum_gear)
    return count
            
import time
time0 = time.time()
read_num(lines)
time1 = time.time()
print(time1-time0)
#check_valid(lines,2,6,3)
