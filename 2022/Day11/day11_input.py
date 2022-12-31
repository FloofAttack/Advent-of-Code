import numpy as np

monkies = [0, 1, 2, 3, 4, 5, 6, 7]
tests = [2, 7, 3, 17, 11, 19, 5, 13]
operation = ["*", "+", "+", "+", "+", "*", "*i", "+"]
operand = [5, 7, 5, 8, 4, 2, 0, 6]
actions = [
        [4,3],
        [5,6],
        [7,0],
        [1,5],
        [3,1],
        [6,2],
        [2,7],
        [4,0]
        ]
items = [
        [80],
        [75, 83, 74],
        [86, 67, 61, 96, 52, 63, 73],
        [85, 83, 55, 85, 57, 70, 85, 52],
        [67, 75, 91, 72, 89],
        [66, 64, 68, 92, 68, 77],
        [97, 94, 79, 88],
        [77, 85]
        ]
items_inspected = [0, 0, 0, 0, 0, 0, 0, 0]
rounds = 10000
# might have to use float64? dtype=float64
# might have to force unsigned 64-bit integer?
for r in range(0,rounds):
    print(f"round {r+1}")
    for i in range(0,len(monkies)):
        for index,item in enumerate(items[i].copy()):
            if item > 0:
                items_inspected[i] += 1
            if operation[i] == "*":
                worry = item * operand[i]
            elif operation[i] == "+":
                worry = item + operand[i]
            elif operation[i] == "*i":
                worry = item * item
            elif operation[i] == "+i":
                worry = item + item
            #worry = np.floor(worry/3) # Part 1
            worry = worry%np.prod(tests) # Part 2
            if worry%tests[i] == 0:
                items[actions[i][0]].append(worry)
            else:
                items[actions[i][1]].append(worry)
            items[i].remove(item)
    #print(f"ongoing items inspected {items_inspected}")
    print(f"current worry: {worry}")
#print(items)
print(f"final items inspected {items_inspected}")
items_inspected.sort()
print(f"monkey business {items_inspected[-1]*items_inspected[-2]}")
