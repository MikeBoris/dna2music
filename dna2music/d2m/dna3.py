# dna3.py
from collections import Counter
import copy
from sys import argv


dj = {'ATGC': 3, 'CTGA': 2, 'GTCA': 10, 'GATC': 1}

from dna2 import generate_sequence, alphabet_str, windows

def get_word_list(n):
	'''create word_list from scratch'''
	# generate string
	dna = generate_sequence(n)
	# find alphabet
	T = alphabet_str(dna)
	# get list of words
	words = [dna[i:j] for i, j in windows(dna, T)]
	#
	return words

word_list = get_word_list(argv[1])

#['CATAAG', 'GACAT', 'ACATAAG', 'TAAGC', 'AGTTTGAC', 'GCGCAT', 
#'AGCGCAT', 'TTGAC', 'GTTTGAC', 'AAGCGCAT', 'TGAC', 'CATG', 'GCAT', 'CGCAT', 'TTTGAC', 'ATAAGC']

# function to check if presection dict satisifies conditions to be deemed 'section'
def is_section(d):
	# check if d has at least 4 keys
	if len(d.keys()) < 4:
		return False
	else:
		if sum(d.values()) < 8:
			return False
		else:
			return True
	# check if at least 4 keys contain 2 or more elements

#print(is_section(dj))

# create section

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

for x in sections:
    print (x)
    for y in sections[x]:
        print (y,':',sections[x][y])
#print(sections)


# for each section
# calculate:
# number of elements; sum of element counts

#len(d.keys())
#sum(d.values())


# print description:
# avg section length
# longest, shortest sections
# densest sections
# 


