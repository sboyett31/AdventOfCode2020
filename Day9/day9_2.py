#######################
# Stephen Boyett
# Advent of Code
# Day 9, Part 2
# 12/29/2020
########################

def main():
	with open("day9_input", "r") as f:
		nums = f.read().splitlines()
	Found = False
	target = 15353384
	nums = [int(_) for _ in nums]
	for i, v in enumerate(nums):
		acc = [v]
		for j in nums[i+1:]:
			acc.append(j)
			if sum(acc) == target:
				Found = True
				break
			elif sum(acc) > target:
				break
		if Found:
			break
	ans = max(acc) + min(acc)
	print(f"Answer is: {ans}")






if __name__=="__main__":
	main()