# Day 5: Binary Boarding
# https://adventofcode.com/2020/day/5

f = open("input.txt", "r")
txt = f.read().splitlines()
f.close()

def get_seat_id(seat_positioning):
    lower = 0
    upper = 127

    # find row
    for instruction in seat_positioning[:7]:
        mid = int((upper - lower)/2) # middle
        if instruction == "B":
            lower += mid + 1
        else:
            upper = lower + mid

    row = min(lower, upper)

    # find column
    lower = 0
    upper = 7

    for instruction in seat_positioning[-3:]:
        mid = int((upper - lower)/2) # middle
        if instruction == "R":
            lower += mid + 1
        else:
            upper = lower + mid

    column = min(lower, upper)

    return row * 8 + column


# find the highest id
highest_id = 0
for line in txt:
    print(line)
    print(get_seat_id(line))
    if get_seat_id(line) > highest_id:
        highest_id = get_seat_id(line)

print(highest_id)
