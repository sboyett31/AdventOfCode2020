#######################
# Stephen Boyett
# Advent of Code
# Day 7, Part 1
# 12/25/2020
########################
count = 0
def get_carrier_bags(rules, bags):
	rc = []
	for bag in bags:
		rc += [" ".join(rule.split()[:2]) for rule in rules if bag in rule and not rule.startswith(bag)]
	return rc

with open("day7_input", "r") as f:
	rules = f.read().splitlines()

bags = ["shiny gold"]
carrier_bags = list(set(get_carrier_bags(rules, bags)))
while len(carrier_bags) != len(bags):
	bags = carrier_bags.copy()
	carrier_bags += get_carrier_bags(rules, bags)
	carrier_bags = list(set(carrier_bags))

print(len(carrier_bags))