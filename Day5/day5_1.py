#######################
# Stephen Boyett
# Advent of Code
# Day 5, Part 1
# 10/24/2020
########################

with open("day5_input", "r") as f:
	passes = f.readlines()
seats = []
for p in passes:
	rows = list(range(128))
	cols = list(range(8))
	for ltr in p[:7]:
		rows = rows[int(len(rows)/2):] if ltr == "B" else rows[:int(len(rows)/2)]
	for ltr in p[8:]:
		cols = cols[int(len(cols)/2):] if ltr == "R" else cols[:int(len(cols)/2)]
	seats.append(rows[0]*8 + cols[0])
print(max(seats))
