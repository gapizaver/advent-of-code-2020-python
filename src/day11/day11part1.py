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
# if seat occupied & >3 more seats adjacent to it occupied -> empty seat
def change_grid(old_grid):
    new_grid = []

    for i, row in enumerate(old_grid):
        new_row = ""
        for j, seat in enumerate(row):
            if seat == ".":  # floor - nothing to do
                new_row += "."
            else:
                # number of occupied neighboring seats
                occupied_neighbours = 0

                # check all 8 neighbouring seats:
                # check current row:
                if j > 0 and row[j - 1] == "#":  # previous seat
                    occupied_neighbours += 1
                if j < len(row) - 1 and row[j + 1] == "#":  # next seat
                    occupied_neighbours += 1
                # check previous row
                if i > 0:
                    if old_grid[i - 1][j] == "#":
                        occupied_neighbours += 1
                    if j > 0 and old_grid[i - 1][j - 1] == "#":
                        occupied_neighbours += 1
                    if j < len(old_grid[i - 1]) - 1 and old_grid[i - 1][j + 1] == "#":
                        occupied_neighbours += 1
                # check next row
                if i < len(old_grid) - 1:
                    if old_grid[i + 1][j] == "#":
                        occupied_neighbours += 1
                    if j > 0 and old_grid[i + 1][j - 1] == "#":
                        occupied_neighbours += 1
                    if j < len(old_grid[i + 1]) - 1 and old_grid[i + 1][j + 1] == "#":
                        occupied_neighbours += 1

                # occupy seat if necessary
                if seat == "L":
                    if occupied_neighbours == 0:
                        new_row += "#"
                    else:
                        new_row += "L"
                # empty seat if necessary
                if seat == "#":
                    if occupied_neighbours >= 4:
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
