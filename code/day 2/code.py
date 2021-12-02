import re

def Chal2_1():
    lines = []
    horizontalPos = 0
    depth = 0
    with open('input.txt') as f:
       lines = f.readlines()
    for l in lines:
        x = int(re.findall("\d", l)[0])
        if re.findall("forward", l):
            horizontalPos += x
        elif re.findall("up", l):
            depth -= x
        elif re.findall("down", l):
            depth += x
    return horizontalPos, depth, (horizontalPos * depth)
def Chal2_2():
    lines = []
    horizontalPos = 0
    depth = 0
    aim = 0
    with open('input.txt') as f:
       lines = f.readlines()
    for l in lines:
        x = int(re.findall("\d", l)[0])
        if re.findall("forward", l):
            horizontalPos += x
            depth += aim * x
        elif re.findall("up", l):
            aim -= x
        elif re.findall("down", l):
            aim += x
    return horizontalPos, depth, aim, (horizontalPos * depth)

print(Chal2_1())
print(Chal2_2())