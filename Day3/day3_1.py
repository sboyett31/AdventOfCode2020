#######################
# Stephen Boyett
# Advent of Code
# Day 3, Part 1
# 10/24/2020
########################

with open("day3_input", "r") as f:
	lines = f.read().splitlines()

x_pos = 0
tree_count = 0

for line in lines:
	x_pos = x_pos - len(line) if x_pos >= len(line) else x_pos
	if line[x_pos] == "#":
		tree_count += 1
	x_pos += 3

print(f"Tree count is: {tree_count}")