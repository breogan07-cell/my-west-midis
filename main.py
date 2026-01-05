import mido
from mido import Message, MidiFile, MidiTrack, MetaMessage

# 1. Setup the MIDI file
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# 2. Settings (155 BPM is the "sweet spot" for a fast banjo chase)
track.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(155)))
track.append(Message('program_change', program=105, time=0)) # 105 = Banjo

def add_note(note, duration, velocity, time_since_last=0):
    track.append(Message('note_on', note=note, velocity=velocity, time=time_since_last))
    track.append(Message('note_off', note=note, velocity=velocity, time=duration))

# 3. THE MELODY: "The Outlaw's Return" (Key: A Minor)
# Each 120 ticks = one 16th note. 
# We are combining the melody notes with lower "roll" notes for a full sound.

# --- BAR 1: The Entrance ---
add_note(57, 120, 110) # A3 (Main Melody)
add_note(60, 120, 80)  # C4 (Roll)
add_note(62, 120, 85)  # D4 (Roll)
add_note(63, 60, 95)   # D#4 (Quick Slide)
add_note(64, 180, 105) # E4 (Resolve)

# --- BAR 2: The High Tension ---
add_note(69, 480, 115) # A4 (High Hero Note)
add_note(67, 240, 90)  # G4
add_note(64, 240, 85)  # E4

# --- BAR 3: The Descending Run ---
add_note(60, 120, 95)  # C4
add_note(59, 120, 90)  # B3
add_note(57, 120, 100) # A3
add_note(55, 120, 85)  # G3
add_note(53, 120, 80)  # F3

# --- BAR 4: The Spanish Turnaround (E Major) ---
add_note(52, 120, 110, time_since_last=120) # E3 (Low hit)
add_note(56, 120, 95)  # G#3 (The "Sting" note)
add_note(59, 120, 90)  # B3
add_note(56, 120, 85)  # G#3
add_note(57, 480, 127) # A3 (Final Slam)

# 4. Save the file
filename = 'outlaw_banjo_complete.mid'
mid.save(filename)
print(f"Success! '{filename}' has been created.")
print("Check the file list on the left in Replit to download it.")