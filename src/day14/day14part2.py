# Day 14: Docking Data
# https://adventofcode.com/2020/day/14

from collections import defaultdict

# memory
# location : value
mem = defaultdict(str)


# write to memory
# mask aplies to location
# values X can be 0 or 1
def write_to_memory(memory, location, binary, mask):
    location_binary = ('{:0>' + str(len(mask)) + '}').format(dec_to_bin(location))
    possible_locations = [""]

    # apply mask and find all possible locations
    for i, digit in enumerate(mask):
        new_possible_locations = []

        if digit == "0":
            for possible_location in possible_locations:
                new_possible_locations.append(possible_location + location_binary[i])
        elif digit == "1":
            for possible_location in possible_locations:
                new_possible_locations.append(possible_location + "1")
        elif digit == "X":
            # every possible location now becomes 2 possible locations
            # by adding "0" or "1" to that location
            for possible_location in possible_locations:
                new_possible_locations.append(possible_location + "1")
                new_possible_locations.append(possible_location + "0")
        else:
            print("ERROR", mask)

        possible_locations = new_possible_locations

    for possible_location in possible_locations:
        memory[possible_location] = binary


# convert decimal to binary
def dec_to_bin(num):
    if num == 0:
        return "0"

    binary = ""
    while num > 0:
        binary = "{}{}".format(num % 2, binary)
        num //= 2
    return binary


# convert binary to decimal
def bin_to_dec(binary):
    dec = 0
    for i, digit in enumerate(binary[::-1]):
        dec += int(digit)*(2**i)
    return dec


# read input
f = open("input.txt", "r")
inpt = f.read().splitlines()

# mask - used for every writing to mem
mask = ""

# execute all instructions
for instruction in inpt:
    var = instruction.split(" = ")[0]
    value = instruction.split(" = ")[1]
    if var == "mask":
        mask = value
    else:
        mem_location = int(var[4:-1])
        write_to_memory(mem, mem_location, dec_to_bin(int(value)), mask)


# sum of values in mem
mem_sum = 0
for key, val in mem.items():
    mem_sum += bin_to_dec(val)

print(mem_sum)
