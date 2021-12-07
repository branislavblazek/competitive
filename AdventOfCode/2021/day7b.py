with open('input.txt') as f:
	for line in f:
		numbers = [int(i) for i in line.split(',')]

def mode(all_numbers):
	return sum(all_numbers) // len(all_numbers)

def gauss(n):
	return (n * (n + 1)) // 2

def calculate_diff(all_numbers, current_median):
	diff = 0
	for number in all_numbers:
		diff += gauss(abs(number - current_median))
	return diff

m = mode(numbers)
d = calculate_diff(numbers, m)
print(d)