import random
import rtmidi_python as rtmidi
from pythonosc import udp_client
import gestures
import time
import helper

SHIMON_IP = "169.254.251.148"
OWN_IP = "127.0.0.1"
MUSIC_PORT = 51973
GESTURE_PORT = 3002
#pedal inputs are : 48, 50, 52, 53
#mididata 60 60
#velocity between 0 - 127

clientmusic = udp_client.SimpleUDPClient(SHIMON_IP, MUSIC_PORT)
clientGest = udp_client.SimpleUDPClient(OWN_IP, GESTURE_PORT)

one = 48
two = 50
three = 52
four = 53

###############################LEVELS############################################
def start():
    print("start")
    tutorial()

def tutorial():
    correct = False
    while not correct:
        time.sleep(2)
        playNotes([72])
        count = 0
        userPlayed = []
        while count < 2:
            message, delta_time = midi_in.get_message()
            if message:
                count += 1
                if count % 2 == 1:
                    userPlayed.append(message[1])
                    if message[1] == 48:
                        playNotes([72])
                    if message[1] == 50:
                        playNotes([74])
                    if message[1] == 52:
                        playNotes([76])
                    if message[1] == 53:
                        playNotes([77])
                    time.sleep(.5)
        if userPlayed == [48]: # 1,2,3,4 is just placeholder I don't know what message actually looks like
            correctGesture()
            correct = True
        else:
            wrongGesture()
    correct = False
        while not correct:
        time.sleep(2)
        playNotes([72, 74])
        count = 0
        userPlayed = []
        while count < 4:
            message, delta_time = midi_in.get_message()
            if message:
                count += 1
                if count % 2 == 1:
                    userPlayed.append(message[1])
                    if message[1] == 48:
                        playNotes([72])
                    if message[1] == 50:
                        playNotes([74])
                    if message[1] == 52:
                        playNotes([76])
                    if message[1] == 53:
                        playNotes([77])
                    time.sleep(.5)
        if userPlayed == [48, 50]: # 1,2,3,4 is just placeholder I don't know what message actually looks like
            correctGesture()
            correct = True
        else:
            wrongGesture()
    correct = False
        while not correct:
        time.sleep(2)
        playNotes([72,74,76])
        count = 0
        userPlayed = []
        while count < 6:
            message, delta_time = midi_in.get_message()
            if message:
                count += 1
                if count % 2 == 1:
                    userPlayed.append(message[1])
                    if message[1] == 48:
                        playNotes([72])
                    if message[1] == 50:
                        playNotes([74])
                    if message[1] == 52:
                        playNotes([76])
                    if message[1] == 53:
                        playNotes([77])
                    time.sleep(.5)
        if userPlayed == [48, 50, 52]: # 1,2,3,4 is just placeholder I don't know what message actually looks like
            correctGesture()
            correct = True
        else:
            wrongGesture()
    correct = False
    while not correct:
        time.sleep(2)
        playNotes([72,74,76,77])
        count = 0
        userPlayed = []
        while count < 8:
            message, delta_time = midi_in.get_message()
            if message:
                count += 1
                if count % 2 == 1:
                    userPlayed.append(message[1])
                    if message[1] == 48:
                        playNotes([72])
                    if message[1] == 50:
                        playNotes([74])
                    if message[1] == 52:
                        playNotes([76])
                    if message[1] == 53:
                        playNotes([77])
                    time.sleep(.5)
        if userPlayed == [48,50,52,53]: # 1,2,3,4 is just placeholder I don't know what message actually looks like
            correctGesture()
            correct = True
        else:
            wrongGesture()
    print("finished tuturial, starting level 1")
    level1()

def level1():
    notes = chooseNotes(70,80)
    score = returnNotes(notes, 2)
    size = len(score)
    mod = getMod(notes, score)
    correct = False
    while not correct:
        userPlayed = []
        count = 0
        playNotes(score)
        while count < size * 2:
            message, delta_time = midi_in.get_message()
            if message:
                count += 1
                if count % 2 == 1:
                    userPlayed.append(message[1])
                    notePressed = message[1]
                    if notePressed == one:
                        playNotes([notes[0]])
                    if notePressed == two:
                        playNotes([notes[1]])
                    if notePressed == three:
                        playNotes([notes[2]])
                    if notePressed == four:
                        playNotes([notes[3]])
        if userPlayed == mod:
            correctGesture()
            correct = True
        else:
            wrongGesture()
    print("Finished level 1, moving on to level2")
    level2()

def level2():
    notes = chooseNotes(70,80)
    score = returnNotes(notes, 4)
    size = len(score)
    mod = getMod(notes, score)
    correct = False
    while not correct:
        playNotes(score)
        userPlayed = []
        count = 0
        while count < size * 2:
            message, delta_time = midi_in.get_message()
            if message:
                count += 1
                if count % 2 == 1:
                    userPlayed.append(message[1])
                    notePressed = message[1]
                    if notePressed == one:
                        playNotes([notes[0]])
                    if notePressed == two:
                        playNotes([notes[1]])
                    if notePressed == three:
                        playNotes([notes[2]])
                    if notePressed == four:
                        playNotes([notes[3]])
        if userPlayed == mod:
            correctGesture()
            correct = True
        else:
            wrongGesture()
    print("Finished level 2, moving on to level3")
    level3()

def level3():
    notes = chooseNotes(70,80)
    score = returnNotes(notes, 6)
    size = len(score)
    mod = getMod(notes, score)
    correct = False
    while not correct:
        userPlayed = []
        count = 0
        playNotes(score)
        while count < size * 2:
            message, delta_time = midi_in.get_message()
            if message:
                count += 1
                if count % 2 == 1:
                    userPlayed.append(message[1])
                    notePressed = message[1]
                    if notePressed == one:
                        playNotes([notes[0]])
                    if notePressed == two:
                        playNotes([notes[1]])
                    if notePressed == three:
                        playNotes([notes[2]])
                    if notePressed == four:
                        playNotes([notes[3]])
        if userPlayed == mod:
            correctGesture()
            correct = True
        else:
            wrongGesture()
    print("Finished level3. You win!")


#########################################MAIN METHOD########################
midi_in = rtmidi.MidiIn(b"input")
midi_in.open_port(0)
start()
