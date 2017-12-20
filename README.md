dna2music WIP
=============

Melody - random walk on notes representing keys...
Rhythm generated using Bjorklund's implementation of Euclidean algorithm.

Program that converts FASTA file to music (in the form of midi, wav, or score).

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
