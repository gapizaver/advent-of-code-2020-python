# Day 12: Rain Risk
# https://adventofcode.com/2020/day/12

from collections import defaultdict

# read the file
f = open("input.txt", "r")
txt = f.read().splitlines()
f.close()

# waypoint position relative to the ship in each of 4 directions:
# N, S, E, W
waypoint_position = defaultdict(int)
# waypoint starts 10 units east and 1 unit north relative to the ship
waypoint_position["N"] = 1
waypoint_position["E"] = 10
waypoint_position["S"] = 0
waypoint_position["W"] = 0
# how much distance ship travelled in each of 4 directions:
# N, S, E, W
distance = defaultdict(int)


# rotate waypoint position
# turning_direction: R (right) or L (left)
def rotate_waypoint_position(current_waypoint_position, turning_direction, degrees):
    new_waypoint_position = current_waypoint_position

    for i in range(0, int(degrees/90)):
        # rotate right
        if turning_direction == "R":
            north = new_waypoint_position["N"]
            new_waypoint_position["N"] = new_waypoint_position["W"]
            new_waypoint_position["W"] = new_waypoint_position["S"]
            new_waypoint_position["S"] = new_waypoint_position["E"]
            new_waypoint_position["E"] = north
        else:  # rotate left
            north = new_waypoint_position["N"]
            new_waypoint_position["N"] = new_waypoint_position["E"]
            new_waypoint_position["E"] = new_waypoint_position["S"]
            new_waypoint_position["S"] = new_waypoint_position["W"]
            new_waypoint_position["W"] = north

    return new_waypoint_position


# loop through all ship movements
for instruction in txt:
    mnemonic = instruction[0]
    parameter = int(instruction[1:])

    # ship moves torwards waypoint
    if mnemonic == "F":
        for direction in waypoint_position.keys():
            distance[direction] += waypoint_position[direction] * parameter
    # waypoint moves north, south, east or west
    elif mnemonic == "N" or mnemonic == "S" or mnemonic == "E" or mnemonic == "W":
        waypoint_position[mnemonic] += parameter
    # ship changes pole it is facing
    elif mnemonic == "R" or mnemonic == "L":
        waypoint_position = rotate_waypoint_position(waypoint_position, mnemonic, parameter)
    else:
        print("ERROR", instruction)

# calculate manhattan distance - result
manhattan_distance = \
    abs(distance["N"] - distance["S"]) \
    + abs(distance["W"] - distance["E"])

print(manhattan_distance)
