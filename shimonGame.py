import random
import rtmidi_python as rtmidi
from pythonosc import udp_client
import gestures
import time
#remake gestures in python
#test connection with shimon


SHIMON_IP = "169.254.251.148"
GESTURE_PORT = 30310
MUSIC_PORT = 51973
#pedal inputs are : 48, 50, 52, 53
#mididata 60 60
#velocity between 0 - 127


clientmusic = udp_client.SimpleUDPClient(SHIMON_IP, MUSIC_PORT)
clientGest = udp_client.SimpleUDPClient(SHIMON_IP, GESTURE_PORT)
def start():
    print("start")
    tutorial()

def tutorial():
    correct = False
    while not correct:
        time.sleep(4)
        playNotes([60,62,64,65])
        count = 0
        userPlayed = []
        while count < 8:
            message, delta_time = midi_in.get_message()
            if message:
                count += 1
                if count % 2 == 1:
                    userPlayed.append(message[1])
                    if message[1] == 48:
                        playNotes([60])
                    if message[1] == 50:
                        playNotes([62])
                    if message[1] == 42:
                        playNotes([64])
                    if message[1] == 53:
                        playNotes([65])
                    print(message[1])
                    time.sleep(1)
        if userPlayed == [48,50,52,53]: # 1,2,3,4 is just placeholder I don't know what message actually looks like
            correctGesture()
            correct = True
        else:
            wrongGesture()
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
        #sock.sendto(bytes("/mididata " + str(note) + " 110", "utf-8"), (SHIMON_IP , MUSIC_PORT))
        time.sleep(1)
    print("Shimon played notes:", arr)

'''
Method that makes shimon do the gesture indicating correct notes by the player
'''
def correctGesture():
    message = gestures.headShakeGood()
    for part in message:
        filter1 = "/head-commands " + part[0]
        clientmusic.send_message(filter1, part[1:])
    print("shimon does good gesture")


'''
Method that makes shimon do the gesture indicating incorrect notes by the player
'''
def wrongGesture():
    message = gestures.headShakeBad()
    for part in message:
        filter1 = "/head-commands " + part[0]
        clientmusic.send_message(filter1, part[1:])
        time.sleep(1)
    print("shimon does bad gesture")



midi_in = rtmidi.MidiIn(b"input")
midi_in.open_port(0)
start()
