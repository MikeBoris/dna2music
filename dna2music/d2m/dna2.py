# dna2.py

from collections import Counter
import random

def generate_sequence(n, chars = ['A','C','T','G']):
	dna = ''
	for i in range(n):
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
	print('-----------------------------------------------')
	# generate string
	dna = generate_sequence(100)

	print('Alphabet is: %s' % ''.join(get_alphabet(dna)))

	T = alphabet_str(dna)
	print('Words found: ')
	words = [dna[i:j] for i, j in windows(dna, T)]
	cnt = Counter()
	for word in words:
		cnt[word] += 1
	print(cnt.most_common(3))
