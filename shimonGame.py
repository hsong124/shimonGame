import random
import rtmidi_python as rtmidi_python
import socket


GESTURE_IP = "169.254.251.148"
GESTURE_PORT = 30310


midi_in = rtmidi.MidiIn()
start(midi_in)

def start(midi_in):
    midi_in.open_port(0)
    print("initial shimon gesture")



def tutorial():
    correct = False
    while not correct:
        playNotes([1,2,3,4])
        count = 0
        userPlayed = []
        while count < 4:
            message, delta_time = midi_in.get_message()
            if message:
                count += 1
                userPlayed.append(message)
                #send message to shimon to play
        if userPlayed == [1,2,3,4]: # 1,2,3,4 is just placeholder I don't know what message actually looks like
            correctGesture()
            correct = True
        else:
            wrongGesture()
    level1()


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
    pass

'''
Method that makes shimon do the gesture indicating correct notes by the player
'''
def correctGesture():
    pass

'''
Method that makes shimon do the gesture indicating incorrect notes by the player
'''
def wrongGesture():
    pass