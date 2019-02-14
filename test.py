import rtmidi_python as rtmidi

midi_in = rtmidi.MidiIn(b"input")
midi_in.open_port(0)
print("start")
while True:
    message, delta_time = midi_in.get_message()
    if message:
        print(message, delta_time)