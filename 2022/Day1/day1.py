# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 18:30:19 2022

@author: sfoster
"""
import sys
from imports_functions import *

with open("input.txt") as f:
    lines = f.readlines()

# Create a calorie finding function
def highest_calorie_finder(lines):
    totals = []
    running_total = 0
    for i in range(0,len(lines)):
        if len(lines[i].split("\n")[0]) == 0:
            totals.append(running_total)
            running_total = 0
        else:
            running_total += int(lines[i].split("\n")[0])
        if i == len(lines) - 1:
            totals.append(running_total)
    return totals

totals = highest_calorie_finder(lines)

highest_carriers = []
for i in range(0,3):
    print("showing max totals")    
    print(np.max(totals))
    # remove this items from the totals list
    highest_carriers.append(totals.pop(totals.index(np.max(totals))))

print("the sum of the top three is")
print(np.sum(highest_carriers))
