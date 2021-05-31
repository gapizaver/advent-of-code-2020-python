# Day 4: Passport Processing
# https://adventofcode.com/2020/day/4

f = open("input.txt", "r")
txt = f.read().splitlines()
f.close()

valid = 0 # number of valid passports
keys = 0  # number of key in passports

for line in txt:
    if line == "":
        if keys == 7:
            valid += 1
        keys = 0
        continue

    keys += line.count(":")
    keys -= line.count("cid:")

if keys == 7:
    valid += 1

print(valid)
