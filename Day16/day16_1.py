#######################
# Stephen Boyett
# Advent of Code
# Day 16 Part 2
# 1/11/2021
########################
import re


def main():
	with open("day16_input", "r") as f:
		data = f.read().splitlines()
		nearby_tix = []
		nearby = False
		your = False
		for line in data:
			if "your" in line:
				nearby = False
				your = True
				continue
			if "nearby" in line:		
				nearby = True
				your = False
				continue
			if line:
				if nearby:
					nearby_tix.append(line)
				else:
					my_ticket = line

	invalid = []

	ranges = re.findall('(\d+)-(\d+)', data)  
	for t in nearby_tix:
		print(f"t is: {t}")
		nums = re.findall('\d+', t) 
		for n in nums:
			valid = False
			for r in ranges:
				if int(r[1]) >= int(n) >= int(r[0]):
					valid = True
			if not valid:
				invalid.append(n)

	print(f"Answer is: {sum([int(v) for v in invalid])}")

if __name__=="__main__":
	main()


