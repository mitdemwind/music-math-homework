import numpy as np

melody_1 = np.array([
        ['', '', '', '', '', '', '', 'A'],
        ['A', 'B', 'B', 'C5', 'C5', 'B', 'B', 'A'],
        ['A', 'E', 'E', 'C', 'C', 'A3', 'A3', 'G'],
        ['G', 'F', 'F', 'E', 'F', 'G', 'F', ''],
        ['', '', '', 'F', 'F', 'G', 'G', 'A'],
        ['A', 'B', 'B', 'G', 'G', 'D', 'D', 'F'],
        ['F', 'E', 'E', 'D', 'E', 'F', 'E', ''],
        ['', '', '', '', '', '', '', '']])
melody_2 = np.array([
        ['', 'G', 'G', 'E', 'D', 'E', 'A3', ''],
        ['D', 'E', 'G', 'E', 'D', '', '', ''],
        ['', 'G', 'G', 'E', 'D', 'E', 'G3', ''],
        ['D', 'E', 'G', 'D', 'C', '', '', ''],
        ['', 'C', 'D', 'E', 'G', 'A', 'G', 'E'],
        ['G', 'E', 'E', 'D', 'D', '', '', ''],
        ['', 'C', 'D', 'C', 'D', '', 'C', 'D'],
        ['', 'E', '', 'G', '', 'E', '', '']])
melody_3 = np.array([
        ['', '', '', '', '', '', 'A', 'B'],
        ['C5', '', '', 'B', 'C5', '', 'E5', ''],
        ['B', '', '', '', '', '', 'E', ''],
        ['A', '', '', 'G', 'A', '', 'C5', ''],
        ['G', '', '', '', '', '', 'E', ''],
        ['F', '', '', 'E', 'F', 'C5', '', ''],
        ['E', '', '', '', '', '', 'C5', 'C5'],
        ['B', '', '', 'G', 'G', '', 'B', '']])
melody_4 = np.array([
        ['', '', '', '', '', '', 'C', 'D'],
        ['E', '', 'E', '', 'D', '', 'E', ''],
        ['D', 'C', 'B3', 'A3', '', '', 'E3', 'A3'],
        ['G3', '', '', 'A3', 'B3', '', 'A3', 'G3'],
        ['A3', '', '', '', 'C', 'B3', 'A3', 'B3'],
        ['A', '', '', '', '', '', '', ''],
        ['', '', '', 'E3', 'C', 'B3', 'A3', 'B3'],
        ['A3', '', '', '', '', '', '', '']])
melody_5 = np.array([
        ['C', '', 'E', '', 'G', '', 'A', ''],
        ['F', '', 'C', '', 'E', '', 'E3', ''],
        ['F3', '', 'C', '', 'C', '', 'B3', ''],
        ['C', 'B3', 'C', 'E3', 'G3', '', 'B3', ''],
        ['C', '', 'E', '', 'G', 'E', 'G', 'A'],
        ['F', 'E', 'D', 'F', 'E', 'D', 'C', 'B3'],
        ['A3', 'F3', 'C', '', 'C', '', 'C', 'B3'],
        ['C', 'B3', 'C', 'E3', 'G3', '', 'B3', ''],])
melody_6 = np.array([
        ['E', '', 'E5', '', 'E5', 'D5', 'E5', 'A5'],
        ['G5', '', 'E5', '', 'G5', '', '', ''],
        ['A5', '', 'C5', '', 'A', 'B', 'C5', 'F5'],
        ['E5', '', 'D5', 'C5', 'B', '', '', ''],
        ['C5', '', 'A', 'B', 'C5', 'C5', 'C5', 'F5'],
        ['E5', '', 'E5', 'C5', 'D5', '', '', ''],
        ['E5', '', '', '', 'A', '', 'B', ''],
        ['B', '', '', '', '', '', '', '']])
melody_7 = np.array([
        ['', 'C', 'C', 'A3', 'C', 'A3', 'C', 'D'],
        ['E', '', 'C', 'C', 'G3', 'E', '', ''],
        ['', '', '', '', '', 'C', 'C', 'C'],
        ['B3', '', '', 'B3', 'B3', 'A3', 'C', ''],
        ['', 'C', 'C', 'A3', 'C', 'A3', 'C', 'D'],
        ['E', '', 'C', 'C', 'G', 'E', '', ''],
        ['', '', '', '', '', 'C', 'C', 'D'],
        ['', '', '', '', '', 'E', 'E', 'E']])
melody_8 = np.array([
        ['G', 'B', 'B', 'C5', 'C5', 'D5', 'D5', 'G5'],
        ['F5', '', '', 'D5', 'C5', '', '', ''],
        ['G', 'B', 'B', 'C5', 'C5', 'D5', 'D5', ''],
        ['G', '', 'F', '', '', '', '', ''],
        ['G', 'B', 'B', 'C5', 'C5', 'D5', 'D5', 'G5'],
        ['F5', '', '', 'D5', 'C5', '', '', ''],
        ['C5', 'D5', 'G', '', 'C5', 'D5', 'G', 'F'],
        ['G', '', '', '', '', '', '', '']])
melody_9 = np.array([
        ['G', '', 'E', 'G', 'C5', '', '', ''],
        ['A', '', 'C5', '', 'G', '', '', ''],
        ['G', '', 'C', 'D', 'E', '', 'D', 'C'],
        ['D', '', '', '', '', '', '', ''],
        ['G', '', 'E', 'G', 'C5', '', '', 'B'],
        ['A', '', 'C5', '', 'G', '', '', ''],
        ['G', '', 'D', 'E', 'F', '', '', 'B'],
        ['C', '', '', '', '', '', '', '']])
melody_10 = np.array([
        ['', '', 'A', 'B', 'C5', '', 'G5', ''],
        ['F5', '', '', '', '', '', '', ''],
        ['', '', 'G', 'A', 'B', '', 'F5', ''],
        ['E5', '', '', '', '', '', '', ''],
        ['', '', 'E5', 'E5', 'A5', '', 'G5', ''],
        ['F5', '', 'D5', '', '', '', 'C5', ''],
        ['B', '', 'C5', 'D5', '', '', 'F5', ''],
        ['E5', '', '', '', '', '', '', '']])

