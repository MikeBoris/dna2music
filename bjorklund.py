# bjorklund.py

# need count array
count = []
# need level
# need remainder array
remainder = []

def build_string(level):
	if level == -1:
		bitmap.append('0')
	elif level == -2:
		bitmap.append('1')
	else:
		for i in range(len(count[level])):
			build_string(level - 1)
		if remainder[level] != 0:
			build_string(level - 2)

def compute_bitmap(num_steps, num_pulses):
	# first compute count and remainder arrays
	divisor = num_steps - num_pulses
	remainder[0] = num_pulses
	level = 0
	while remainder[level] > 1:
		count[level] = divisor / remainder[level]
		remainder[level + 1] = divisor % remainder[level]
		level += 1
	count[level] = divisor
	build_string(level)


def bjorklund(steps, pulses):
	steps = int(steps)
	pulses = int(pulses)
	# pulses can't be > steps
	if pulses > steps:
		raise ValueError
	pattern = []
	counts = []
	remainders = []
	divisor = steps - pulses
	remainders.append(pulses)
	level = 0
	while True:
		counts.append(divisor / remainders[level])
		remainders.append(divisor % remainders[level])
		divisor = remainders[level]
		level += 1
		if remainders[level] <= 1:
			break
	counts.append(divisor)

	def build(level):
		if level == -1:
			pattern.append(0)
		elif level == -2:
			pattern.append(1)
		else:
			for i in xrange(0, counts[level]):
				build(level - 1)
			if remainders[level] != 0:
				build(level - 2)

	build(level)
	i = pattern.index(1)
	pattern = pattern[i:] + pattern[0:i]
	return pattern

print(bjorklund(13,5))	

