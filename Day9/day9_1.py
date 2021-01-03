#######################
# Stephen Boyett
# Advent of Code
# Day 9, Part 1
# 12/29/2020
########################

def main():
	with open("day9_input", "r") as f:
		nums = f.read().splitlines()

	nums = [int(_) for _ in nums]
	for i, v in enumerate(nums):
		found = False
		if i >= 25:
			vals = [_ for _ in nums[i-25:i] if _ < v]
			for j in range(len(vals)):
				for k in vals[j:]:
					if vals[j] + k == v and j != k:
						found = True
						break
				if found == True:
					break
			if found == False:
				print(f"Answer is: {v}")
				break


if __name__=="__main__":
	main()