#######################
# Stephen Boyett
# Advent of Code
# Day 4, Part 1
# 10/24/2020
########################

valid = 0
fields = ["ecl:", "pid:", "eyr:", "hcl:", "byr:", "iyr:", "hgt:"]

with open("day4_input", "r") as f:
	cards = f.read().split("\n\n")

for card in card:
	if any(field not in card for field in fields):
		continue
	
	valid += 1

print(valid)