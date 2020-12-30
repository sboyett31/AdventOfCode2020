#######################
# Stephen Boyett
# Advent of Code
# Day 8, Part 1
# 12/29/2020
########################




def main():
	with open("day7_input", "r") as f:
		rules = get_rules(f.read().splitlines())#######################
# Stephen Boyett
# Advent of Code
# Day 7, Part 2
# 12/25/2020
########################

import re 

class HandheldGame():
	def __init__(self):
		self.acc = None
		self.pc = 0
		self.executed_instr = []

	def execute_instruction(self):
		if self.pc in self.executed_instr:
			raise ValueError("Instruction already executed.")
		else:
			self.get_instuction()

		if "nop" in self.instr:
			pass
		elif "jmp -" in self.instr:
			self.pc -= int(self.instr[5])
		elif "jmp +" in self.instr:
			self.pc += int(self.instr[5])
		elif "acc" in self.instr:
			self.acc += int(self.instr[5])
			self.pc += 1

	def get_instruction(self):
		return self.instr_set[self.pc]


def main():
	with open("day7_input", "r") as f:
		instruction_list = f.read().splitlines()

	kids_dumb_game = HandheldGame()

	for i in instruction_list:
		try:
			kids_dumb_game.execute_instruction()
		except ValueError as e:
			print(f"Error is: {e}")

	print(f"Answer is: {kids_dumb_game.acc}")

	

if __name__=="__main__":
	main()