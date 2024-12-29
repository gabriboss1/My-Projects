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
    (60, 0, 2), (62, 2, 2), (64, 4, 2), (65, 6, 2), (67, 8, 2), (69, 10, 2),
    (71, 12, 2), (72, 14, 2), (74, 16, 2), (76, 18, 2), (77, 20, 2), (79, 22, 2)
]

current_time = 0
for pitch, start_time, duration in melody_notes:
    midi.addNote(0, 0, pitch, current_time, duration, 100) 
    current_time += duration

chords = [
    [(60, 64, 67), 0, 4],   
    [(62, 65, 69), 4, 4],   
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

with open("melody1.mid", "wb") as f:
    midi.writeFile(f)

print("MIDI file with melody, harmony, and bassline generated successfully.")
