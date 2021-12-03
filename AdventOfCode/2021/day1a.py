last = None
deep = input()
increased = 0

while deep:
	deep = int(deep)
	if last == None:
		last = deep
		deep = input()
		continue

	if deep > last:
		increased += 1

	last = deep
	deep = input()

print(increased)