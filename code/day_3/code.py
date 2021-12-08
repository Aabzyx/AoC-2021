import os
os.chdir(".\day_3")

def BinaryToDecimal(number):
    returned = 0
    for i in range(len(number)):
        returned += int(number[i]) * pow(2, len(number) - i - 1)
    return returned

def Chal3_1():
    lines = []
    maxZero = 0
    gammaRateBin = ""
    epsilonRateBin = ""
    with open("input.txt") as f:
        lines = f.read().split("\n")
    for x in range(len(lines[0])):
        for line in range(len(lines)):
            if lines[line][x] == "0":
                maxZero += 1
        if maxZero > len(lines) - maxZero:
            gammaRateBin += '0'
            epsilonRateBin += '1'
        elif len(lines) - maxZero > maxZero:
            gammaRateBin += '1'
            epsilonRateBin += '0'
        else:
            print("Not supposed to be equal")
        maxZero = 0
    gammaRateDec = BinaryToDecimal(gammaRateBin)
    epsilonRateDec = BinaryToDecimal(epsilonRateBin)
    return gammaRateDec, epsilonRateDec, gammaRateDec * epsilonRateDec

def Chal3_2():
    oxyPossibilities = []
    maxZero = 0
    with open("input.txt") as f:
        oxyPossibilities = f.read().split("\n")
    coPossibilities = oxyPossibilities.copy()
    for x in range(len(oxyPossibilities[0])):
        for line in oxyPossibilities:
            if line[x] == "0":
                maxZero += 1
        if maxZero > len(oxyPossibilities) - maxZero:
            for line in oxyPossibilities.copy(): #SUPER IMPORTANT, otherwise the list's length reduces too fast
                if line[x] != '0' and len(oxyPossibilities) > 1:
                    oxyPossibilities.remove(line)
        else:
            for line in oxyPossibilities.copy():
                if line[x] != '1' and len(oxyPossibilities) > 1:
                    oxyPossibilities.remove(line)
        print(oxyPossibilities)
        maxZero = 0

        for line in coPossibilities:
            if line[x] == "0":
                maxZero += 1
        if maxZero > len(coPossibilities) - maxZero:
            for line in coPossibilities.copy():
                if line[x] != '1' and len(coPossibilities) > 1:
                    coPossibilities.remove(line)
        else:
            for line in coPossibilities.copy():
                if line[x] != '0' and len(coPossibilities) > 1:
                    coPossibilities.remove(line)
        maxZero = 0
    oxGenerator = BinaryToDecimal(oxyPossibilities[0])
    coScrubber = BinaryToDecimal(coPossibilities[0])
    return oxGenerator, coScrubber, oxGenerator * coScrubber


print(Chal3_2())