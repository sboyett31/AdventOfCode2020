#######################
# Stephen Boyett
# Advent of Code
# Day 13 Part 2
# 1/3/2021
# Chinese remainder theorem
########################
import time

class Bus:

	def __init__(self, t, offset):
		self.route_time = int(t)
		self.offset = offset

	def is_bus_departing(self, time):
		return (time % self.route_time == 0)

def main():
	with open("day13_input", "r") as f:
		data = f.read().splitlines()
	buses = [Bus(t, offset) for offset, t in enumerate(data[1].split(',')) if t != 'x']
	t = abs(int(data[0]) % buses[0].route_time - buses[0].route_time) + int(data[0])

	while True:
		if not buses[1].is_bus_departing(t+buses[1].offset):
			t += buses[0].route_time
			continue
		break
	print(f"starting t is: {t}")
	inc = 17
	found = False
	print(buses)
	while not found:
		found = True
		for bus in buses:
			if not bus.is_bus_departing(t+bus.offset):
				found = False
				break
			elif bus.is_bus_departing(t+bus.offset) and t != 986:
				buses.remove(bus)
				print(f"inc is: {inc}")
				inc = t - 986
				if len(buses) > 0:
					found = False
		if found:
			break
		t += inc
		# print(f"t is: {t}")
	print(f"Solution is: {t}")


if __name__=="__main__":
	start = time.time()
	main()
	print(f"Execution time: {time.time() - start}")
	print(f"2000xtime : {(time.time()-start)*2000}")