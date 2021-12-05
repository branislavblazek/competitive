lines = []

diagram = []

for y in range(1001):
	l = []
	for x in range(1001):
		l.append(0)
	diagram.append(l) 

with open('input.txt') as f:
	for line in f:
		line = line.rstrip()
		[first, second] = line.split(' -> ')
		record = []
		record.append(first.split(','))
		record.append(second.split(','))
		lines.append(record)

def filter_lines(all_lines):
	def filter_fn(current_record):
		x1 = current_record[0][0]
		y1 = current_record[0][1]
		x2 = current_record[1][0]
		y2 = current_record[1][1]
		return x1 == x2 or y1 == y2

	return list(filter(filter_fn, all_lines))

def spread_line(current_line):
	start_x = int(current_line[0][0])
	start_y = int(current_line[0][1])
	end_x = int(current_line[1][0])
	end_y = int(current_line[1][1])
	is_same_x = False
	is_same_y = False

	if start_x == end_x:
		m = min(start_y, end_y)
		n = abs(start_y - end_y)
		is_same_x = True
	elif start_y == end_y:
		m = min(start_x, end_x)
		n = abs(start_x - end_x)
		is_same_y = True

	if n == 1: 
		return [[start_x, start_y], [end_x, end_y]]

	result = []
	for i in range(m, m + n + 1):
		new_item = [start_x, i] if is_same_x else [i, start_y]
		result.append(new_item)
	return result

def write_into(current_diagram, current_spreaded):
	for current_item in current_spreaded:
		[current_x, current_y] = current_item
		actual_value_at = current_diagram[current_y][current_x]
		if actual_value_at == 0:
			current_diagram[current_y][current_x] = 1
		else:
			current_diagram[current_y][current_x] += 1

	return current_diagram

def count_overlaps(current_diagram):
	n = 0
	for y in current_diagram:
		for x in y:
			if x >= 2: n += 1
	return n

lines = filter_lines(lines)
for line in lines:
	spreaded = spread_line(line)
	diagram = write_into(diagram, spreaded)

for y in diagram:
	print(y)
print(count_overlaps(diagram))