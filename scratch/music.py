'''
Takes some sort of input and convert to musical notes

'''
from music21 import note, stream

n1 = note.Note("F#3")
n2 = note.Note("G3")
n3 = note.Note("B-4")

s1 = stream.Stream()

s1.append(n1)
s1.append(n2)
s1.append(n3)

s1.show('midi')