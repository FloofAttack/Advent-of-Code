# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 14:51:44 2022

@author: sfoster
"""
import sys

def line_reader(lines):
    output_lines = []
    for i in range(0,len(lines)):
        if i < len(lines):
            output_lines.append(lines[i].split("\n")[0])
        else:
            output_lines.append(lines[i])
    return output_lines

# read in each line.
with open("input.txt") as f:
    file = f.readlines()
    
lines = line_reader(file)
 
# Part 1 ###########################################################################
# find the first run of 4 unique characters
for l in lines:
    l_list = [*l]
    for i in range(0,len(l_list)-3): # step through each character in the string
        window = l_list[i:i+4]
        if len(window) == len(set(window)): # we know all items are unique
            print(f"packet starting at position {i+4}")
            break

# Part 2 ###########################################################################
# find the first run of 4 unique characters
for l in lines:
    l_list = [*l]
    for i in range(0,len(l_list)-13): # step through each character in the string
        window = l_list[i:i+14]
        if len(window) == len(set(window)): # we know all items are unique
            print(f"message starting at position {i+14}")
            break