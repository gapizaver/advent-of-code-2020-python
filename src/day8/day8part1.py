# Day 8: Handheld Halting
# https://adventofcode.com/2020/day/8

# read the input
f = open("input.txt", "r")
txt = f.read().splitlines()
f.close()

executed = set() 		# numbers of instructions that have already been executed
accumulator = 0 		# data modified by instructions
instruction_number = 0	# number of executing instruction

# execute instructions until the same instruction is executed twice
while instruction_number not in executed:
    instruction = txt[instruction_number].split()
    mnemonic = instruction[0]
    operand = int(instruction[1])
    executed.add(instruction_number) # add instruction to already executed

    if mnemonic == "nop": 			# no operation
        instruction_number += 1
    elif mnemonic == "acc": 		# modify acc with operand
        accumulator += operand
        instruction_number += 1
    elif mnemonic == "jmp": 		# relative jump
        instruction_number += operand

print(accumulator)
