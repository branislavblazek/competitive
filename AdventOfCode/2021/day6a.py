lanternfish = []
days = 18

with open('input.txt') as f:
	for line in f:
		lanternfish = [int(i) for i in line.split(',')]

for day in range(days):
	add_fishes = 0
	for fish_index in range(len(lanternfish)):
		fish = lanternfish[fish_index]
		if fish > 0:
			lanternfish[fish_index] -= 1
		elif fish == 0:
			lanternfish[fish_index] = 6
			add_fishes += 1

	for _ in range(add_fishes):
		lanternfish.append(8)

print(len(lanternfish))
