"""
Write static helper functions here
"""
import numpy as np
from constants import *

def to_pitchclass(midi_number: int) -> tuple[int]:
    """
    Convert a midi numder into (pitchClass, octaveNumber)
    e.g. to_pitchclass(60) == (0, 4) is the note C4
    """
    return (MAJSCALE.index(midi_number % 12), midi_number // 12 - 1)

def to_note(pitchclass: int, octave: int) -> int:
    """
    The inverse function of to_pitchclass
    e.g. to_note(0, 4) == 60 is C4
    """
    return MAJSCALE[pitchclass] + 12 * (1 + octave)

def lift(note: int, distance: int) -> int:
    """
    Returns a new note raised by the distance
    e.g. raise(C4, 1) == D4, raise(C4, 5) == A4
    """
    pc, octave = to_pitchclass(note)
    pc += distance
    octave += pc // 7
    pc %= 7
    return to_note(pc, octave)
