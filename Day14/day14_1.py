#######################
# Stephen Boyett
# Advent of Code
# Day 14 Part 1
# 1/10/2021
########################



def main():
	with open("day14_input", "r") as f:
		data = f.read().splitlines()


	mem = {}
	instr_set = data
	for inst in instr_set:
		print(f"isnt is: {inst}")
		if inst.startswith("mask"):
			mask = [v for v in inst.split(" ")[2]]
		else:
			val = [v for v in format(int(inst.split(' ')[2]), 'b').zfill(len(mask))]
			for i in range(len(mask)):
				print(f"i is: {i}")
				val[i] = mask[i] if mask[i] != "X" else val[i]
			val = "".join(val)
			print(f"val is: {val}")
			print(f"int_val is: {int(val, base=2)}")
			mem[inst.split("[")[1].split("]")[0]] = int(val, base=2)

	print(mem)
	print(f"Answer is: {sum([v for v in mem.values()])}")


if __name__=="__main__":
	main()

 
