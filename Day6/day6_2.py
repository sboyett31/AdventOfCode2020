#######################
# Stephen Boyett
# Advent of Code
# Day 6, Part 2
# 12/25/2020
########################

with open("day6_input", "r") as f:
	groups = f.read().split("\n\n")
count = 0
for group in groups:
	people = group.splitlines()
	for v in range(97, 123):
		if all(chr(v) in person for person in people):
			count += 1

print(count)

