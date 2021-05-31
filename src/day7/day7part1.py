# Day 7: Handy Haversacks
# https://adventofcode.com/2020/day/7

from collections import defaultdict


# get all the possible color of the bag color's parents
# parent color can contain this bag color
def get_parents(bags):
    global parents
    parents = parents.union(bags)

    for bag in bags:
        if bag in bag_colors.keys():
            get_parents(bag_colors[bag])


# read the input
f = open("input.txt", "r")
txt = f.read().splitlines()
f.close()

# dictionary of all bag colors and their parents
# color: possible parents
bag_colors = defaultdict(set)

# fill the dictionary
for line in txt:
    words = line.split()
    if words[4] == "no":
        continue

    parent_color = words[0] + words[1]
    for i in range(5, len(words), 4):
        color = words[i] + words[i + 1]
        bag_colors[color].add(parent_color)


shinygold_parents = bag_colors["shinygold"]
parents = set()
get_parents(shinygold_parents)

print(len(parents))

