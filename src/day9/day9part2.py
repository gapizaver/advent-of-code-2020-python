# Day 9: Encoding Error
# https://adventofcode.com/2020/day/9

from itertools import combinations

# invalid number = 1398413738 (part1)
invalid_number = 1398413738

# read the input
f = open("input.txt", "r")
txt = f.read().splitlines()
f.close()

# find contiguous range of numbers that sum to the invalid number:
# restult is sum of the smallest and largest number in this contiguous range:
result = 0
lst = list()
for i, line in enumerate(txt):
    for j in range(i, len(txt)):
        lst.append(int(txt[j]))
        if sum(lst) == invalid_number:
            result = min(lst) + max(lst)
            break
        elif sum(lst) > invalid_number: # optimisation
            break
    if result != 0:
        break
    else:
        del lst[:]

print(result)
