#######################
# Stephen Boyett
# Advent of Code
# Day 10, Part 1
# 12/29/2020
########################

def main():
	with open("day10_input", "r") as f:
		nums = f.read().splitlines()

	nums = [int(_) for _ in nums]
	nums.sort()
	one_volt = 1
	three_volt = 1

	for i, v in enumerate(nums):
		if i == len(nums)-1:
			break
		print(f"v = {v}, nums[i+1] = {nums[i+1]}")
		if v+1 == nums[i+1]:
			one_volt += 1
			print(f"one_volt = {one_volt}")
		elif v+3 == nums[i+1]:
			three_volt += 1
			print(f"three_volt = {three_volt}")
	print(f"one_volt = {one_volt}")
	print(f"three_volt = {three_volt}")
	print(f"Answer is: {one_volt*three_volt}")

if __name__=="__main__":
	main()