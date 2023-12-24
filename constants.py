DATAPATH = './data/'
MUTATE_RATE = 0.6

# the pitch number assigned for extending the last note
EXTEND = [-1, '']

# scale offset
MAJSCALE = [0, 2, 4, 5, 7, 9, 11]
RHYTHM = [[4],
        [1, 3],
        [3, 1],
        [1, 2, 1],
        [2, 2],
        [1, 1, 2],
        [2, 1, 1],
        [1, 1, 1, 1]]

# define the global key signature
C3 = 48
C4 = 60
C5 = 72
C6 = 84

# chords in major scale, omitted the vii chord
CHORDS = [
        [0, 4, 7, 11],
        [2, 5, 9, 0],
        [4, 7, 11, 2],
        [5, 9, 0, 4],
        [7, 11, 2, 5],
        [9, 0, 4, 7],
        ]
CHORD_PROG = {
        0: [0, 1, 2, 3, 4, 5],
        1: [4, 1],
        2: [5, 3, 1, 2],
        3: [4, 0, 3],
        4: [0, 5, 4],
        5: [1, 2, 3, 5]
        }
CHORD_STRING = {
        0: ['C3', 'G3', 'C4'],
        1: ['D2', 'F2', 'D3'],
        2: ['E2', 'G2', 'E3'],
        3: ['F2', 'A2', 'F3'],
        4: ['G2', 'B2', 'G3'],
        5: ['A2', 'C3', 'A3']}

##### below are unused yet
MINSCALE = [0, 2, 3, 5, 7, 8, 10]

# offsets of chords
MAJ3CHORD = [0, 4, 7]
MIN3CHORD = [0, 3, 7]
DIM3CHORD = [0, 3, 6]
AUG3CHORD = [0, 4, 8]

Mm7CHORD = [0, 4, 7, 10]
mm7CHORD = [0, 3, 7, 10]
MM7CHORD = [0, 4, 7, 11]
dm7CHORD = [0, 3, 6, 10]
