import os, re
os.chdir('.\day_2')

#Part 1, first method (using findall regex + array (which is O(N) in space))
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

#Part 2, better method (using compile which selects only the first word + the first digit found, only read (O(1) space complexity))
def Chal2_2():
    horizontalPos = 0
    depth = 0
    aim = 0
    with open('input.txt') as f:
        pattern = re.compile('(\w+) (\d+)')
        for l in f:
            info = pattern.search(l) #seachs the string with the given pattern (1 word, 1 digit, don't retain the space or \n)
            direction = info.group(1) #info.group(1) is the direction (up, down, fwd)
            x = int(info.group(2))
            if direction == "forward":
                horizontalPos += x
                depth += aim * x
            elif direction == "up":
                aim -= x
            elif direction == "down":
                aim += x
    return horizontalPos, depth, aim, (horizontalPos * depth)


print(Chal2_1())
print(Chal2_2())