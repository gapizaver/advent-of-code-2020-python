# Day 3: Toboggan Trajectory
# https://adventofcode.com/2020/day/3

f = open("input.txt", "r")
ground = f.read().splitlines()
f.close()

width = len(ground[0])
trees = 0   # number of trees hit
pos = 0     # my position

for line in ground:
    if line[pos%width] == "#":
        trees += 1;
    pos += 3

print(trees)
