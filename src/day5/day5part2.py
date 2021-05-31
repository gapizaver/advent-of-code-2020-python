# Day 5: Binary Boarding
# https://adventofcode.com/2020/day/5

f = open("input.txt", "r")
txt = f.read().splitlines()
f.close()

# rows and columns of (empty=0, full=1) seats
seats = [[0]*8 for _ in range(128)]


def fill_seat(seat_positioning):
    lower = 0
    upper = 127

    # find row
    for instruction in seat_positioning[:7]:
        mid = int((upper - lower)/2) #middle
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

    # take the seat
    seats[row][column] = 1

# fill seats
for line in txt:
    fill_seat(line)

# find empty seat
empty_row = 0
empty_column = 0
current = 0
was_seat = False # one seat before was empty
for count_row, row in enumerate(seats):
    for count_seat, seat in enumerate(row):
        # if seat is empty and neighbor seats are taken
        if seat == 0 and row[count_seat - 1] == 1 and row[count_seat + 1] == 1:
            empty_column = count_seat
            break

    if empty_column != 0:
        empty_row = count_row
        break

print(empty_row * 8 + empty_column)
