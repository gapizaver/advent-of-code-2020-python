# Day 8: Handheld Halting
# https://adventofcode.com/2020/day/8

# read the input
f = open("input.txt", "r")
txt = f.read().splitlines()
f.close()


def run(instruction_set):
    executed = set() 		# numbers of instructions that have already been executed
    accumulator = 0		 	# data modified by instructions
    instruction_number = 0 	# number of executing instruction

    # execute instructions until the same instruction is executed twice
    while instruction_number not in executed and instruction_number != len(instruction_set):
        instruction = txt[instruction_number].split()
        mnemonic = instruction[0]
        operand = int(instruction[1])
        executed.add(instruction_number) # add instruction to already executed

        if mnemonic == "nop": 		# no operation
            instruction_number += 1
        elif mnemonic == "acc": 	# modify acc with operand
            accumulator += operand
            instruction_number += 1
        elif mnemonic == "jmp": 	# relative jump
            instruction_number += operand

        if instruction_number < 0 or instruction_number > len(instruction_set):
            return "error"

    # program terminated on the last instruction
    if instruction_number == len(instruction_set):
        return accumulator
    else:
        return "error"


# swap one "nop" and "jmp" to correct the instruction set
for i, instructon in enumerate(txt):
    instruction = txt[i].split()
    mnemonic = instruction[0]
    operand = instruction[1]
    # continue if mnemonic is "acc" (cannot change acc)
    if mnemonic == "acc":
        continue

    # swap mnemonics
    if mnemonic == "nop":
        txt[i] = "jmp " + operand
    else:
        txt[i] = "nop " + operand

    # try running:
    global result
    result = run(txt)
    if result != "error":
        break

    # swap back
    txt[i] = " ".join(instruction)


print(result)
