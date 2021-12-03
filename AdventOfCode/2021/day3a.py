inputline = input()

bits = []

while inputline:
	numbers = [int(i) for i in inputline]

	while len(bits) != len(numbers):
		bits.append({0: 0, 1: 0})

	for index in range(len(numbers)):
		bits[index][numbers[index]] += 1


	inputline = input()

gamma = 0
epsilon = 0

for bit_index in range(len(bits)):
	n = len(bits) - bit_index - 1
	if bits[bit_index][0] > bits[bit_index][1]:
		gamma += 0
		epsilon += 2 ** n
	else:
		gamma += 2 ** n
		epsilon += 0

print(gamma * epsilon)
