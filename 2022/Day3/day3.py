# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 13:19:43 2022

@author: sfoster
"""
import sys
from imports_functions import *
import string

def line_reader(lines):
    output_lines = []
    for i in range(0,len(lines)):
        if i < len(lines):
            output_lines.append(lines[i].split("\n")[0])
        else:
            output_lines.append(lines[i])
    return output_lines

with open("input.txt") as f:
    file = f.readlines()
    
lines = line_reader(file)

# split each line into 2: one for each compartment
compartment_1 = []
compartment_2 = []

for l in lines:
    compartment_1.append(l[0:int(len(l)/2)])
    compartment_2.append(l[int(len(l)/2):len(l)])
    
# seach through each compartment and find the common item
common_elements = []
for i in range(0,len(compartment_1)):
    common_var = ""
    c1 = [*compartment_1[i]]
    c2 = [*compartment_2[i]]
    if len(c1) != len(c2):
        print("all to hell!")
    else:
        for e in range(0,len(c1)):
            if c1[e] in c2:# not in common_elements:
                common_var = c1[e]
    common_elements.append(common_var)
    
# create a dictionary to look up the priority of each item
letters = [*string.ascii_lowercase + string.ascii_uppercase]
numbers = uc_number = [x for x in range(1,52+1)]

lookup_dict = dict(zip(letters,numbers))

priority_sum = 0
for ce in common_elements:
    priority_sum += lookup_dict[ce]
    
print(priority_sum)
####################################################################################################
# Part 2
## split the original lines into lists of 3 to be passed to the above function
priority_sum = 0
chunks = []
for i in range(0, len(lines), 3):
    chunks.append(lines[i:i+3])    
# find the common element in each group of 3 lines
common_elements = []
for c in chunks:
    c0 = [*c[0]]
    c1 = [*c[1]]
    c2 = [*c[2]]
    common_elements.append(list(set(c0) & set(c1) & set(c2)))

for ce in common_elements:
    priority_sum += lookup_dict[ce[0]]
    
print(priority_sum)
