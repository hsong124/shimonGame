##########################Helper methods####################################
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
    time.sleep(3)
    print("shimon does good gesture")


'''
Method that makes shimon do the gesture indicating incorrect notes by the player
'''
def wrongGesture():
    clientGest.send_message("1", "bad")
    time.sleep(3)
    print("shimon does bad gesture")

def chooseNotes(lower, upper):
    notes = []
    for i in range(4):
        note = random.randint(lower, upper)
        while note in notes:
            note = random.randint(lower, upper)
        notes.append(note)
    notes.sort()
    return notes

def returnNotes(notes, length):
    score = []
    for i in range(length):
        j = random.randint(0,3)
        score.append(notes[j])
    for note in notes:
        if note not in score:
            score.append(note)
    return score

def getMod(notes, score):
    first = notes[0]
    second = notes[1]
    third = notes[2]
    fourth = notes[3]
    mod = []
    for note in score:
        if note == first:
            mod.append(one)
        elif note == second:
            mod.append(two)
        elif note == third:
            mod.append(three)
        elif note == fourth:
            mod.append(four)
    return mod