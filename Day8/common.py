import time

class HandheldGame():
	def __init__(self, disk, prog=1):
		self.prog = prog
		self.disk = disk
		self.check = False
		self.reset()
		
	def reset(self):
		self.acc = 0
		self.pc = 0
		self.isntr = None
		self.executed_instructions = []
		self.read_disk(self.disk) 

	def read_disk(self, disk):
		with open(disk, "r") as f:
			self.instr_set = f.read().splitlines()

	def run(self):
		self.start_time = time.time()
		while not self.terminate():
			self.get_instruction()
			self.save_executed_instruction()
			self.execute_instruction()

	def execute_instruction(self):
		if self.check:
			print(f"Executing instruction: {self.instr}")
		if "nop" in self.instr:
			self.pc += 1
		elif "jmp -" in self.instr:
			self.pc -= int(self.instr[5:])
		elif "jmp +" in self.instr:
			self.pc += int(self.instr[5:])
		elif "acc -" in self.instr:
			self.acc -= int(self.instr[5:])
			self.pc += 1
		elif "acc +" in self.instr:
			self.acc += int(self.instr[5:])
			self.pc += 1

	def get_instruction(self):
		self.instr = self.instr_set[self.pc]

	def save_executed_instruction(self):
		self.executed_instructions.append(self.pc)

	def find_possible_issues(self):
		return [i for i, v in enumerate(self.instr_set) if "nop" in v or "jmp" in v]

	def swap_instruction(self, idx):
		if idx == 7:
			self.check = True
		if "nop" in self.instr_set[idx]:
			self.instr_set[idx] = self.instr_set[idx].replace("nop", "jmp")
		elif "jmp" in self.instr_set[idx]:
			print(f"swapping index {idx}")
			self.instr_set[idx] = self.instr_set[idx].replace("jmp", "nop")
		else:
			raise ValueError("Instruction can not currently be swapped.")
		print(f"self.instr_set = {self.instr_set}")

	def terminate(self):
		if self.prog == 1:
			if self.pc in self.executed_instructions:
				raise ValueError("Duplicate instruction Executed.")
		if self.prog == 2:
			if time.time() - self.start_time > 1:
				print(f"self.instr_set is: {self.instr_set}")
				raise TimeoutError("Timeout Error")
			return self.pc >= len(self.instr_set)
		raise ValueError("Unknown program running.")