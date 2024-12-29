from midiutil import MIDIFile

midi = MIDIFile(3)

tempo = 160
midi.addTempo(0, 0, tempo)
midi.addTempo(1, 0, tempo)
midi.addTempo(2, 0, tempo)

midi.addProgramChange(0, 0, 0, 0)  
midi.addProgramChange(1, 0, 0, 24)
midi.addProgramChange(2, 0, 0, 32)

melody_notes = [
    (60, 0, 0.5), (62, 0.5, 0.5), (64, 1, 0.5), (67, 1.5, 0.5), 
    (69, 2, 0.5), (72, 2.5, 0.5), (74, 3, 0.5), (77, 3.5, 0.5), 
    (79, 4, 0.5), (81, 4.5, 0.5), (83, 5, 0.5), (84, 5.5, 0.5),
    (86, 6, 0.5), (88, 6.5, 0.5), (90, 7, 0.5), (91, 7.5, 0.5)
]

current_time = 0
for pitch, start_time, duration in melody_notes:
    midi.addNote(0, 0, pitch, current_time, duration, 100)
    current_time += duration

chords = [
    [(60, 64, 67), 0, 2], [(62, 65, 69), 2, 2], [(64, 67, 71), 4, 2], 
    [(65, 69, 72), 6, 2], [(67, 71, 74), 8, 2], [(69, 72, 76), 10, 2], 
    [(72, 76, 79), 12, 2], [(74, 77, 81), 14, 2], [(76, 79, 83), 16, 2],
    [(78, 82, 86), 18, 2], [(80, 84, 88), 20, 2], [(82, 86, 90), 22, 2]
]

current_time = 0
for chord, start_time, duration in chords:
    for note in chord:
        midi.addNote(1, 0, note, current_time, duration, 80)
    current_time += duration

bass_notes = [
    (36, 0.5), (40, 1), (43, 1.5), (45, 2), (48, 2.5), (50, 3), 
    (53, 3.5), (55, 4), (57, 4.5), (60, 5), (62, 5.5), (64, 6),
    (65, 6.5), (67, 7), (69, 7.5), (71, 8)
]

current_time = 0
for i in range(0, 240, 1):
    note, duration = bass_notes[i % len(bass_notes)]
    midi.addNote(2, 0, note, current_time, duration, 110)
    current_time += duration

with open("melody3.mid", "wb") as f:
    midi.writeFile(f)

print("MIDI file with dynamic melody and harmony generated successfully.")
