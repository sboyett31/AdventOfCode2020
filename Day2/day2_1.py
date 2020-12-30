##################
# Advent of Code
# Day 2, Part 1
# Stephen Boyett
# 10/24/2020
##################

valid = 0

with open("day2_input", "r") as f:
	lines = f.read().splitlines()

for line in lines:
	low = int(line.split()[0].split("-")[0])
	high = int(line.split()[0].split("-")[1])
	count = line.split(":")[1].count(line.split()[1].split(":")[0])
	if count >= low and count <= high:
		valid += 1

print(f"# of valid passwords: {valid}")
