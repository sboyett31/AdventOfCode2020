from itertools import combinations 

#################################
# Advent of Code - Day 1, part 2
# by Stephen Boyett
# 12/23/2020
#################################

with open("Day1_input", "r") as f:
	for c in combinations(f.read().splitlines(), 3):
		c = [int(_) for _ in c]
		if c[0]+c[1]+c[2] == 2020:
			print(f"Answer is: {c[0]*c[1]*c[2]}")
			break