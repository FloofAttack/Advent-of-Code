# Part 1
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
    
# formula for box surface area: 2*l*w + 2*w*h + 2*h*l + the area of the smallest side
# Example
# 2x3x4
# lxwxh
# l = 2 d[0]
# w = 3 d[1]
# h = 4 d[2]
# d = [2,3,4]
# surface_area = 2*d[0]*d[1] + 2*d[1]*d[2] + 2*d[2]*d[0]
# d.remove(max(d))
# surface_area += d[0]*d[1]
# excess depends on finding the smallest two sides
# print(f"surface area: {surface_area}")
lines = line_reader(file)
required_area = 0
required_ribbon = 0
for l in lines:
    l = l.split("x")
    l = [int(e) for e in l]
    required_area += 2*l[0]*l[1] + 2*l[1]*l[2] + 2*l[2]*l[0]
    l_max = max(l)
    l.remove(l_max)
    required_area += l[0]*l[1]
    required_ribbon += 2*l[0] + 2*l[1] + l[0]*l[1]*l_max
print(f"required area is {required_area}")
print(f"required ribbon is {required_ribbon}")
