#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 19:55:56 2024

@author: auro
"""
import os

#Code to open the input file
path = os.getcwd()
FILE = "day4.txt"

with open(path + '/' + FILE, encoding = 'utf-8') as f:
    lines = f.read().strip()
    lines = lines.split('\n')
    lines = [x.split(':')[1].split("|") for x in lines]

import time
time0 = time.time()
ans = 0
dict_wins = dict()
scratchcards = 0


for i, numbers in enumerate(lines):

    win_numbers = numbers[0].split(" ")
    have_numbers = numbers[1].split(" ")
    set_win = set()
    points_pow = -1
    check = False
    for win_num in win_numbers:
        if win_num.isalnum():
            set_win.add(win_num)
    for num in have_numbers:
        if num.isalnum() and num in set_win:
            check = True
            points_pow += 1 
    dict_wins[i] = [points_pow+1, 1]
    if check:
        ans += 2**points_pow

print(ans)
            
for key in dict_wins:
    for key2 in range(key+1, key+1+dict_wins[key][0]):
        dict_wins[key2][1] +=dict_wins[key][1]
    scratchcards += (dict_wins[key][1])

        

print(scratchcards)

time1 = time.time()
print(time1-time0)



