# Day 6: Custom Customs
# https://adventofcode.com/2020/day/6

f = open("input.txt", "r")
txt = f.read().splitlines()
f.close()

counts = 0 				# counts of al groups
group_votes = set()  	# different votes of a group

for line in txt:
    # and of group votes, count them
    if line == "":
        counts += len(group_votes)
        group_votes = set()
        continue
	
	# add votes on current line to group_votes
    group_votes = group_votes.union([char for char in line]) 

counts += len(group_votes)

print(counts)
