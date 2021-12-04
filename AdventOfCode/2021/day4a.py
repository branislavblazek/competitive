numbers = input().split(',')
tables = []

input()

while True:
	table = []
	for _ in range(5):
		line = input()
		
		for i in range(14):
			if i % 3 == 2: line = line[:i] + '|' + line[i + 1:]

		line = [{'value': int(i), 'is_match': False} for i in line.split('|')]
		table.append(line)

	tables.append(table)

	c = input()
	if c == 'x':
		break

def check_tables(all_tables):
	for current_table in all_tables:

		result = {'columns': [0, 0, 0, 0, 0], 'rows': [0, 0, 0, 0, 0]}
		for current_row_index in range(len(current_table)):
			for current_value_index in range(len(current_table[current_row_index])):
				value = 1 if current_table[current_row_index][current_value_index]['is_match'] else 0
				result['columns'][current_value_index] += value
				result['rows'][current_row_index] += value
		state = 5 in result['rows'] or 5 in result['columns']
		if state: return current_table
	return None

def add_value(all_tables, value):
	for current_table in all_tables:
		break_it = False
		for current_row in current_table:
			if break_it: break
			for current_value in current_row:
				if break_it: break
				if current_value['value'] == value: 
					current_value['is_match'] = True
					break_it = True
	return all_tables

def calculate_result(current_table, n):
	unmarked = 0
	for current_row in current_table:
		for current_value in current_row:
			if current_value['is_match'] == False:
				unmarked += current_value['value']

	return unmarked * n
	

def get_result(all_tables, all_numbers):
	for number in all_numbers:
		tables = add_value(all_tables, int(number))
		restab = check_tables(all_tables)
		if restab: return calculate_result(restab, int(number))

print(get_result(tables, numbers))