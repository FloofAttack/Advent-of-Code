# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 18:30:19 2022

@author: sfoster
"""
import sys
from imports_functions import *

with open("input.txt") as f:
    file = f.readlines()
# odd are the base values
# even are the encrypted values


# Opponent
# A = 1 # Rock
# B = 2 # Paper
# C = 3 # Scissors
# Me
# Y = 2 # Paper
# X = 1 # Rock
# Z = 3 # Scissors

print("Part 1")
# possible combinations
# A Y = W + 6 + 2 = 8
# A X = D + 3 + 1 = 4
# A Z = L + 0 + 3 = 3
# B Y = D + 3 + 2 = 5
# B X = L + 0 + 1 = 1
# B Z = W + 6 + 3 = 9
# C Y = L + 0 + 2 = 2
# C X = W + 6 + 1 = 7
# C Z = D + 3 + 3 = 6

lines = [ 8 if i == "A Y\n" else i for i in file]
lines = [ 4 if i == "A X\n" else i for i in lines]
lines = [ 3 if i == "A Z\n" else i for i in lines]
lines = [ 5 if i == "B Y\n" else i for i in lines]
lines = [ 1 if i == "B X\n" else i for i in lines]
lines = [ 9 if i == "B Z\n" else i for i in lines]
lines = [ 2 if i == "C Y\n" else i for i in lines]
lines = [ 7 if i == "C X\n" else i for i in lines]
lines = [ 6 if i == "C Z\n" else i for i in lines]

print(sum(lines))

# part 2
# X = L + 0
# Y = D + 3
# Z = W + 6

print("Part 2")
# possible combinations
# A Y = 3 + 1 = 4
# A X = 3 + 0 = 3
# A Z = 6 + 2 = 8
# B Y = 2 + 3 = 5
# B X = 0 + 1 = 1
# B Z = 6 + 3 = 9
# C Y = 3 + 3 = 6
# C X = 0 + 2 = 2
# C Z = 6 + 1 = 7

lines = [ 4 if i == "A Y\n" else i for i in file]
lines = [ 3 if i == "A X\n" else i for i in lines]
lines = [ 8 if i == "A Z\n" else i for i in lines]
lines = [ 5 if i == "B Y\n" else i for i in lines]
lines = [ 1 if i == "B X\n" else i for i in lines]
lines = [ 9 if i == "B Z\n" else i for i in lines]
lines = [ 6 if i == "C Y\n" else i for i in lines]
lines = [ 2 if i == "C X\n" else i for i in lines]
lines = [ 7 if i == "C Z\n" else i for i in lines]

print(sum(lines))
