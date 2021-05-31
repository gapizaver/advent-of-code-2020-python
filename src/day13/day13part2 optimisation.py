# Day 13: Shuttle Search
# https://adventofcode.com/2020/day/13

# first try would take too long for large inputs
# (works on smaller tests)
# here I try to optimise the algorithm

# read input
f = open("input.txt", "r")
temp = f.read().splitlines()

# each bus departs every x (bus id) timestamps:
buses = temp[1].split(",")
# timestamps apart from the first bus departure
timestamp_apart = 1
# step at which to look for new timestamp
step = int(buses[0])
# start at first departure of the first bus
start = int(buses[0])

# search for timestamp after which all buses depart
# one after another, one timestamp apart
for bus in buses[1:]:
    # bus x can start any timestamp - do nothing
    if bus != "x":
        # find first possible departure of the bus
        i = start
        while (i + timestamp_apart) % int(bus) != 0:
            i += step
        first_departure = i

        # find second possible departure of the bus
        i += step
        while (i + timestamp_apart) % int(bus) != 0:
            i += step
        second_departure = i

        # step at which to search for departures of the next bus
        step = second_departure - first_departure
        # start searching at first departure
        start = first_departure

    # timestamps apart from the first bus departure++
    timestamp_apart += 1

print(first_departure)
