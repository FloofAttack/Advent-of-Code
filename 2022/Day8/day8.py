# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 14:51:44 2022

@author: sfoster
"""
import sys
import numpy as np

def grid_reader(lines):
    output_lines = []
    output_grid = []
    for i in range(0,len(lines)):
        if i < len(lines):
            output_lines.append(lines[i].split("\n")[0])
        else:
            output_lines.append(lines[i])
    for o in output_lines:
        output_grid.append([*o])
    return output_grid

def tree_spy(grid,tree_coord):
    left = True
    left_count = 0
    right = True
    right_count = 0
    down = True
    down_count = 0
    up = True
    up_count = 0
    visible = False
    scenic_score = 0
    tree_val = grid[tree_coord[0]][tree_coord[1]]
    # print(f"chosen tree height is {tree_val}")
    
    # check "left" by decrementing columns until we are checking the edge tree
    for col in range(tree_coord[1]-1,-1,-1):
        if grid[tree_coord[0]][col] >= tree_val:
            left = False
            left_count += 1
            break
        else:
            left_count += 1
    # check "right" by incrementing columns until we are checking the edge tree
    for col in range(tree_coord[1]+1,max_col):
        if grid[tree_coord[0]][col] >= tree_val:
            right = False
            right_count += 1
            break
        else:
            right_count += 1
    # check "up" by decrementing rows until we are checking the edge tree
    for row in range(tree_coord[0]-1,-1,-1):
        if grid[row][tree_coord[1]] >= tree_val:
            up = False
            up_count += 1
            break
        else:
            up_count += 1
    # check "down" by incrementing rows until we are checking the edge tree
    for row in range(tree_coord[0]+1,max_rows,1):
        if grid[row][tree_coord[1]] >= tree_val:
            down = False
            down_count += 1
            break
        else:
            down_count += 1
    if left == True or right == True or up == True or down == True:
        visible = True
    else:
        visible = False
    scenic_score = left_count*right_count*up_count*down_count
    return visible, scenic_score

# read in each line.
with open("input.txt") as f:
    file = f.readlines()
    
grid = grid_reader(file)

max_rows = len(grid[0])
max_col = len(grid)


# looking for 4 conditions to be true for each tree
# OR all of these conditions for Part 1

# Loop through all the trees to find the visible ones
visible = []
for c in range(0,max_col):
    visible_row = []
    for r in range(0,max_rows):
        visible_row.append(tree_spy(grid,[r,c])[0])
        # print([r,c])
    visible.append(visible_row)

# Loop through all trees collecting the scenic scores Part 2
scenic_scores = []
for r in range(0,max_rows):
    scenic_row = []
    for c in range(0,max_col):
        scenic_row.append(tree_spy(grid,[r,c])[1])
        # print([r,c])
    scenic_scores.append(scenic_row)
print(f"max scenic score possible: {np.max(scenic_scores)}")

# Pick one tree as a test
"""
tree_coord = [1,2]
tree_val = grid[tree_coord[0]][tree_coord[1]]
print(tree_val)
# Find it's scenic score
scenic_score  = tree_spy(grid,tree_coord)[1]
print(f"scenic score {scenic_score}")
"""
# total number of visible trees
count = 0
for i in range(0,len(visible)):
    for j in range(0,len(visible[0])):
        if visible[i][j] == True:
            count += 1
print(f"number of visible trees {count}")
