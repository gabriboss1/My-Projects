from midiutil import MIDIFile

midi = MIDIFile(3)

tempo = 120
midi.addTempo(0, 0, tempo)
midi.addTempo(1, 0, tempo)
midi.addTempo(2, 0, tempo)

midi.addProgramChange(0, 0, 0, 0)
midi.addProgramChange(1, 0, 0, 24)
midi.addProgramChange(2, 0, 0, 32)

melody_notes = [
    (60, 0, 1),
    (62, 1, 1),
    (64, 2, 1),
    (67, 3, 1),
    (65, 4, 1),
    (69, 5, 1),
    (71, 6, 1),
    (72, 7, 1),
    (74, 8, 1),
    (76, 9, 1),
    (79, 10, 1),
    (81, 11, 1)
]

current_time = 0
for pitch, start_time, duration in melody_notes:
    midi.addNote(0, 0, pitch, current_time, duration, 100)
    current_time += duration

chords = [
    [(60, 64, 67), 0, 4],
    [(62, 65, 69), 4, 4],
    [(64, 67, 71), 8, 4],
    [(65, 69, 72), 12, 4],
    [(67, 71, 74), 16, 4],
    [(69, 72, 76), 20, 4],
    [(71, 74, 77), 24, 4],
    [(72, 76, 79), 28, 4]
]

current_time = 0
for chord, start_time, duration in chords:
    for note in chord:
        midi.addNote(1, 0, note, current_time, duration, 80)
    current_time += duration

bass_notes = [
    (36, 2), (38, 2), (40, 2), (41, 2), (43, 2), (45, 2),
    (47, 2), (48, 2), (50, 2), (52, 2), (53, 2), (55, 2)
]

current_time = 0
for i in range(0, 240, 2):
    note, duration = bass_notes[i % len(bass_notes)]
    midi.addNote(2, 0, note, current_time, duration, 110)
    current_time += duration

with open("melody2.mid", "wb") as f:
    midi.writeFile(f)

print("MIDI file with new melody, harmony, and bassline generated successfully.")
