from random import randint
from time import sleep

file = open("guessinggame.txt","rt")
scores = file.read()
file.close()

score = 100

input("Welcome to the Guessing Game! [press enter to continue]")
input(scores)
input("How To Play:\nThe program will generate a random 4 digit number, which you will need to guess.\nYou lose 5 points for every incorrect guess.")
input("Select a mode:")
input(" - Easy mode will tell you which position you guessed correctly.\n - Normal mode will tell you how many numbers you got correct, without telling you the position.\n - Hard mode will generate a 5 digit number instead of 4.")

done = False
while not done:
    sleep(1)
    try:
        mode = int(input("Type 1 for easy mode\nType 2 for normal mode\nType 3 for hard mode\n"))
        if mode == 1:
            print("Easy mode selected!")
            num = randint(1000,9999)
            done = True
        elif mode == 2:
            print("Normal mode selected!")
            num = randint(1000,9999)
            done = True
        elif mode == 3:
            print("Hard mode selected!")
            num = randint(10000,99999)
            done = True
        else:
            print("Invalid input, try again.")
    except:
        print("Invalid input, try again.")

print("The number has been generated.")

def easyMode(n, s):
    playing = True
    while playing:
        chosen = False
        correctNums = []
        while not chosen:
            sleep(1)
            try:
                g = int(input("Enter your guess: "))
                if g == n:
                    print("Correct!")
                    return s
                    playing = False
                    chosen = True
                elif (len(str(g))) != 4:
                    print("Input is not 4 digits.")
                else:
                    chosen = True
            except:
                print("Invalid input, try again")
        value = [i for i in str(n)]

        for i in range(len(str(g))):
            if str(g)[i] == str(num)[i]:
                correctNums.append(str(g)[i])
            else:
                s -= 5
                correctNums.append("_")
        print("".join(correctNums))        

def normalMode(n, s):
    playing = True
    while playing:
        chosen = False
        correctNums = []
        while not chosen:
            sleep(1)
            try:
                g = int(input("Enter your guess: "))
                if g == n:
                    print("Correct!")
                    return s
                    playing = False
                    chosen = True
                elif (len(str(g))) != 4:
                    print("Input is not 4 digits.")
                else:
                    chosen = True
            except:
                print("Invalid input, try again")

        value = [i for i in str(n)]
        count = 0
        for i in range(len(value)):
            if value[i] == str(g)[i]:
                count += 1

        print(f"{count} numbers were guessed correctly.")

def hardMode(n, s):
    playing = True
    while playing:
        chosen = False
        correctNums = []
        while not chosen:
            sleep(1)
            try:
                g = int(input("Enter your guess: "))
                if g == n:
                    print("Correct!")
                    return s
                    playing = False
                    chosen = True
                elif (len(str(g))) != 5:
                    print("Input is not 5 digits.")
                else:
                    chosen = True
            except:
                print("Invalid input, try again")
    
if mode == 1:
    thing = easyMode(num, score)
elif mode == 2:
    thing = normalMode(num, score)
else:
    hardMode(num, score)

print(f"Score = {thing}")
name = input("What is your name?\n")
file = open("guessinggame.txt", "wt")
if thing > 80:
    file.write(f"\nHIGH SCORES:\n1. {name.upper()}: {thing}\n2. JACK: 80\n3. MIKE: 50\n")
    file.close()
elif thing > 50:
    file.write(f"\nHIGH SCORES:\n1. JACK: 80\n2. {name.upper()}: {thing}\n3. MIKE: 50\n")
    file.close()
else:
    file.write(f"\nHIGH SCORES:\n1. JACK: 80\n2. MIKE: 50\n3. {name.upper()}: {thing}\n")
    file.close()