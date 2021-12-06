inpt = []
data = {}
mid_data = {}
result = 0
days = 256

with open('input.txt') as f:
	for line in f:
		inpt = [int(i) for i in line.split(',')]

def calculate(number):
	is_first = True
	depth = 1

	while number > 0:
		number -= 9 if is_first else 7
		if number > 0: 
			if number in mid_data:
				depth += mid_data[number]
			else:
				x = calculate(number)
				mid_data[number] = x
				depth += x
		is_first = False

	return depth

def run_calculations(days, offset):
	depth = 1
	number = days - offset
	while number > 0:
		depth += calculate(number)
		number -= 7
	
	return depth

for x in inpt:
	if x in data:
		result += data[x]
	else:
		l = run_calculations(days, x)
		data[x] = l
		result += l

print(result)