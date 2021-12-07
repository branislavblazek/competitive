with open('input.txt') as f:
	for line in f:
		numbers = [int(i) for i in line.split(',')]

def median(all_numbers):
	all_numbers = sorted(all_numbers)
	l = len(all_numbers)
	if l % 2 == 1: return all_numbers[l // 2]
	else: return (all_numbers[l // 2] + all_numbers[l // 2 - 1]) // 2

def calculate_diff(all_numbers, current_median):
	diff = 0
	for number in all_numbers:
		diff += abs(number - current_median)
	return diff

m = median(numbers)
d = calculate_diff(numbers, m)
print(d)