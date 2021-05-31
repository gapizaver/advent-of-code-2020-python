# Day 10: Adapter Array
# https://adventofcode.com/2020/day/9

# read the input
f = open("input.txt", "r")
adapters = list(map(int, f.read().splitlines()))
f.close()

adapters.sort()
adapters = [0] + adapters
# adapters weight is sum of weights of previous adapters
# with jolts greater than adapters - 4
adapters_weights = [1, 1, 0]

if adapters[2] - adapters[0] <= 3:
    adapters_weights[2] += 1
if adapters[2] - adapters[1] <= 3:
    adapters_weights[2] += 1

for i in range(3, len(adapters)):
    # add weight for this adapter
    adapters_weights.append(0)

    # check 3 previous adapters:
    # if weights of previous - current <= 3:
    # add weight of previous to current
    for j in range(1, 4):
        if adapters[i] - adapters[i - j] <= 3:
            adapters_weights[i] += adapters_weights[i - j]


print(adapters_weights[-1])
