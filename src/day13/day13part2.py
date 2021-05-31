# Day 13: Shuttle Search
# https://adventofcode.com/2020/day/13

import math

# read the input
f = open("input.txt", "r")
temp = f.read().splitlines()
# each bus departs every x (bus id) timestamps:
buses = temp[1].split(",")

first_id = int(buses[0])
buses = buses[1:]
first_timestamp = first_id  # when bus departs
departures = []  # departures of buses
earliest_next_departure = first_timestamp + first_id

# find first_timestamp after which all buses depart
# one after another
result_timestamp = -1
while result_timestamp == -1:
    timestamp = first_timestamp + 1
    for bus in buses:
        # bus x can start every timestamp
        if bus != "x":
            # check if the bus can start at that timestamp
            if timestamp % int(bus) != 0:
                break

        # add bus departure
        departures.append(timestamp)
        # next bus must start next minut
        timestamp += 1

    # if all buses has departed, that's it!
    if len(departures) == len(buses):
        result_timestamp = first_timestamp
    else:
        first_timestamp += first_id
        departures = []
        # print(first_timestamp)


# result
print(result_timestamp)
