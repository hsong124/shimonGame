

def start():
    print("initial shimon gesture")

def tutorial():
    correct = False
    while not correct:
        print("1, 2, 3, 4")
        #shimon listen
        if user == [1,2,3,4]:
            print("correct gesture")
            correct = True
        else:
            print("wrong gesture")
    correct = False
    while not correct:
        print("4,3,2,1")
        #shimon listen
        if user == [4,3,2,1]:
            print("correct gesture")
            correct = True
        else:
            print("wrong gesture")


