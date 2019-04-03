import random
import rtmidi_python as rtmidi
from pythonosc import udp_client
import gestures
import time
#remake gestures in python
#test connection with shimon
SHIMON_IP = "169.254.251.148"
OWN_IP = "127.0.0.1"
MUSIC_PORT = 51973
GESTURE_PORT = 3002
#pedal inputs are : 48, 50, 52, 53
#mididata 60 60
#velocity between 0 - 127


clientmusic = udp_client.SimpleUDPClient(SHIMON_IP, MUSIC_PORT)
clientGest = udp_client.SimpleUDPClient(OWN_IP, GESTURE_PORT)

def start():
    print("start")
    tutorial()

def tutorial():
    correct = False
    while not correct:
        test = input()
        if test == "correct":
            correctGesture()
        elif test == "wrong":
            wrongGesture()
        elif test == "play":
            playNotes([72])
        else:
            print("enter correct, wrong, or play")
    print("finished tuturial")


#######################################################################
def level1():
    #have to pass 3 times to get to level 2
    for j in range(3):
        #add 4 random notes
        for i in range(4):
            notes = []
            notes.append(random.randint(1, 12))
        correct = False
        while not correct:
            #here shimon should play notes and then wait for input
            if user == notes:
                correctGesture()
                correct = True
            else:
                wrongGesture()

    level2()

def level2():
    print("not done")
#######################################################################
'''
Method where shimon plays notes, e.g. C, E, G, C
Takes in array of numbers(notes)
'''
def playNotes(arr):
    for note in arr:
        clientmusic.send_message("/mididata", [note,  110])
        time.sleep(.5)
    print("Shimon played notes:", arr)

'''
Method that makes shimon do the gesture indicating correct notes by the player
'''
def correctGesture():
    clientGest.send_message("0", "good")
    print("shimon does good gesture")


'''
Method that makes shimon do the gesture indicating incorrect notes by the player
'''
def wrongGesture():
    clientGest.send_message("1", "bad")
    print("shimon does bad gesture")



midi_in = rtmidi.MidiIn(b"input")
midi_in.open_port(0)
start()
