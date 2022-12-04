# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 18:13:57 2022

@author: sfoster
"""
import sys
from imports_functions import *

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

# create list spaced by 1 from 0 to 3
#list(range(0,3+1))

#######################################################################################
# Part 1

# create a function which takes the ranges and generates explicit lists
overlap_counter = 0
for l in lines:
    pair = l.split(",")
    elf_1 = set(list(range(int(pair[0].split("-")[0]),int(pair[0].split("-")[1])+1)))
    elf_2 = set(list(range(int(pair[1].split("-")[0]),int(pair[1].split("-")[1])+1)))
    if (elf_2 <= elf_1) or (elf_1 <= elf_2): # Python set method issubset
        overlap_counter += 1
        # print("overlap detected")
        # print(f"first elf {elf_1}")
        # print(f"second elf {elf_2}")

print("total complete overlaps")        
print(overlap_counter)

#######################################################################################
# Part 2
# looking for any overlap whatsoever.
overlap_counter = 0
for l in lines:
    pair = l.split(",")
    elf_1 = set(list(range(int(pair[0].split("-")[0]),int(pair[0].split("-")[1])+1)))
    elf_2 = set(list(range(int(pair[1].split("-")[0]),int(pair[1].split("-")[1])+1)))
    if elf_1.isdisjoint(elf_2) == False:
        overlap_counter += 1
        # print("overlap detected")
        # print(f"first elf {elf_1}")
        # print(f"second elf {elf_2}")

print("total partial overlaps")        
print(overlap_counter)
