#######################
# Stephen Boyett
# Advent of Code
# Day 14 Part 2
# 1/10/2021
########################



def main():
	with open("day14_input", "r") as f:
		data = f.read().splitlines()


	mem = {}
	instr_set = data
	for inst in instr_set:
		if inst.startswith("mask"):
			mask = [v for v in inst.split(" ")[2]]
		else:
			flt_bits = []
			addr = [v for v in format(int(inst.split("[")[1].split("]")[0]), 'b').zfill(len(mask))]
			for i in range(len(mask)):
				if mask[i] == '1':
					addr[i] = '1'
				elif mask[i] == 'X':
					flt_bits.append(i)
			for i in range(2**len(flt_bits)):
				vals = [v for v in format(i, 'b').zfill(len(flt_bits))]
				for ii in range(len(vals)):
					addr[flt_bits[ii]] = vals[ii]
				int_addr = int("".join(addr), base=2)
				mem[int_addr] = int(inst.split(" ")[2])

	print(f"Answer is: {sum([v for v in mem.values()])}")


if __name__=="__main__":
	main()

 
