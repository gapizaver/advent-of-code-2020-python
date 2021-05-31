# Day 4: Passport Processing
# https://adventofcode.com/2020/day/4

f = open("input.txt", "r")
txt = f.read().splitlines()
f.close()

valid_pass = 0 # number of valid passports
valid_keys = 0 # number of valid keys in passports

for line in txt:
    if line == "":
        if valid_keys == 7:
            valid_pass += 1
        valid_keys = 0
        continue

    fields = line.split()
    for field in fields:
        key = field.split(":")[0]   # key
        val = field.split(":")[1]   # value

        # check if value is valid for different keys
        if key == "byr":
            if len(val) == 4 and 1920 <= int(val) <= 2002:
                valid_keys += 1
        elif key == "iyr":
            if len(val) == 4 and 2010 <= int(val) <= 2020:
                valid_keys += 1
        elif key == "eyr":
            if len(val) == 4 and 2020 <= int(val) <= 2030:
                valid_keys += 1
        elif key == "hgt":
            if val[-2:] == "cm":
                if 150 <= int(val[:-2]) <= 193:
                    valid_keys += 1
            elif val[-2:] == "in":
                if 59 <= int(val[:-2]) <= 76:
                    valid_keys += 1
        elif key == "hcl":
            # create list of 0-9 + a-f
            valid_chars = [str(i) for i in range(0, 10)] + [(chr(ord('a')+i)) for i in range(6)]
            # check if first char is # and rest are 0-9 or a-f
            if val[0] == "#" and False not in [c in valid_chars for c in val[1:]]:
                valid_keys += 1
        elif key == "ecl":
            if val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                valid_keys += 1
        elif key == "pid":
            if val.isnumeric() and len(val) == 9:
                valid_keys += 1


if valid_keys == 7:
    valid_pass += 1

print(valid_pass)
