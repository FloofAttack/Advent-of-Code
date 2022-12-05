import numpy as np

# Part 1
with open('input.txt') as f:
    file = f.read()

directions = [*file]

count = 0
for d in directions:
    if d == "(":
        count = count + 1
    elif d == ")":
        count = count - 1
    else:
        print("Something else")
print("the count is")
print(count)

#########################################
# Part 2

count = 0
for d in range(0,len(directions)):
    if directions[d] == "(":
        count = count + 1
    elif directions[d] == ")":
        count = count - 1
    else:
        print("Something else")
    if count == -1:
        print("entered the basement")
        print(d+1)
