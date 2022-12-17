# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 14:51:44 2022

@author: sfoster
"""
import sys
import numpy as np

def line_reader(lines):
    output_lines = []
    for i in range(0,len(lines)):
        if i < len(lines):
            output_lines.append(lines[i].split("\n")[0])
        else:
            output_lines.append(lines[i])
    return output_lines

def tail_move(h_pos,t_pos):
    hd = h_pos[0] - t_pos[0]
    td = h_pos[1] - t_pos[1]
    htd = np.sqrt(hd**2 + td**2)
    return htd

def rope_move(direction,h_pos,t_pos):
    h = h_pos.copy()
    t = t_pos.copy()
    if direction == "R":
        htd_start = tail_move(h,t)
        h[0] += 1
        # print(f"moving Right by {1}")
        htd = tail_move(h,t)
        if htd > np.sqrt(2):
            t[0] = h[0] - 1
            t[1] = h[1]

    elif direction == "L":
        htd_start = tail_move(h,t)
        h[0] += -1
        # print(f"moving Left by {1}")
        htd = tail_move(h,t)
        if htd > np.sqrt(2):
            t[0] = h[0] + 1
            t[1] = h[1]

    elif direction == "U":
        htd_start = tail_move(h,t)
        h[1] += 1
        # print(f"Movin on Up by {1}")
        htd = tail_move(h,t)
        if htd > np.sqrt(2):
            t[1] = h[1] - 1
            t[0] = h[0]

    elif direction == "D":
        htd_start = tail_move(h,t)
        h[1] += -1
        # print(f"Gettin Down by {1}")
        htd = tail_move(h,t)
        if htd > np.sqrt(2):
            t[1] = h[1] + 1
            t[0] = h[0]

    return h, t

# H and T must be always touching or even overlapping.
# read in each line.
with open("input.txt") as f:
    file = f.readlines()
    
lines = line_reader(file)

# Part 1
# first map the movement of H
h_pos = [0,0]
t_pos = [0,0]
tail_positions = []
for l in lines:
    direction = l.split(" ")[0]
    steps = int(l.split(" ")[1])
    for i in range(0,steps):
        h_pos, t_pos = rope_move(direction,h_pos,t_pos)
        tail_positions.append(t_pos)
    print(f"head position {h_pos}")
    print(f"tail position {t_pos}")
    print(f"head tail distance is {tail_move(h_pos,t_pos)}")

tail_set = set([str(i) for i in tail_positions])
print(f"total unique coords covered by tail {len(tail_set)}")

# Part 2
# Can't do one by one! When the head moves up 2, it pulls all the tails not overlapping!

