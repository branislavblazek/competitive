line = input()

horizontal = 0
depth = 0
aim = 0

while line:
	[direction, value] = line.split(' ')
	value = int(value)

	if direction == 'forward':
		horizontal += value
		depth += aim * value
	elif direction == 'down':
		aim += value
	elif direction == 'up':
		aim -= value

	line = input()

print(horizontal * depth)