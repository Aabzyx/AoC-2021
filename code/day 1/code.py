def Chal1_1():
    depth = []
    cpt = 0
    with open('input.txt') as f:
        depth = f.readlines()
    for x in range(1, len(depth)):
        if int(depth[x]) > int(depth[x - 1]):
            cpt += 1
    return cpt

def Chal1_2():
    depth = []
    cpt = 0
    with open('input.txt') as f:
        depth = f.readlines()
        depth = [int(x) for x in depth]
    for x in range(len(depth) - 3):
        if sum(depth[x : x + 3]) < sum(depth[x + 1 : x + 4]):
            cpt += 1
    return cpt


print(Chal1_1(), Chal1_2())