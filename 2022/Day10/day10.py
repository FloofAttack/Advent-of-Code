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

# read in each line.
with open("input.txt") as f:
    file = f.readlines()
    
lines = line_reader(file)
total_cycles = 0
var_X = 1 # starting value given in the description
instruct = []
operand = []
interesting = 0

# Part 1
# work out the total number of required total_cycles
for l in lines:
    if l == "noop":
        total_cycles += 1
        instruct.append("noop")
        operand.append(0)
    if l.split(" ")[0] == "addx":
        total_cycles += 2
        instruct.append("addx")
        instruct.append("addx")
        operand.append(0)
        operand.append(int(l.split(" ")[1]))
print(f"required number of cycles {total_cycles}")

for c in range(0,total_cycles):
    if c == 20 - 1:
        print(f" interesting value at 20 cycles {(c+1)*var_X}")
        print(f" value of var_X {var_X}")
        interesting += (c+1)* var_X
    elif c == 60 - 1:
        print(f" interesting value at 60 cycles {(c+1)*var_X}")
        print(f" value of var_X {var_X}")
        interesting += (c+1)* var_X
    elif c == 100 - 1:
        print(f" interesting value at 100 cycles {(c+1)*var_X}")
        print(f" value of var_X {var_X}")
        interesting += (c+1)* var_X
    elif c == 140 - 1:
        print(f" interesting value at 140 cycles {(c+1)*var_X}")
        print(f" value of var_X {var_X}")
        interesting += (c+1)* var_X
    elif c == 180 - 1:
        print(f" interesting value at 180 cycles {(c+1)*var_X}")
        print(f" value of var_X {var_X}")
        interesting += (c+1)* var_X
    elif c == 220 - 1:
        print(f" interesting value at 220 cycles {(c+1)*var_X}")
        print(f" value of var_X {var_X}")
        interesting += (c+1)* var_X
    var_X += operand[c]
print(f"total interesting sum {interesting}")

# Part 2
print("\n")
print("Part 2: CRT")
# 40 pixels wide
# 6 pixels high
# var_X is the sprite position, starting at 1
# CRT index starts from 0
var_X = 1 # starting value given in the description
crt = []
horiz = 0

for c in range(0,total_cycles):
    # draw the screen here
    if c%40 == 0 and c > 0:
        horiz += 40
    if (c - horiz) == (var_X - 1) or (c - horiz) == var_X or (c - horiz) == (var_X + 1):
        crt.append("#")
    else:
        crt.append(".")
    var_X += operand[c]

# printing function: accounting for CRT aspect ratio
new_string = ""
for i,character in enumerate(crt):
    if i%40 == 0:
       new_string += '\n'
    new_string += character
print(new_string)
