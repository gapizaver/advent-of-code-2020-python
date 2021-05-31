# Day 13: Shuttle Search
# https://adventofcode.com/2020/day/13

# read input
f = open("input.txt", "r")
temp = f.read().splitlines()
current_timestamp = int(temp[0])
# each bus departs every x (bus id) timestamps:
buses = temp[1].split(",")

# find bus which departs first
# waiting time for the earliest departing bus
waiting_time = int(buses[0]) - current_timestamp % int(buses[0])
# id of the earliest departing bus
first_bus_id = int(buses[0])

for bus in buses:
    # if value unknown do nothing
    if bus != "x":
        # waiting time for this bus:
        bus_waiting_time = int(bus) - current_timestamp % int(bus)
        if bus_waiting_time < waiting_time:
            waiting_time = bus_waiting_time
            first_bus_id = int(bus)

# result of the puzzle
print(waiting_time * first_bus_id)
