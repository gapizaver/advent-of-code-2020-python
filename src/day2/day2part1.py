# Day 2: Password Philosophy
# https://adventofcode.com/2020/day/2

f = open("input2.txt", "r")
temp = f.read().splitlines()
f.close()

valid = 0 # number of valid passwords

for line in temp:
    reps = line.split(": ")[0][:-1]
    minim = int(reps.split("-")[0]) # minimal number of reps of char in string
    maxim = int(reps.split("-")[1]) # maximal number of reps of char in string
    char = line.split(": ")[0][-1:] # character to search in string
    string = line.split(": ")[1]

    # indrement valid if reps of char in string between minim and maxim
    if minim <= string.count(char) <= maxim:
        valid += 1

print(valid)
