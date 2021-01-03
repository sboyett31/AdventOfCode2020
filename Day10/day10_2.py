################################################
# Stephen Boyett
# Advent of Code
# Day 10, Part 2
# 12/29/2020
# I am really happy with this solution I came up
# with using graph theory + dynamic programming
#################################################

import time

class adapterDAG:

	def __init__(self, joltages):
		self.adj = {k: [] for k in joltages}
		self.paths = {k: 0 for k in joltages}
		self.joltages = joltages
		self.start = [i for i in [1,2,3] if i in self.joltages]
		self.end = max(joltages)
		self.combinations = 0

	def add_edge(self, src, dst):
		self.adj[src].append(dst)

	def fill_adj_mtrx(self):
		for i, j in enumerate(self.joltages):
			sub_arr = self.joltages[i+1:i+4]
			for v in sub_arr:
				if v <= j+3:
					self.add_edge(j, v)

	def fill_paths_mtrx(self):
		"""
		Keeps track of the number of possible paths to the
		end from each node, starting at the end.
		"""
		self.paths[self.end] = 1
		for j in reversed(self.joltages[:len(self.joltages)-1]):
			self.paths[j] = sum([self.paths[i] for i in self.adj[j]])

	def count_possible_combinations(self):
		for s in self.start:
			self.combinations += self.paths[s]
		print(f"# of possible combinations: {self.combinations}")


def main():
	with open("day10_input", "r") as f:
		joltages = [int(_) for _ in f.read().splitlines()]

	joltages.sort()
	G = adapterDAG(joltages)
	G.fill_adj_mtrx()
	G.fill_paths_mtrx()
	G.count_possible_combinations()

if __name__=="__main__":
	start = time.time()
	main()
	print(f"Execution time: {time.time() - start}s")