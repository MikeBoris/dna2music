dna2music
=========

Program that converts FASTA file to music (in the form of midi, wav, or score).

## Dependencies
Probably will rely on
- [Biopython](http://biopython.org/)
- [music21](http://web.mit.edu/music21/)

# Examples
### Begin
Feed dna2music a FASTA file.
```python
from dna2music import d2m

FASTA_FILE = 'path/to/file'

mmmbop = d2m(FASTA_FILE)
```
## Midi
```python
mmmbop.midi
<d2m midi>
```
## Wav

## Score