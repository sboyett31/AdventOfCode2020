##################
# Advent of Code
# Day 2, Part 2
# Stephen Boyett
# 10/24/2020
##################

valid = 0

with open("day2_input", "r") as f:
	lines = f.read().splitlines()

for line in lines:
	pos1 = int(line.split()[0].split("-")[0]) -1
	pos2 = int(line.split()[0].split("-")[1]) -1
	letter = line.split()[1].split(":")[0]
	word = line.split()[2]
	if word[pos1] == letter and word[pos2] != letter:
		valid += 1
	elif word[pos1] != letter and word[pos2] == letter:
		valid += 1

print(f"# of valid passwords: {valid}")
