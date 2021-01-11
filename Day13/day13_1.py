#######################
# Stephen Boyett
# Advent of Code
# Day 13 Part 1
# 1/3/2021
########################



def main():
	with open("day13_input", "r") as f:
		data = f.read().splitlines()

	earliest_depart = int(data[0])
	buses = [int(i) for i in data[1].split(",") if i is not "x"]
	bus_depart_time = {abs((earliest_depart % buses[i]) - buses[i]): buses[i] for i in range(len(buses))}


	earliest_depart_time = min(bus_depart_time) + earliest_depart
	print(f"earliest_depart: {earliest_depart}")
	print(f"trains: {buses}")
	print(f"trains_depart_time is: {bus_depart_time}")
	print(f"earliest_depart_time = {earliest_depart_time}")
	answer = bus_depart_time[min(list(bus_depart_time.keys()))]*min(list(bus_depart_time.keys()))
	print(f"Answer is: {answer}")

if __name__=="__main__":
	main()

 
