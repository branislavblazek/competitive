number = input()

numbers = []

slides = [[], [], []]

all_slides = []

while number:
	n = int(number)
	numbers.append(n)

	number = input()

for nindex in range(len(numbers)):
	num = numbers[nindex]
	if nindex == 0:
		slides[0].append(num)
		continue

	if nindex == 1:
		slides[0].append(num)
		slides[1].append(num)
		continue

	if len(slides[0]) == 3: 
		all_slides.append(sum(slides[0]))
		slides[0] = [num]
	else: slides[0].append(num)

	if len(slides[1]) == 3: 
		all_slides.append(sum(slides[1]))
		slides[1] = [num]
	else: slides[1].append(num)

	if len(slides[2]) == 3: 
		all_slides.append(sum(slides[2]))
		slides[2] = [num]
	else: slides[2].append(num)

if (len(slides[0])) == 3: all_slides.append(sum(slides[0]))
if (len(slides[1])) == 3: all_slides.append(sum(slides[1]))
if (len(slides[2])) == 3: all_slides.append(sum(slides[2]))

increased = 0
last = None
for slide in all_slides:
	if last == None: 
		last = slide
		continue

	if slide > last:
		increased += 1

	last = slide

print('xxx')
print(increased)
