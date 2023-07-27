# Code to MIDI Creator

## Overview

Code to MIDI Creator is an innovative application that turns Python code into MIDI files. Users can create melodies by entering a sequence of musical notes and their durations. 

## Features

- Converts Python code into MIDI files.
- Offers a broad range of musical instruments.
- Features an easy-to-use, intuitive GUI.
- Generates MIDI files efficiently.

## How to Use

1. Download the `.exe` file from the repository.
2. Run the executable on your machine.
3. Select your desired instrument from the drop-down menu.
4. Enter the note sequence and their durations in the text box provided. The format should be as follows: `[(note1, duration1), (note2, duration2), ...]`. 
5. Click the "Create MIDI" button. You will be prompted to enter a filename and choose a directory where the file will be saved.
6. The program will convert your code into a MIDI file and save it in the chosen directory. A success message will confirm that your MIDI file has been created successfully.


## MIDI Code Explanation

In this application, we're representing MIDI (Musical Instrument Digital Interface) notes as a tuple containing three elements. This tuple represents a single note event in the MIDI sequence.

- The first element in the tuple, Pitch, is a MIDI note number. The MIDI protocol specifies that note numbers 0-127 correspond to pitches, where 60 represents Middle C on a standard piano. The note numbers ascend chromatically, so 61 is a C#, 62 is a D, and so on.

- The second element in the tuple, Velocity, represents the volume at which the note is played. This is also on a scale from 0 to 127, where 0 represents silence and 127 represents the loudest possible note. This allows for dynamic expression in the music.

- The third element in the tuple, Duration, represents how long the note is held, measured in beats. A duration of 1.0 is one beat, 0.5 is a half beat, 2.0 is two beats, and so on.

So, a tuple like `(60, 100, 1.0)` would correspond to the note Middle C, played fairly loud (as the velocity is 100), for the duration of one beat.

Here's how a simple C Major scale would be represented:

```python
midi_data = [
    (60, 100, 1.0),  # C
    (62, 100, 1.0),  # D
    (64, 100, 1.0),  # E
    (65, 100, 1.0),  # F
    (67, 100, 1.0),  # G
    (69, 100, 1.0),  # A
    (71, 100, 1.0),  # B
    (72, 100, 2.0),  # C
]

## License

This project is licensed under the terms of the MIT License.
