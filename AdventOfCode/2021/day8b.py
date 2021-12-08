def sortFn(e): return len(e)

#.-0-.
#|   |
#1   2
#|   |
#|-3-|
#|   |
#4   5
#|   |
#.-6-.

correct_places = {
	0: [0, 1, 2, 4, 5, 6],
	1: [2, 5],
	2: [0, 2, 3, 4, 6],
	3: [0, 2, 3, 5, 6],
	4: [1, 2, 3, 5],
	5: [0, 1, 3, 5, 6],
	6: [0, 1, 3, 4, 5, 6],
	7: [0, 2, 5],
	8: [0, 1, 2, 3, 4, 5, 6],
	9: [0, 1, 2, 3, 5, 6]
}

lennums = {
	2: 1,
	3: 7,
	4: 4,
	7: 8
}

what_numbers = [[3], [0, 1, 3, 4, 6], [1, 5], [1, 4], [0, 4, 6], [2, 4], [2], [1, 3, 4, 6], [], [4]]

def is_interception(allx, compare):
	a = set()
	for s in allx:
		i = s.intersection(compare)
		if i: a.update(i)

	return a if len(a) else False

def write(what, where, alls):
	for place in where:
		alls[place].update(what)

def remove_all_occurs(of_what, fromw):
	for si in range(len(fromw)):
		s = fromw[si]
		i = s.intersection(of_what)
		if len(i):
			fromw[si] = fromw[si] - of_what

all_res = 0
with open('input.txt') as f:
	for line in f:
		all_values = []
		all_patterns = []
		line = line.rstrip()
		[patterns, values] = line.split(' | ')
		p = patterns.split(' ')
		p.sort(key=sortFn)
		all_patterns.append(p)
		all_values = values.split(' ')

		segments = [set(), set(), set(), set(), set(), set(), set()]

		for x in all_patterns:
			used_places = set()
			for p in x:
				if len(p) in [2,3,4,7]:
					pattern = {i for i in p}
					places = {i for i in correct_places[lennums[len(pattern)]]}

					inter = is_interception(segments, pattern)

					updt = pattern if not inter else pattern - inter
					updtplcs = places if not inter else places - used_places

					write(updt, updtplcs, segments)
					used_places.update(places)


		sixs = list(filter(lambda i: len(i) == 6, x))
		temp = []
		for value in sixs:
			temp.append({i for i in value})
		sixs = temp
		diff_at = [2,3,4]
		diffs = set()

		i1 = sixs[0].intersection(sixs[1])
		i2 = sixs[0].intersection(sixs[2])
		i3 = sixs[1].intersection(sixs[2])
		diffs.update(sixs[0] - i1, sixs[1] - i1)
		diffs.update(sixs[0] - i2, sixs[2] - i2)
		diffs.update(sixs[1] - i3, sixs[2] - i3)

		for place in diff_at:
			i = segments[place].intersection(diffs)
			remove_all_occurs(i, segments)
			segments[place] = i

		segmentsset = set()
		temp = []
		for aa in segments:
			temp.append(list(aa)[0])
			segmentsset.update(aa)
		
		result = ''

		for value in all_values:
			v = list(segmentsset - {i for i in value})
			diffs = []
			for x in v: diffs.append(temp.index(x))
			for maybei in range(len(what_numbers)):
				maybe = what_numbers[maybei]
				if sorted(maybe) == sorted(diffs):
					result += str(maybei)
					break

		all_res += int(result)
print(all_res)