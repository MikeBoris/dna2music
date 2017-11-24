'''
Program to return dna string.

> python dna.py dclynch123@gmail.com
>NM_002299.3 Homo sapiens lactase (LCT), mRNA

GTTCCTAGAAAATGGAGCTGTCTTGGCATGTAGTCTTTATTGCCCTGCTAAGTTTTTCATGCTGGGGGTC

AGACTGGGAGTCTGATAGAAATTTCATTTCCACCGCTGGTCCTCTAACCAATGACTTGCTGCACAACCTG

...

http://biopython.org/DIST/docs/api/Bio.Entrez-module.html

Input:	
		an email address (for pubmed authentication) - as cml argument
		id (has a default right now)

'''
from sys import argv
from Bio import Entrez, Seq, SeqIO
from Bio.Alphabet import IUPAC

def dna_fetch(email, id=['NM_002299']):
	Entrez.email = email
	hdl = Entrez.efetch(db='nucleotide', id=id, rettype='fasta')
	return hdl

# seq = SeqIO.read(hdl, 'fasta')


from desulfo import genome

# number of 


from collections import Counter
import re

cnt = Counter()
for c in genome:
    cnt[c] += 1

# Counter({'A': 9027, 'T': 7620, 'G': 6453, 'C': 5110, '\n': 403})

import re, random

chars = ['G', 'A', 'T', 'C']
dna = ''
for i in range(100):
    dna += chars[random.randrange(4)]

print(dna)

# list minimal alphabets ('words')
pattern = r'\b(the\s+\w+)\s+'
regex = re.compile(pattern, re.IGNORECASE)
for match in regex.finditer(html):
    print "%s: %s" % (match.start(), match.group(1))



matches = re.finditer(r"[AT]{6,}", dna) 
for m in matches: 
    base = m.group() 
    pos  = m.start() 
    print(base + " found at position " + str(pos))






if __name__ == '__main__':
	#h = dna_fetch(argv[1])
	#for l in h:
	#	print(l)
