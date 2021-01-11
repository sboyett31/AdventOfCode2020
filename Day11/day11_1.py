#######################
# Stephen Boyett
# Advent of Code
# Day 11, Part 1
# 1/3/2021
########################

class seatingChart:

	def __init__(self, seats):
		self.seats = {(r, s): state for r, row in enumerate(seats) for s, state in enumerate(row)}
		self.adj = {s: self.find_adj_seats(s) for s in self.seats.keys()}

	def find_adj_seats(self, seat):
		return [(r,s) for r in range(seat[0]-1, seat[0]+2) for s in range(seat[1]-1, seat[1]+2) 
				if (r,s) != seat and (r,s) in self.seats.keys()]

	def occupied(self, seat):
		return (self.seats[seat] == "#")

	def crowded(self, seat):
		return (sum([1 for s in self.adj[seat] if self.occupied(s)]) >= 4)

	def spacious(self, seat):
		return (not any([1 for s in self.adj[seat] if self.occupied(s)]))

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
