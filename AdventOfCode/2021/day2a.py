line = input()

horizontal = 0
depth = 0

while line:
	[direction, value] = line.split(' ')
	value = int(value)

	if direction == 'forward':
		horizontal += value
	elif direction == 'down':
		depth += value
	elif direction == 'up':
		depth -= value

	line = input()

print(horizontal * depth)