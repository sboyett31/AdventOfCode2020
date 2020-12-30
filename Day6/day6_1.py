#######################
# Stephen Boyett
# Advent of Code
# Day 6, Part 1
# 12/25/2020
########################

with open("day6_input", "r") as f:
	groups = f.read().split("\n\n")
print(len([v for v in range(97, 123) for group in groups if chr(v) in group]))
