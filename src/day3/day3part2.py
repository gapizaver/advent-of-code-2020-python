# Day 3: Toboggan Trajectory
# https://adventofcode.com/2020/day/3

f = open("input.txt", "r")
ground = f.read().splitlines()
f.close()

width = len(ground[0])
moving_patterns = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]] # x and y of moving
answer = 1

# for every pattern find number of trees hit
for moving_pattern in moving_patterns:
    pos = 0
    trees = 0

    for i in range(0, len(ground), moving_pattern[1]):
        # print(ground[i])
        if ground[i][pos%width] == "#":
            trees += 1
        pos += moving_pattern[0]

    answer *= trees # multiply number of trees

print(answer)
