#######################
# Stephen Boyett
# Advent of Code
# Day 7, Part 2
# 12/25/2020
########################

import re 

def get_rules(rules):
	"""
	Splits rules into a dictionary with the format:
	{bag: {contained_bag: quantity, contained_bag: quantity}}
	"""
	rules_dict = {}
	for rule in rules:
		bag = " ".join(rule.split()[:2])
		rules_dict[bag] = {}
		results = re.findall('([\d/]+) ([\S]+ [\S]+) bag', rule)
		for result in results:
			rules_dict[bag][result[1]] = result[0] 
	return rules_dict

def count_bags(rules, bag, multiplier, count, bag_list):
	multiplier = int(count)*multiplier
	for next_bag, count in rules[bag].items():
		bag_list.append(int(count)*int(multiplier))
		count_bags(rules, next_bag, multiplier, count, bag_list)
	multiplier = 1
	return sum(bag_list)


def main():
	with open("day7_input", "r") as f:
		rules = get_rules(f.read().splitlines())

	num_bags = count_bags(rules, "shiny gold", 1, 1, [])
	print(num_bags)

if __name__=="__main__":
	main()