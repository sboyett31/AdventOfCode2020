#######################
# Stephen Boyett
# Advent of Code
# Day 8, Part 2
# 12/29/2020
########################

from common import HandheldGame

def main():
	kids_dumb_game = HandheldGame(disk="day8_input", prog=2)


	problem_indices = kids_dumb_game.find_possible_issues()
	print(f"problems is: {problem_indices}")
	for i in problem_indices:
		try:
			kids_dumb_game.swap_instruction(i)
			kids_dumb_game.run()
		except TimeoutError as e:
			kids_dumb_game.reset()

	print(f"Answer is: {kids_dumb_game.acc}")

if __name__ == "__main__":
	main()