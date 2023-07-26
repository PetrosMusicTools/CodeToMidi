import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
from tkinter import ttk
from mido import MidiFile, MidiTrack, Message, MetaMessage
import os

# Define MIDI instruments
instruments = {
    "Acoustic Grand Piano": 0,
    "Bright Acoustic Piano": 1,
    "Electric Grand Piano": 2,
    "Honky-tonk Piano": 3,
    "Electric Piano 1": 4,
    "Electric Piano 2": 5,
    "Harpsichord": 6,
    "Clavinet": 7,
    "Celesta": 8,
    "Glockenspiel": 9,
    "Music Box": 10,
    "Vibraphone": 11,
    "Marimba": 12,
    "Xylophone": 13,
    "Tubular Bells": 14,
    "Dulcimer": 15,
    "Drawbar Organ": 16,
    "Percussive Organ": 17,
    "Rock Organ": 18,
    "Church Organ": 19,
    "Reed Organ": 20,
    "Accordion": 21,
    "Harmonica": 22,
    "Tango Accordion": 23,
    "Acoustic Guitar (nylon)": 24,
    "Acoustic Guitar (steel)": 25,
    "Electric Guitar (jazz)": 26,
    "Electric Guitar (clean)": 27,
    "Electric Guitar (muted)": 28,
    "Overdriven Guitar": 29,
    "Distortion Guitar": 30,
    "Guitar Harmonics": 31,
    "Acoustic Bass": 32,
    "Electric Bass (finger)": 33,
    "Electric Bass (pick)": 34,
    "Fretless Bass": 35,
    "Slap Bass 1": 36,
    "Slap Bass 2": 37,
    "Synth Bass 1": 38,
    "Synth Bass 2": 39,
    "Violin": 40,
    "Viola": 41,
    "Cello": 42,
    "Contrabass": 43,
    "Tremolo Strings": 44,
    "Pizzicato Strings": 45,
    "Orchestral Harp": 46,
    "Timpani": 47,
    "String Ensemble 1": 48,
    "String Ensemble 2": 49,
    "Synth Strings 1": 50,
    "Synth Strings 2": 51,
    "Choir Aahs": 52,
    "Voice Oohs": 53,
    "Synth Voice": 54,
    "Orchestra Hit": 55,
    "Trumpet": 56,
    "Trombone": 57,
    "Tuba": 58,
    "Muted Trumpet": 59,
    "French Horn": 60,
    "Brass Section": 61,
    "Synth Brass 1": 62,
    "Synth Brass 2": 63,
    "Soprano Sax": 64,
    "Alto Sax": 65,
    "Tenor Sax": 66,
    "Baritone Sax": 67,
    "Oboe": 68,
    "English Horn": 69,
    "Bassoon": 70,
    "Clarinet": 71,
    "Piccolo": 72,
    "Flute": 73,
    "Recorder": 74,
    "Pan Flute": 75,
    "Bottle Blow": 76,
    "Shakuhachi": 77,
    "Whistle": 78,
    "Ocarina": 79,
    "Square Lead": 80,
    "Saw Lead": 81,
    "Calliope Lead": 82,
    "Chiff Lead": 83,
    "Charang Lead": 84,
    "Voice Lead": 85,
    "Fifths Lead": 86,
    "Bass + Lead": 87,
    "New Age Pad": 88,
    "Warm Pad": 89,
    "Polysynth Pad": 90,
    "Choir Pad": 91,
    "Bowed Pad": 92,
    "Metallic Pad": 93,
    "Halo Pad": 94,
    "Sweep Pad": 95,
    "Rain Sound": 96,
    "Soundtrack": 97,
    "Crystal Sound": 98,
    "Atmosphere": 99,
    "Brightness": 100,
    "Goblins": 101,
    "Echo Drops": 102,
    "Star Theme": 103,
    "Sitar": 104,
    "Banjo": 105,
    "Shamisen": 106,
    "Koto": 107,
    "Kalimba": 108,
    "Bagpipe": 109,
    "Fiddle": 110,
    "Shanai": 111,
    "Tinkle Bell": 112,
    "Agogo": 113,
    "Steel Drums": 114,
    "Woodblock": 115,
    "Taiko Drum": 116,
    "Melodic Tom": 117,
    "Synth Drum": 118,
    "Reverse Cymbal": 119,
    "Guitar Fret Noise": 120,
    "Breath Noise": 121,
    "Seashore": 122,
    "Bird Tweet": 123,
    "Telephone Ring": 124,
    "Helicopter": 125,
    "Applause": 126,
    "Gunshot": 127,


    # Your instruments here
    # ...
}

def create_midi():
    melody = eval(txt.get('1.0', 'end-1c'))  # Retrieve the text from the text widget
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    # Select instrument
    instrument_name = combo.get()
    instrument_code = instruments[instrument_name]
    track.append(Message('program_change', program=instrument_code, time=0))

    # Set tempo
    user_tempo = float(tempo_entry.get())
    track.append(MetaMessage('set_tempo', tempo=int(60000000 / user_tempo)))

    for note, duration in melody:
        track.append(Message('note_on', note=note, velocity=64, time=0))
        track.append(Message('note_off', note=note, velocity=64, time=int(duration * 480)))

    filename = filename_entry.get()
    if filename == "":
        filename = "new_song"
    
    # Use filedialog to select directory
    directory = filedialog.askdirectory()
    filepath = os.path.join(directory, f'{filename}.mid')
    
    try:
        mid.save(filepath)
        messagebox.showinfo("Success", f"Congrats, your midi file {filename}.mid is ready at {directory}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while creating the MIDI file: {e}")

window = tk.Tk()
window.title("MIDI Creator")

# Change the background color of the window
window.configure(bg='lightblue')

label_instrument = tk.Label(window, text = "Choose instrument:", bg='lightblue')
label_instrument.pack()

combo = ttk.Combobox(window, values=list(instruments.keys()))
combo.pack()

tempo_label = tk.Label(window, text="Enter tempo (bpm):", bg='lightblue')
tempo_label.pack()

tempo_entry = tk.Entry(window)
tempo_entry.pack()

filename_label = tk.Label(window, text="Enter filename:", bg='lightblue')
filename_label.pack()

filename_entry = tk.Entry(window)
filename_entry.pack()

txt = scrolledtext.ScrolledText(window, width=60, height=10)
txt.pack()

btn = tk.Button(window, text="Create MIDI", command=create_midi)
btn.pack()

window.mainloop()
