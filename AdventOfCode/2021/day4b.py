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
	indexes = []
	for current_table_index in range(len(all_tables)):
		current_table = all_tables[current_table_index]
		result = {'columns': [0, 0, 0, 0, 0], 'rows': [0, 0, 0, 0, 0]}
		for current_row_index in range(len(current_table)):
			for current_value_index in range(len(current_table[current_row_index])):
				value = 1 if current_table[current_row_index][current_value_index]['is_match'] else 0
				result['columns'][current_value_index] += value
				result['rows'][current_row_index] += value

		state = 5 in result['rows'] or 5 in result['columns']
		if state: return current_table_index

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
	result = None
	for number in all_numbers:
		if result is not None:
			return result

		tables = add_value(all_tables, int(number))
		restab_index = check_tables(all_tables)
		while restab_index is not None:
			if result is not None:
				break

			if (len(all_tables) > 1):
				del all_tables[restab_index]
				restab_index = check_tables(all_tables)
				continue

			if check_tables(all_tables) is not None:
				result = calculate_result(all_tables[0], int(number))

			restab_index = check_tables(all_tables)

print(get_result(tables, numbers))