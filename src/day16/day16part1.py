# Day 16: Ticket Translation
# https://adventofcode.com/2020/day/16

# read input
f = open("input.txt", "r")
inpt = f.read().splitlines()

# datastructures for input
# legit 2 ranges of each field
ticket_fields = {}
type(ticket_fields)
# my tickets
my_tickets = []
# other tickets
nearby_tickets = []

# fill datastructures with input
reading = "ticket fields"
for line in inpt:
    if line == "":
        continue

    line_splitted = line.split(":")
    if line_splitted[0] == "your ticket" or line_splitted[0] == "nearby tickets":
        reading = line_splitted[0]
        continue

    if reading == "ticket fields":
        # field of tickets
        field = line_splitted[0]
        range1 = line_splitted[1].split(" or ")[0]
        range2 = line_splitted[1].split(" or ")[1]
        # for each field two ranges of tickets stored in list:
        # [range1min, range1max, range2min, range2max]
        ranges = [int(range1.split("-")[0]), int(range1.split("-")[1]),
                  int(range2.split("-")[0]), int(range2.split("-")[1])]
        ticket_fields[field] = ranges
    elif reading == "your ticket":
        my_tickets += map(int, line.split(","))
    elif reading == "nearby tickets":
        nearby_tickets += map(int, line.split(","))

# count invalid tickets
invalid_sum = 0
for ticket in nearby_tickets:
    # assume its invalid (not invalid)
    invalid = ticket

    # try to prove opposite by iterating trough ticket_fields
    for field, ranges in ticket_fields.items():
        # check if ticket not inside ranges
        if (
                ranges[0] <= ticket <= ranges[1] or
                ranges[2] <= ticket <= ranges[3]
        ):
            invalid = 0
            break

    invalid_sum += invalid

print(invalid_sum)
