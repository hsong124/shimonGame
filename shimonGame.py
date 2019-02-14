import random
import rtmidi_python as rtmidi
import socket
import gestures

#remake gestures in python
#test connection with shimon


SHIMON_IP = "169.254.251.148"
GESTURE_PORT = 30310
MUSIC_PORT = 51973
#pedal inputs are : 48, 50, 52, 53
#mididata 60 60
#velocity between 0 - 127
print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

def start():
    print("initial shimon gesture")
    tutorial()

def tutorial():
    correct = False
    while not correct:
        playNotes([60,61,62,63])
        count = 0
        userPlayed = []
        while count < 8:
            message, delta_time = midi_in.get_message()
            if message:
                count += 1
                if count % 2 == 1:
                    userPlayed.append(message[1])
                    print(message[1])
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
    #need to check if valid arr
    sock.sendto(bytes(arr, "utf-8"), (SHIMON_IP , MUSIC_PORT))
    print("Shimon played notes:", arr)

'''
Method that makes shimon do the gesture indicating correct notes by the player
'''
def correctGesture(sock):
    message = gestures.headShakegood()
    sock.sendto(bytes(arr, "utf-8"), (SHIMON_IP , GESTURE_PORT))
    print("shimon does good gesture")


'''
Method that makes shimon do the gesture indicating incorrect notes by the player
'''
def wrongGesture():
    print("shimon does bad gesture")


print("start")
midi_in = rtmidi.MidiIn(b"input")
midi_in.open_port(0)
start()
