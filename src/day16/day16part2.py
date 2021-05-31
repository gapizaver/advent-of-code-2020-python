#
# the algorithm does not work (yet)
#
# Day 16: Ticket Translation
# https://adventofcode.com/2020/day/16

from collections import defaultdict

# read input
f = open("input.txt", "r")
inpt = f.read().splitlines()

# datastructures for input
# legit 2 ranges of each field
fields = {}
type(fields)
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
        fields[field] = ranges
    elif reading == "your ticket":
        my_tickets += map(int, line.split(","))
    elif reading == "nearby tickets":
        nearby_tickets += map(int, line.split(","))

# discard invalid tickets
invalid_sum = 0
for i, ticket in enumerate(nearby_tickets):
    # assume its invalid (not invalid)
    invalid = ticket

    # try to prove opposite by iterating trough ticket_fields
    for field, ranges in fields.items():
        # check if ticket not inside ranges
        if (
                ranges[0] <= ticket <= ranges[1] or
                ranges[2] <= ticket <= ranges[3]
        ):
            invalid = 0
            break

    # remove if invalid:
    if invalid != 0:
        print(invalid)
        nearby_tickets.remove(invalid)


# define possible fields for ticket fields:
def is_in_range(ranges, ticket):
    return (
            ranges[0] <= ticket <= ranges[1] or
            ranges[2] <= ticket <= ranges[3]
    )


# possible "fields of ticket" for each field
#
possible_ticket_fields = {}

# check for every field
for field, ranges in fields.items():
    possible_fields = []
    # check all parts of tickets
    for i in range(len(fields.keys())):
        j = i
        possible = True
        # check every ticket in that part
        while j < len(nearby_tickets):
            if not is_in_range(ranges, nearby_tickets[j]):
                # if not in range this field is not possible
                possible = False
                break
            j += len(fields.keys())

        # if every ticket in the "ticket field" in range
        # add this field to possible fields
        if possible:
            possible_fields += [i]
    possible_ticket_fields[field] = possible_fields


# now figure out which field has which "ticket field"
"""
first attempt at this - unsuccessful - there are no 
fields with only one possible "ticket field" to begin with

used_ticket_fields = []
while len(used_ticket_fields) < len(fields.keys()):
    print(possible_ticket_fields)
    recently_used_ticket_fields = []

    # determine "ticket fields" to fields with only one possible "ticket field"
    for field, ticket_fields in possible_ticket_fields.items():
        if isinstance(ticket_fields, int):
            continue
        if len(ticket_fields) == 1:
            recently_used_ticket_fields.append(ticket_fields[0])
            possible_ticket_fields[field] = ticket_fields[0]

    # remove recently_used_ticket_fields from other possible_ticket_fields
    for field, ticket_fields in possible_ticket_fields.items():
        if isinstance(ticket_fields, int):
            continue
        for ticket_field in ticket_fields:
            if ticket_field in recently_used_ticket_fields:
                ticket_fields.remove(ticket_field)
        possible_ticket_fields[field] = ticket_fields

    # add recently_used_ticket_fields to used_ticket_fields
    used_ticket_fields += recently_used_ticket_fields


def find_fields_of_ticket_fields(possible_ticket_fields, searching_ticket_field):
    if not possible_ticket_fields:
        return []

    for field, ticket_fields in possible_ticket_fields.items():
        if searching_ticket_field < 6:
            print(searching_ticket_field, field)
        if searching_ticket_field in ticket_fields:
            new_possible_ticket_fields = possible_ticket_fields.copy()
            del new_possible_ticket_fields[field]

            new_fields_sequence = find_fields_of_ticket_fields(new_possible_ticket_fields, searching_ticket_field + 1)
            if len(new_fields_sequence) == len(possible_ticket_fields) - 1:
                return [field] + new_fields_sequence

    return []


# index represents "ticket fields"
fields = find_fields_of_ticket_fields(possible_ticket_fields, 0)
print(fields)
"""
print(possible_ticket_fields)
fields = {}

ticket_fields_count = defaultdict(int)
# find ticket field that appears only once
for field, ticket_fields in possible_ticket_fields.items():
    for ticket_field in ticket_fields:
        ticket_fields_count[ticket_field] += 1

print(ticket_fields_count)
