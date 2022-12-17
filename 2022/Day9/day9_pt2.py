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

def dist_calc(h_pos,t_pos):
    hd = h_pos[0] - t_pos[0]
    td = h_pos[1] - t_pos[1]
    htd = np.sqrt(hd**2 + td**2)
    return htd

def tail_move(h_in,t_in):
    h_pos = h_in.copy()
    t_pos = t_in.copy()
    """ Feed in the two adjacent knot positions to check """
    # Step 1) do they actually need to move?
    if dist_calc(h_pos,t_pos) < np.sqrt(2)+1e-6:
        # tail doesn't need to move
        return t_pos
    else:
        xd = h_pos[0] - t_pos[0]
        yd = h_pos[1] - t_pos[1]
        ht_phase = np.angle(complex(xd,yd),deg=True)
        # all possible values of ht_phase:
        # 0,90,45,-45,-90,-135,180,135
        if ht_phase == 0:
            t_pos[0] += 1
        elif ht_phase == 90:
            t_pos[1] += 1
        elif ht_phase == 180:
            t_pos[0] += -1
        elif ht_phase == -90:
            t_pos[1] += -1
        elif ht_phase > 0 and ht_phase < 90:
            t_pos[0] += 1
            t_pos[1] += 1
        elif ht_phase > 90 and ht_phase < 180:
            # print("dafuq")
            t_pos[0] += -1
            t_pos[1] += 1
        elif ht_phase < -90:
            # print("ola")
            t_pos[0] += -1
            t_pos[1] += -1
        elif ht_phase < 0:
            # print("here")
            t_pos[0] += 1
            t_pos[1] += -1
        else:
            raise Exception("not an expected angle")
    return t_pos

def rope_move(direction,rope):
    # rope is a list of coords.
    # rope[0] is the head
    # rope[1:knots] are the tails
    # function moves the head by one and checks all the tails.

    if direction == "R":
        # first move the head to the right
        rope[0][0] += 1
        print(f"moving Right by {1}")
        for i in range(1,len(rope)):
            tail = tail_move(rope[i-1],rope[i])
            rope[i] = tail

    elif direction == "L":
        rope[0][0] += -1
        print(f"moving Left by {1}")
        for i in range(1,len(rope)):
            tail = tail_move(rope[i-1],rope[i])
            rope[i] = tail

    elif direction == "U":
        rope[0][1] += 1
        print(f"moving Up by {1}")
        for i in range(1,len(rope)):
            tail = tail_move(rope[i-1],rope[i])
            rope[i] = tail

    elif direction == "D":
        rope[0][1] += -1
        print(f"moving Down by {1}")
        for i in range(1,len(rope)):
            tail = tail_move(rope[i-1],rope[i])
            rope[i] = tail
    
    return rope

# H and T must be always touching or even overlapping.
# read in each line.
with open("input.txt") as f:
    file = f.readlines()
    
lines = line_reader(file)

# Part 2
# one head and 10 tails: 0 to 9
# each tail should call the function "rope_move"

rope = [ [11,5], [11,5], [11,5], [11,5], [11,5], [11,5], [11,5], [11,5], [11,5], [11,5] ]

tail_positions = []

for l in lines:
    direction = l.split(" ")[0]
    steps = int(l.split(" ")[1])
    for i in range(0,steps):
        rope = rope_move(direction,rope)
        tail_positions.append(rope[9])
        print(rope)
    print("\n")
    
tail_set = set([str(i) for i in tail_positions])
print(f"total unique coords covered by tail {len(tail_set)}")
    
    
