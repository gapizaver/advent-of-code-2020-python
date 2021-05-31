# Day 2: Password Philosophy
# https://adventofcode.com/2020/day/2

f = open("input2.txt", "r")
temp = f.read().splitlines()
f.close()

valid = 0 # number of valid passwords

for line in temp:
    reps = line.split(": ")[0][:-1]
    pos1 = int(reps.split("-")[0]) 	# position 1 of char
    pos2 = int(reps.split("-")[1]) 	# position 2 of char
    char = line.split(": ")[0][-1:] # character in string that should be in pos1 xor pos2
    string = line.split(": ")[1]

    # indrement valid if reps of char in string in pos1 xor pos2
    if (string[pos1 - 1] == char) ^ (string[pos2 - 1] == char):
        valid += 1

print(valid)
