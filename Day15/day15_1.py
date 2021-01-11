#######################
# Stephen Boyett
# Advent of Code
# Day 15 Part 1
# 1/11/2021
########################



def main():
	with open("day15_input", "r") as f:
		data = f.read().split(',')

	nums = {}

	turn = 1
	for num in data:
		nums[int(num)] = turn
		turn += 1

	print(nums)
	num = 0
	while turn <= 30000000:
		print(f"turn is: {turn}")
		if nums.get(num) is None:
			next_num = 0
		else:
			next_num = turn - nums[num]
		nums[num] = turn
		turn+=1
		if turn != 30000001:
			num = next_num
	print(nums)
	print(num)



if __name__=="__main__":
	main()

 
