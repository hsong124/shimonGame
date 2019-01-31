import random




def start():
    print("initial shimon gesture")

def tutorial():
    correct = False
    while not correct:
        print("1, 2, 3, 4") #actually have shimon play here not print, placeholder
        #get user input here
        if user == [1,2,3,4]:
            print("correct gesture")
            correct = True
        else:
            print("wrong gesture")
    correct = False
    while not correct:
        print("4,3,2,1")
        #get user input here
        if user == [4,3,2,1]:
            print("correct gesture")
            correct = True
        else:
            print("wrong gesture")
    level1()

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
                print("correct gesture")
                correct = True
            else:
                print("wrong gesture")

    level2()

def level2():
    print("not done")


