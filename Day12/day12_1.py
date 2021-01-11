#######################
# Stephen Boyett
# Advent of Code
# Day 12, Part 1
# 1/3/2021
########################

class ship:

	def __init__(self):
		self.dir = 90
		self.x = 0
		self.y = 0
		self.dirdict = {0: "N", 90: "E", 180: "S", 270: "W"}

	def autopilot(self, instr_set):
		for i in instr_set:
			self.move(i)

	def move(self, instr):
		if instr[:1] == "E":
			self.x += int(instr[1:])
		elif instr[:1] == "N":
			self.y += int(instr[1:])
		elif instr[:1] == "W":
			self.x -= int(instr[1:])
		elif instr[:1] == "S":
			self.y -= int(instr[1:])
		elif instr[:1] == "R":
			self.dir += int(instr[1:])
			self.dir = self.dir % 360
		elif instr[:1] == "L":
			self.dir-= int(instr[1:])
			self.dir = self.dir % 360
		elif instr[:1] == "F":
			self.move(instr.replace("F", self.dirdict[self.dir]))


def main():
	with open("day12_input", "r") as f:
		instr = f.read().splitlines()

	boat = ship()
	boat.autopilot(instr)
	print((boat.x, boat.y))
	print(f"Manhattan distance is {abs(boat.x)+abs(boat.y)}")

if __name__=="__main__":
	main()
