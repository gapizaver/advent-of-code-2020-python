# Day 15: Rambunctious Recitation
# https://adventofcode.com/2020/day/15

# still trying to find a way to optimise the algorithm
# takes cca 0.5min to find the result (30000000th card)

from collections import defaultdict

# input
inpt = [5, 1, 9, 18, 13, 8, 0]

# when numbers were said the last time
# number: time
lastly_said = defaultdict(int)

# add numbers in input to lastly_said
for i, a in enumerate(inpt[:-1]):
    lastly_said[a] = i

# most recently spoken number
spoken_num = inpt[-1]

# find 2020th number
i = len(inpt) - 1
while i < 18 - 1:
    if spoken_num not in lastly_said.keys():
        lastly_said[spoken_num] = i
        spoken_num = 0
    else:
        new_spoken_num = i - lastly_said[spoken_num]
        lastly_said[spoken_num] = i
        spoken_num = new_spoken_num

    i += 1

# result
print(spoken_num)
