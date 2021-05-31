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
        if num1 != num2 and num1 + num2 == 2020:
            result = num1*num2

    if result != 0:
        break

print(result)
