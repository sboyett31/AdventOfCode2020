#########################
# Advent of Code - Day 1
# by Stephen Boyett
# 12/23/2020
#########################

with open("Day1_pt1_input", "r") as inFile:
	data = [int(_) for _ in inFile.read().splitlines()]
ans = 0
idx = 0
while idx < len(data):
	for i in range(idx, len(data)):
		if data[idx] + data[i] == 2020:
			ans = data[idx] * data[i]		
	idx+=1
	if ans > 0:
		break
print(f"answer is: {ans}")


