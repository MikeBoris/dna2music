'''
	Generates random 'dna sequence' of length n
	generates sections as dict of dicts

'''
from collections import Counter
import copy
import random
from sys import argv

def generate_sequence(n, chars = ['A','C','T','G']):
	''' returns string ("sequence") of length n '''
	dna = ''
	for i in range(int(n)):
		dna += chars[random.randrange(4)]
	return dna

def alphabet_str(s):
	return ''.join(list(Counter(s)))

def windows(S, T):
	''' given string, alphabet
	returns all substrings containing every char in alphabet
	''' 
	# empty string/multiset is matched everywhere
	if not T:
		yield(0, 0)
		return
	# target multiset initialized to contents of T
	target_ms = Counter(T)
	# empty test multiset
	test_ms = Counter()
	head = enumerate(S)
	tail = enumerate(S)
	# while the condition is not met, advance head 
	# and add to the test multiset
	# iterate over the whole input with head
	for i_head, char_head in head:
		test_ms[char_head] += 1
		# while the condition is met, advance tail
		# (and subtract from test multiset)
		# (a - b) for Counters has only elements from a that
		# remained >0 after subtraction
		while not target_ms - test_ms:
			i_tail, char_tail = tail.next()
			yield (i_tail, i_head + 1)
			test_ms[char_tail] -= 1

def get_word_list(n):
	'''create word_list from scratch'''
	# generate string
	dna = generate_sequence(n)
	# find alphabet
	T = alphabet_str(dna)
	# get list of words
	word_list = [dna[i:j] for i, j in windows(dna, T)]
	#
	return word_list

def is_section(d):
	'''
	check if presection dict satisifies conditions to be deemed 'section'
	'''
	# check if d has at least 4 keys
	if len(d.keys()) < 4:
		return False
	else:
		if sum(d.values()) < 8:
			return False
		else:
			return True
	# check if at least 4 keys contain 2 or more elements

def get_sections(word_list):
	''' given list of words
	returns sections as dict of dicts
	'''
	# initialize new dict for all sections (so a dict of dicts)
	sections = {}
	# initialize empty presection
	presection = {}
	for word in word_list:
		# add word to presection
		# 
		pw = Counter(word)
		n = len(pw)
		# convert word Counter object to 4-char key
		w = ''.join([pw.most_common(n)[i][0] for i in range(n)])
		# add 4-char key to presection
		presection[w] = presection.get(w, 0) + 1
		# check if presection is a section
		fn = is_section(presection)
		if fn:
			# presection is now a section, add it to sections dict
			# create new name for presection, insert into sections dict as sections['name'] = presection
			num = len(sections.keys()) + 1
			name = 's' + str(num)
			presection1 = copy.deepcopy(presection)
			sections[name] = presection1
			# clear contents of presection
			presection.clear()
	return sections

def get_section_stats(sections):
	''' function that takes sections (dict of dicts)
	and returns stats on each
	
	for each section
	calculate:
	number of elements; sum of element counts

	len(d.keys())
	sum(d.values())

	print description:
	avg section length
	longest, shortest sections
	densest sections
	'''
	# number of sections
	x = len(sections)
	# get list of lengths (=num of elements) of each section
	ll = [len(sections[i].values()) for i in sections.keys()]
	# sum of lengths of each section
	y = sum(ll)
	# get longest section
	z = max(ll)
	# shortest section
	w = min(ll)
	print('Number of sections: {0}\nLongest section: {1}'.format(x, z))
'''
sections = {
	's8': {'ATCG': 1, 'ACTG': 3, 'ACGT': 3, 'AGCT': 1},
	's3': {'ATCG': 1, 'ACTG': 3, 'ACGT': 3, 'AGCT': 3, 'CATG': 1, 'CTAG': 1, 'ACTG': 6},
	's1': {'ATCG': 1, 'ACTG': 3, 'ACGT': 3, 'AGCT': 1},
	's2': {'CATG': 1, 'CTAG': 1, 'ACTG': 6}
}
'''
if __name__ == '__main__':
	word_list = get_word_list(argv[1])
	sections = get_sections(word_list)
	get_section_stats(sections)

	#print(sections)
	#for x in sections:
	#	print(x)
		#for y in sections[x]:
		#	print(y, sections[x][y])



