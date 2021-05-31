# Day 7: Handy Haversacks
# https://adventofcode.com/2020/day/7

from collections import defaultdict


# count all the children bags of parent bag
# recursion - count all children + count all children of children..
def count_all_children(children, parents):
    bags_of_parent = 0

    for bag in children:
        bags = bag[1] * parents # how many bags this parent contains
        if bag[0] in bag_colors.keys():
            bags_of_parent += bags + count_all_children(bag_colors[bag[0]], bags)
        else:
            bags_of_parent += bags

    return bags_of_parent

# read the input
f = open("input.txt", "r")
txt = f.read().splitlines()
f.close()

# dictionary of all bag colors and their children + how many of them they can carry
# dict - color: [children]
# children - (list)[color, how many parent can carry]
bag_colors = defaultdict(list)

# fill the dictionary
for line in txt:
    words = line.split()
    if words[4] == "no":
        continue

    parent_color = words[0] + words[1]
    for i in range(5, len(words), 4):
        color = words[i] + words[i + 1]
        number_of_bags = int(words[i - 1])
        bag_colors[parent_color].append([color, number_of_bags])

# count all childre of shiny gold color
shinygold_children = bag_colors["shinygold"]
counter = count_all_children(shinygold_children, 1)

print(counter)
