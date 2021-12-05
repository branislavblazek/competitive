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

def spread_line(current_line):
	start_x = int(current_line[0][0])
	start_y = int(current_line[0][1])
	end_x = int(current_line[1][0])
	end_y = int(current_line[1][1])
	is_same_x = False
	is_same_y = False
	limit = 1

	if start_x == end_x:
		m = min(start_y, end_y)
		limit = abs(start_y - end_y)
		is_same_x = True
	elif start_y == end_y:
		m = min(start_x, end_x)
		limit = abs(start_x - end_x)
		is_same_y = True

	if is_same_x or is_same_y:
		if limit == 1: 
			return [[start_x, start_y], [end_x, end_y]]

		result = []
		for i in range(m, m + limit + 1):
			new_item = [start_x, i] if is_same_x else [i, start_y]
			result.append(new_item)
		return result
	elif is_same_x is False and is_same_y is False:
		limit = abs(start_x - end_x)
		result = []
		for i in range(limit + 1):
			new_item = []
			if start_x > end_x:
				new_item.append(start_x - i)
			else:
				new_item.append(start_x + i)
			if start_y > end_y:
				new_item.append(start_y - i)
			else:
				new_item.append(start_y + i)
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

for line in lines:
	spreaded = spread_line(line)
	diagram = write_into(diagram, spreaded)

print(count_overlaps(diagram))