# Day 1: Report Repair
# https://adventofcode.com/2020/day/1

f = open("input.txt", "r")
temp = f.read().splitlines()
f.close()

data = []
for num in temp:
    data.append(int(num))

result = 0
for num1 in data:
    for num2 in data:
        for num3 in data:
            if num1 != num2 and num1 != num3 and num1 + num2 + num3 == 2020:
                result = num1*num2*num3

    if result != 0:
        break

print(result)
