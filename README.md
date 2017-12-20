dna2music WIP
=============

Layers of abstraction (score, instruments, melodies, notes, rhythms)

Start with string/sequence of characters: `'CATAGTCGATCGTACTCGATCGAATCGAGCTAG'`

This sequence is characterized by the alphabet `['A', 'C', 'G', 'T']`

The first substring containing all characters of alphabet is a word.

Find all words in the string. 

The first sequence of words to satisfy some 'section criteria' is an instrument.

Find all instruments.

Each instrument is represented as a dictionary of word-derived 4-char keys and their corresponding values (counts), e.g.  `'s1': {'ATCG': 1, 'ACTG': 3, 'ACGT': 3, 'AGCT': 1}`

The contents of each instrument-dictionary are used to generate melodies: 
	- generate euclidean rhythm
	- randomly select a key (or multiple keys)
	- all the notes contained in the key(s) are collectively All Possible Notes
 
A melody is a random walk among All Possible Notes according to the selected rhythm pattern.

Each melody has onset and length

Rhythm generated using Bjorklund's implementation of Euclidean algorithm.

## Objective

Program that converts a long string to music (in the form of midi, wav, or score).

### Dependencies
Probably will rely on
- [Biopython](http://biopython.org/)
- [music21](http://web.mit.edu/music21/)

## Examples
### Goal
This program is still WIP.
Ideally it will support functionality like:

#### Begin
Feed dna2music a FASTA file.
```python
from dna2music import d2m

FASTA_FILE = 'path/to/file'

mmmbop = d2m(FASTA_FILE)
```
### Midi
```python
mmmbop.midi
<d2m midi>
```
### Wav

### Score
