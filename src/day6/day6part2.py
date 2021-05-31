# Day 6: Custom Customs
# https://adventofcode.com/2020/day/6

f = open("input.txt", "r")
txt = f.read().splitlines()
f.close()

counts = 0 # counts of al groups
group_votes = set([char for char in txt[0]])  # same votes of a group

for i_line, line in enumerate(txt):
    # and of group votes, count them
    if line == "":
        counts += len(group_votes)
        group_votes = set([char for char in txt[i_line+1]])
        continue
	
	# add the same votes on current line to group_votes
    group_votes = group_votes.intersection([char for char in line]) 

counts += len(group_votes)

print(counts)
