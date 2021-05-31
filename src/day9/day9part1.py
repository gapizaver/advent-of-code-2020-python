# Day 9: Encoding Error
# https://adventofcode.com/2020/day/9

# read the input
f = open("input.txt", "r")
txt = f.read().splitlines()
f.close()

# check if 2 numburs from list l add to the number a
def check_number(a, l):
    for i, b in enumerate(l):
        for j, c in enumerate(l):
            if b != c and b + c == a:
                return True

# 25 numbers in front
preamble = []

# find number which is not sum of any 2 numbers preamble:
for i, line in enumerate(txt):
    if i >= 25:
        if not check_number(int(line), preamble):
            print(line)
            break
        preamble = preamble[1:]

    preamble.append(int(line))
