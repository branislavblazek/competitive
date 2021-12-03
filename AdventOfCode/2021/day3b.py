inputline = input()
data = []

while inputline:
	numbers = [int(i) for i in inputline]

	data.append(numbers)

	inputline = input()

oxygen_data = data
co2_data = data

def get_bits(records, index):
	result = {0: 0, 1: 0}
	for record in records:
		result[record[index]] += 1
	return result

def get_bit(bits, revert):
	if not revert:
		return 1 if bits[1] >= bits[0] else 0
	else:
		return 0 if bits[0] <= bits[1] else 1 

def filter_data(data, index, equal):
	def filter_fn(record):
		return record[index] == equal

	return list(filter(filter_fn, data))

def get_last_valid_item(data, revert=False):
	i = 0
	while len(data) > 1:
		bits = get_bits(data, i)
		bit = get_bit(bits, revert)
			
		data = filter_data(data, i, bit)

		i += 1

	result = 0
	for index in range(len(data[0])):
		result += 2 ** (len(data[0]) - index - 1) * data[0][index]
	return result
	
oxygen = get_last_valid_item(oxygen_data)
co2 = get_last_valid_item(co2_data, True)
print(oxygen * co2)