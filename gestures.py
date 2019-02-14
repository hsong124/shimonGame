'''
Gestures file for shimon in python
Heather
'''
def headShakeGood():
    messages = []
    messages.append("/head-commands HEADTILT 0.2 20.")
    messages.append("/head-commands HEADTILT 0.8 20.")
    messages.append("/head-commands HEADTILT 1.2 20.")
    messages.append("/head-commands HEADTILT 0.8 20.")
    messages.append("/head-commands HEADTILT 1.2 20.")
    return messages

def headShakeBad():
    messages = []
    messages.append("/head-commands HEADTILT 1. 20.")
    messages.append("/head-commands NECKPAN1 -1. 10.")
    messages.append("/head-commands NECKPAN1 -.5 10.")
    messages.append("/head-commands NECKPAN1 -1. 10.")
    messages.append("/head-commands NECKPAN1 -.5 10.")
    messages.append("/head-commands NECKPAN1 -1. 10.")
    messages.append("/head-commands NECKPAN1 -.5 10.")
    return messages