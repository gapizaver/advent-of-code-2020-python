# Day 10: Adapter Array
# https://adventofcode.com/2020/day/9

# read the input
f = open("input.txt", "r")
adapters = list(map(int, f.read().splitlines()))
f.close()

jolts_max = max(adapters) 	# max output of adapter (in jolts)
difference1 = 0 			# difference of 1 (jolts) between two adapters
difference3 = 0 			# difference of 3 (jolts) between two adapters

last_i = 0 # value of i when last adapter was found

# search for adapters from 0 to jolts_max
for i in range(jolts_max + 1):
    if i in adapters:
        if i - last_i == 1:
            difference1 += 1
        elif i - last_i == 3:
            difference3 += 1

        last_i = i

# also count in your device which is always 3 jolts higher than jolts_max
difference3 += 1

print(difference1 * difference3) # result of the puzzle
