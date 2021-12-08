all_values = []
allowed_lens = [2, 4, 3, 7]

with open('input.txt') as f:
	for line in f:
		line = line.rstrip()
		[patterns, values] = line.split(' | ')
		all_values.append(values.split(' '))

s = 0
for current_value in all_values:
	for value in current_value:
		if len(value) in allowed_lens:
			s += 1
print(s)