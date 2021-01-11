#######################
# Stephen Boyett
# Advent of Code
# Day 11, Part 2
# 1/3/2021
########################

class seatingChart:

	def __init__(self, seats):
		self.rowlen = len(seats[0])
		self.num_rows = len(seats)
		self.seats = {(r, s): state for r, row in enumerate(seats) for s, state in enumerate(row) if state != "."}
		self.visible = {s: self.find_visible_seats(s) for s in self.seats.keys()}

	def find_adj_seats(self, seat):
		return [(r,s) for r in range(seat[0]-1, seat[0]+2) for s in range(seat[1]-1, seat[1]+2) 
				if (r,s) != seat and (r,s) in self.seats.keys()]

	def find_visible_seats(self, seat):
		lst = []
		(r, s) = seat
		while s >= 0:
			s -= 1
			if (r, s) in self.seats.keys():
				lst.append((r,s))
				break
		(r,s) = seat
		while s < self.rowlen:
			s += 1
			if (r, s) in self.seats.keys():
				lst.append((r,s))
				break
		(r,s) = seat
		while r >= 0:
			r -= 1
			if (r, s) in self.seats.keys():
				lst.append((r,s))
				break
		(r,s) = seat
		while r < self.num_rows:
			r += 1
			if (r, s) in self.seats.keys():
				lst.append((r,s))
				break
		(r,s) = seat
		while s >= 0 and r >= 0:
			s -= 1
			r -= 1
			if (r, s) in self.seats.keys():
				lst.append((r,s))
				break
		(r,s) = seat
		while s < self.rowlen and r < self.num_rows:
			s += 1
			r += 1
			if (r, s) in self.seats.keys():
				lst.append((r,s))
				break
		(r,s) = seat
		while s >= 0 and r < self.num_rows:
			s -= 1
			r += 1
			if (r, s) in self.seats.keys():
				lst.append((r,s))
				break
		(r,s) = seat
		while s < self.rowlen and r >= 0:
			s += 1
			r -= 1
			if (r, s) in self.seats.keys():
				lst.append((r,s))
				break
		return lst


	def occupied(self, seat):
		return (self.seats[seat] == "#")

	def crowded(self, seat):
		return (sum([1 for s in self.visible[seat] if self.occupied(s)]) >= 5)

	def spacious(self, seat):
		return (not any([1 for s in self.visible[seat] if self.occupied(s)]))

	def update(self):
		change_list = []
		for seat, state, in self.seats.items():
			if state == '#' and self.crowded(seat):
				change_list.append(seat)
			elif state == 'L' and self.spacious(seat):
				change_list.append(seat)
		for s in change_list:
			self.seats[s] = '#' if self.seats[s] == 'L' else 'L'

def main():
	with open("day11_input", "r") as f:
		seats = [[s for s in r] for r in f.read().splitlines()]

	prev = {}
	count = 0
	SC = seatingChart(seats)

	while(prev != SC.seats):
		count += 1
		prev = SC.seats.copy()
		SC.update()
	print(f"# of occupied seats: {list(SC.seats.values()).count('#')}")
	
if __name__=="__main__":
	main()
