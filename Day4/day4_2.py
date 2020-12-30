#######################
# Stephen Boyett
# Advent of Code
# Day 4, Part 2
# 10/24/2020
########################

def validate_ecl(v):
	return v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def validate_pid(v):
	return len(v) == 9

def validate_eyr(v):
	return int(v) >= 2020 and int(v) <= 2030

def validate_hcl(v):
	if not v.startswith("#"):
		return False
	for letter in v[1:]:
		print(f"letter is: {letter}")
		if not(48 <= ord(letter) <= 57 or 97 <= ord(letter) <= 102):
			return False
	return True

def validate_byr(v):
	return int(v) >= 1920 and int(v) <= 2002

def validate_iyr(v):
	return int(v) >= 2010 and int(v) <= 2020

def validate_hgt(v):
	if "cm" in v:
		return int(v.split("cm")[0]) >= 150 and int(v.split("cm")[0]) <= 193
	elif "in" in v:
		return int(v.split("in")[0]) >= 59 and int(v.split("in")[0]) <= 76
	return False

valid = 0
fields = {
		"ecl:": validate_ecl, 
		"pid:": validate_pid, 
		"eyr:": validate_eyr, 
		"hcl:": validate_hcl, 
		"byr:": validate_byr,
		"iyr:": validate_iyr, 
		"hgt:": validate_hgt
}

def validate_card(card):
	if any(field not in card for field in fields.keys()):
		return False
	if any(not v(card.split(k)[1].split()[0]) for k, v in fields.items()):
		return False
	return True

with open("day4_input", "r") as f:
	cards = f.read().split("\n\n")

for card in cards:
	if validate_card(card):
		valid += 1

print(valid)