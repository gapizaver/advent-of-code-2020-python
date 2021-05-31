# Day 14: Docking Data
# https://adventofcode.com/2020/day/14

from collections import defaultdict

# memory
# location : value
mem = defaultdict(str)


# write to memory
def write_to_memory(memory, location, binary, mask):
    # apply mask
    binary_with_mask = ""
    binary = binary[::-1]

    for i, digit in enumerate(mask[::-1]):
        if digit == "X":
            if i < len(binary):
                binary_with_mask += binary[i]
            else:
                binary_with_mask += "0"
        else:
            binary_with_mask += digit

    binary_with_mask = binary_with_mask[::-1]

    # write to mem
    memory[location] = binary_with_mask


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
