#######################
# Stephen Boyett
# Advent of Code
# Day 12, Part 2
# 1/3/2021
########################


class ship:

	def __init__(self):
		self.x = 0
		self.y = 0
		self.wpy = 1
		self.wpx = 10
		self.dir = 90
		self.wp_quad = 0

	def autopilot(self, instr_set):
		for i in instr_set:
			print(f"Instruction is: {i}")
			if "F" in i:
				self.x += self.wpx*int(i[1:])
				self.y += self.wpy*int(i[1:])
			elif "R" in i or "L" in i:
				self.rotate_waypoint(i)
			else:
				self.move_waypoint(i)
			print(f"self.waypoint = ({self.wpx}, {self.wpy})")

	def rotate_waypoint(self, instr):
		rotations = int(float(instr[1:])/360/.25)
		self.wp_quad = (self.wp_quad + rotations) % 3
		if "R" in instr:
			for _ in range(rotations):
				tx = self.wpx
				self.wpx = self.wpy
				self.wpy = -tx
		elif "L" in instr:
			for _ in range(rotations):
				tx = self.wpx
				self.wpx = -self.wpy
				self.wpy = tx

	def move_waypoint(self, instr):
		if instr[:1] == "N":
			self.wpy += int(instr[1:])
		elif instr[:1] == "E":
			self.wpx += int(instr[1:])
		elif instr[:1] == "W":
			self.wpx -= int(instr[1:])
		elif instr[:1] == "S":
			self.wpy -= int(instr[1:])			



def main():
	with open("day12_input", "r") as f:
		instr = f.read().splitlines()

	boat = ship()
	boat.autopilot(instr)
	print((boat.x, boat.y))
	print(f"Manhattan distance is {abs(boat.x)+abs(boat.y)}")

if __name__=="__main__":
	main()
