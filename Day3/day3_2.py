#######################
# Stephen Boyett
# Advent of Code
# Day 3, Part 2
# 10/24/2020
########################

def count_trees(data, x_slope, y_slope):
	line_count = 0
	for line in data:
		line_count += 1
	length = len(data[0])
	count = 0
	x_pos = 0
	y_pos = 0
	while y_pos < line_count:
		if data[y_pos][x_pos] == "#":
			count += 1
		x_pos += x_slope
		x_pos = x_pos - len(line) if x_pos >= len(line) else x_pos
		y_pos += y_slope
	return count

with open("day3_input", "r") as f:
	data = f.read().splitlines()


tree_count = 0
tree_count = count_trees(data, 1,1)
print(tree_count)
tree_count *= count_trees(data, 3,1)
print(tree_count)
tree_count *= count_trees(data, 5,1)
print(tree_count)
tree_count *= count_trees(data, 7,1)
print(tree_count)
tree_count *= count_trees(data, 1,2)
print(tree_count)

