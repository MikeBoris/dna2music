# dna2.py

from collections import Counter
import random
from sys import argv

def generate_sequence(n, chars = ['A','C','T','G']):
	dna = ''
	for i in range(int(n)):
		dna += chars[random.randrange(4)]
	return dna

# print alphabet
def get_alphabet(s):
	return list(Counter(s))

def alphabet_str(s):
	return ''.join(list(Counter(s)))

def windows(S, T):
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







if __name__ == '__main__':
	print('\n')
	# generate string
	dna = generate_sequence(argv[1])

	

	T = alphabet_str(dna)
	words = [dna[i:j] for i, j in windows(dna, T)]
	cnt = Counter()
	for word in words:
		cnt[word] += 1
	x = list(cnt.elements())
	y = len(x) / float(len(dna))
	#for i in range(len(x)):
	#	print(x[i])
	print(' ------------------------------------------')
	print(' | Sequence length:                   %s  |' % len(dna))
	print(' | Number of words:                   %s   |' % len(x))
	print(' | Length of longest word in list:    %s   |' % len(max(x, key=len)))
	print(' | Number of sections:                %s |' % y)
	print(' ------------------------------------------')
	print('\n')
	
	
	print('Alphabet is: %s' % ''.join(get_alphabet(dna)))
	print('DNA: %s' % dna)
	print('Longest word in list: %s' % max(x, key=len))
	
	print('\n')
	print('Print groups of k words: ')
	for i in range(len(x)):
		print(x[i])
	'''
	okay we have a list of words
	but we need sections (sequences of words)
	now, first create a new sequence
		while most_common_letters_count < 4 (or some arbitrary #)
		start with the first word; concatenate with the second word; concatenate with the third word;

	for i in list of words:
		while most_common_letter < 4:
			Counter(x[i]).most_common(1)

			Counter(x[i] + x[i+1]).most_common(1)

			# number value of most common character in Counter object
			x.most_common(1)[0][1]
			# char of most common character in Counter object
			x.most_common(1)[0][0]

			new_str = ''
			new_str += x.most_common(1)[0][0]
			print(new_str)
			A
			y = Counter('ATACAGCTAGATCTT')
			new_str += y.most_common(1)[0][0]
			new_str
			'AA'
