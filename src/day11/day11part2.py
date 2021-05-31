# Day 11: Seating System
# https://adventofcode.com/2020/day/11

# read the input
# grid of seats - consists of
# empty seat: 'L'
# occupied seat: '#'
# floor: '.'
f = open("input.txt", "r")
grid = f.read().splitlines()
f.close()


# if seat empty & no occupide seats seats adjacent to it -> occupy seat
# if seat occupied & >4 nearest seats in every 8 directions are occupied -> empty seat
def change_grid(old_grid):
    new_grid = []

    for i, row in enumerate(old_grid):
        new_row = ""
        for j, seat in enumerate(row):
            if seat == ".":  # floor - nothing to do
                new_row += "."
            else:
                # first seats in each of those eight directions
                # (up, down, left, right, up-left, up-right, down-left, down-right)
                first_seats_in_directions = ""

                # get those 8 seats in every directions:
                # up:
                if i > 0:
                    k = i - 1
                    while k > 0 and old_grid[k][j] == ".":
                        k -= 1
                    first_seats_in_directions += old_grid[k][j]

                # down:
                if i < len(old_grid) - 1:
                    k = i + 1
                    while k < len(old_grid) - 1 and old_grid[k][j] == ".":
                        k += 1
                    first_seats_in_directions += old_grid[k][j]

                # left:
                if j > 0:
                    k = j - 1
                    while k > 0 and old_grid[i][k] == ".":
                        k -= 1
                    first_seats_in_directions += old_grid[i][k]

                # right:
                if j < len(row) - 1:
                    k = j + 1
                    while k < len(row) - 1 and old_grid[i][k] == ".":
                        k += 1
                    first_seats_in_directions += old_grid[i][k]

                # up-left:
                # if already 4 occupied seats found, skip
                if first_seats_in_directions.count("#") < 5 and j > 0 and i > 0:
                    k_i = i - 1
                    k_j = j - 1
                    while k_i > 0 and k_j > 0 and old_grid[k_i][k_j] == ".":
                        k_i -= 1
                        k_j -= 1
                    first_seats_in_directions += old_grid[k_i][k_j]

                # up-right:
                if first_seats_in_directions.count("#") < 5 and j < len(row) - 1 and i > 0:
                    k_i = i - 1
                    k_j = j + 1
                    while k_i > 0 and k_j < len(row) - 1 and old_grid[k_i][k_j] == ".":
                        k_i -= 1
                        k_j += 1
                    first_seats_in_directions += old_grid[k_i][k_j]

                # down-left:
                if first_seats_in_directions.count("#") < 5 and j > 0 and i < len(old_grid) - 1:
                    k_i = i + 1
                    k_j = j - 1
                    while k_i < len(old_grid) - 1 and k_j > 0 and old_grid[k_i][k_j] == ".":
                        k_i += 1
                        k_j -= 1
                    first_seats_in_directions += old_grid[k_i][k_j]

                # down-right
                if first_seats_in_directions.count("#") < 5 and j < len(row) - 1 and i < len(old_grid) - 1:
                    k_i = i + 1
                    k_j = j + 1
                    while k_i < len(old_grid) - 1 and k_j < len(row) - 1 and old_grid[k_i][k_j] == ".":
                        k_i += 1
                        k_j += 1
                    first_seats_in_directions += old_grid[k_i][k_j]

                # occupy seat if necessary
                if seat == "L":
                    if first_seats_in_directions.count("#") == 0:
                        new_row += "#"
                    else:
                        new_row += "L"

                # empty seat if necessary
                if seat == "#":
                    if first_seats_in_directions.count("#") >= 5:
                        new_row += "L"
                    else:
                        new_row += "#"

        new_grid.append(new_row)

    return new_grid


# change grid until changing does not have any effect
while grid != change_grid(grid):
    grid = change_grid(grid)

# count occupied seats
occupied = 0
for row in grid:
    for seat in row:
        if seat == "#":
            occupied += 1

print(occupied)
