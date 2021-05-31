# Day 12: Rain Risk
# https://adventofcode.com/2020/day/12

from collections import defaultdict

# read the file
f = open("input.txt", "r")
txt = f.read().splitlines()
f.close()

# how much distance ship travelled in each of 4 directions:
# N, S, E, W
distance = defaultdict(int)
# ship starts facing east
ship_direction = "E"


# change direction of ship
# turning_direction: R (right) or L (left)
def change_ship_direction(current_direction, turning_direction, degrees):
    directions = []

    if turning_direction == "R":            # ship turning right
        directions = ["N", "E", "S", "W"]
    else:                                       # ship turning left
        directions = ["N", "W", "S", "E"]

    current_direction_index = directions.index(current_direction)
    # find new direction by moving through directions with step 90
    new_direction_index = (current_direction_index + int(degrees / 90)) % 4
    return directions[new_direction_index]


# loop through all ship movements
for instruction in txt:
    mnemonic = instruction[0]
    parameter = int(instruction[1:])

    # ship moves forward in direction it is facing
    if mnemonic == "F":
        distance[ship_direction] += parameter
    # ship moves north, south, east or west
    elif mnemonic == "N" or mnemonic == "S" or mnemonic == "E" or mnemonic == "W":
        distance[mnemonic] += parameter
    # ship changes pole it is facing
    elif mnemonic == "R" or mnemonic == "L":
        ship_direction = change_ship_direction(ship_direction, mnemonic, parameter)
    else:
        print("ERROR", instruction)

# calculate manhattan distance - result
manhattan_distance = \
    abs(distance["N"] - distance["S"]) \
    + abs(distance["W"] - distance["E"])

print(manhattan_distance)
