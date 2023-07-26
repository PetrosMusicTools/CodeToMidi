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

## Example

Here's a simple example of how you might use this application:

[(60, 0.25), (62, 0.25), (64, 0.5), (62, 0.5), (60, 0.5), (60, 0.5)]

scss
Copy code

This will create a MIDI file with the notes middle C (60) and D (62) played for a quarter beat, E (64) played for half a beat, D (62) played for half a beat, and finally middle C (60) played for a full beat.

## License

This project is licensed under the terms of the MIT License.
