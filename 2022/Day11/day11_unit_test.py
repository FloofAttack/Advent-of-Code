import numpy as np

monkies = [0, 1, 2, 3,]
tests = [23, 19, 13, 17]
operation = ["*", "+", "*i", "+"]
operand = [19, 6, 0, 3]
actions = [
        [2,3],
        [2,0],
        [1,3],
        [0,1]
        ]
items = [
        [79,98],
        [54, 65, 75, 74],
        [79, 60, 97],
        [74]
        ]
items_inspected = [0, 0, 0, 0]
#worry = 0
rounds = 10000
# might have to use float64? dtype=float64
# might have to force unsigned 64-bit integer?
for r in range(0,rounds):
    print(f"round {r+1}")
    for i in range(0,4):
        for index,item in enumerate(items[i].copy()):
            if item > 0:
                items_inspected[i] += 1
            if operation[i] == "*":
                worry = item * operand[i]
                #worry = np.multiply(item,operand[i], dtype=np.int64)
                #worry = np.multiply(item,operand[i])
            elif operation[i] == "+":
                worry = item + operand[i]
                #worry = np.add(item,operand[i], dtype=np.int64)
                #worry = np.add(item,operand[i])
            elif operation[i] == "*i":
                worry = item * item
                #worry = np.multiply(item,item, dtype=np.int64)
                #worry = np.multiply(item,item)
            elif operation[i] == "+i":
                worry = item + item
                #worry = np.add(item,item, dtype=np.int64)
                #worry = np.add(item,item)
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
