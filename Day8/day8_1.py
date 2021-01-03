#######################
# Stephen Boyett
# Advent of Code
# Day 8, Part 1
# 12/29/2020
########################

from common import HandheldGame

def main():
	kids_dumb_game = HandheldGame(disk="day8_input")
	try:
		kids_dumb_game.run()
	except ValueError as e:
		print(f"Error is: {e}")

	print(f"Answer is: {kids_dumb_game.acc}")

if __name__=="__main__":
	main()