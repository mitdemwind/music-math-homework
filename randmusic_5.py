import music21 as ms
import random
from utils import *

bass = ms.clef.BassClef()
SCALE = ['C', 'D', 'E', 'G', 'A']
SCALEn = [0, 2, 4, 7, 9]
RHYTHM = [
        [4],
        [2, 2],
        [2, 2],
        [1, 1, 2],
        [2, 1, 1],
        [1, 2, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 3],
        [3, 1]
        ]

#######################################
def bg():
    m1 = ms.stream.Measure()
    m1.keySignature = ms.key.Key('C')
    m1.append(ms.note.Note('F2', type='quarter'))
    m1.append(ms.note.Note('C3', type='quarter'))
    m1.append(ms.note.Note('F3', type='half'))

    m2 = ms.stream.Measure()
    m2.keySignature = ms.key.Key('C')
    m2.append(ms.note.Note('G2', type='quarter'))
    m2.append(ms.note.Note('D3', type='quarter'))
    m2.append(ms.note.Note('G3', type='half'))

    m3 = ms.stream.Measure()
    m3.keySignature = ms.key.Key('C')
    m3.append(ms.note.Note('A2', type='quarter'))
    m3.append(ms.note.Note('E3', type='quarter'))
    m3.append(ms.note.Note('A3', type='half'))

    m4 = ms.stream.Measure()
    m4.keySignature = ms.key.Key('C')
    m4.append(ms.note.Note('A2', type='quarter'))
    m4.append(ms.note.Note('E3', type='quarter'))
    m4.append(ms.note.Note('A3', type='half'))
    return [m1, m2, m3, m4]

def to_pitch(note: int) -> str:
    if note == -1:
        return ''
    octave = note // 5
    return SCALE[note % 5] + str(octave)
# C4 is 20

def update(note: int) -> int:
    if note < 21:
        return note + random.randint(0, 3)
    if note > 27:
        return note + random.randint(-2, 1)
    return note + random.randint(-2, 3)

def generate_melody(start, r1, r2):
    new = start
    nl = []
    for i in r1:
        new = update(new)
        nl.append(new)
        if i > 1:
            nl.extend([-1] * (i-1))
    for i in r2:
        new = update(new)
        nl.append(new)
        if i > 1:
            nl.extend([-1] * (i-1))
    # print(nl)
    nl = list(map(to_pitch, nl))
    return nl, new

bgmusic = ms.stream.Part([*bg(), *bg()])
bgmusic.insert(0, bass)

def to_measure(melody):
    stream = ms.stream.Measure()
    stream.keySignature = ms.key.Key('C')
    for data in melody:
        if data == '':
            stream[-1].duration.quarterLength += 0.5
            continue
        note = ms.note.Note(data)
        note.duration.quarterLength = 0.5
        stream.append(note)
    return stream

def gen_fg():
    start = 24
    ret = []
    r1 = random.choice(RHYTHM)
    r2 = random.choice(RHYTHM)
    r3 = random.choice(RHYTHM)
    r4 = random.choice(RHYTHM)
    for i in range(8):
        if i % 2 == 1:
            nl, start = generate_melody(start, r1, r2)
        else:
            nl, start = generate_melody(start, r3, r4)
        ret.append(nl)
    return list(map(to_measure, ret))

for i in range(20):
    fg = ms.stream.Part(gen_fg())
    fg.write('xml', './data/initial_' + str(i))

# sss = ms.stream.Score([fg, bgmusic])
# sss.show()
