# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 18:13:57 2022

@author: sf
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
with open("input_moves.txt") as f:
    file = f.readlines()
    
lines = line_reader(file)

# hard-code the initial crate stacks as lists
# stack_1 = ["Z", "N"]
# stack_2 = ["D", "C", "M"]
# stack_3 = ["P"]

# stack = [["N", "Z"], ["D", "C", "M"], ["P"]] # test input 1
# stack = [ ["D", "N", "Z"], ["C", "M"], ["P"] ]  # test input 2
stack = [ # sorry not sorry, I used VIM to create this :P
    ["P", "D", "Q", "R", "V", "B", "H", "F"],
    ["V", "W", "Q", "Z", "D", "L"],
    ["C", "P", "R", "G", "Q", "Z", "L", "H"],
    ["B", "V", "J", "F", "H", "D", "R"],
    ["C", "L", "W", "Z"],
    ["M", "V", "G", "T", "N", "P", "R", "J"],
    ["S", "B", "M", "V", "L", "R", "J"],
    ["J", "P", "D"],
    ["V", "W", "N", "C", "D"]
    ]

# translate the moves and operate on them line by line
for l in lines:
    number = int(l.split(" ")[1]) # there is probably a -1 gone wrong!!
    from_stack = int(l.split(" ")[3]) - 1
    to_stack = int(l.split(" ")[5]) - 1
    crane_carry = stack[from_stack][0:number]
    crane_carry.reverse() # the change needed for part 2
    [stack[from_stack].remove(e) for e in crane_carry]
    [stack[to_stack].insert(0,e) for e in crane_carry]
    # stack[to_stack].insert(0, crane_carry)
    
print("".join([e[0] for e in stack]))
