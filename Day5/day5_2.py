#######################
# Stephen Boyett
# Advent of Code
# Day 5, Part 2
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
	for ltr in p[7:10]:
		cols = cols[int(len(cols)/2):] if ltr == "R" else cols[:int(len(cols)/2)]
	seats.append(rows[0]*8 + cols[0])
seats.sort()
for i in range(len(seats)):
	if seats[i]+1 != seats[i+1]:
		print(seats[i]+1)
		break
