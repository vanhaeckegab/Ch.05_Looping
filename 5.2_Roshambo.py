'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''
import random
import time
# g keeps the game running, w is user wins, cw is com wins, t is total games
g = False
h = False
w = 0
cw = 0
t = 0
while not h:
    p = input("do you want to play rock paper scissors? ")
    if p.lower() == "yes" or p.lower() == "y":
        h = True
    # If they want to stop
    elif p.lower() == "no" or p.lower() == "n":
        print("ok then")
        g = True
        h = True
    else:
        print("please answer yes or no")
while not g:
    # If they do want to play.
    rps = input("choose rock, paper, or scissors (1=rock, 2=paper, 3=scissors) or 4 to quit ")
    if rps == "1" or rps == "rock" or rps == "r":
        rps = int(1)
    elif rps == "2" or rps == "paper" or rps == "p":
        rps = int(2)
    elif rps == "3" or rps == "scissors" or rps == "s":
        rps = int(3)
    elif rps == "4" or rps == "quit" or rps == "q":
        g = True
    else:
        print("please choose rock, paper, or scissors, unless you wanna quit")
    if rps in range(1, 4):
        com = random.randint(1, 3)
        time.sleep(.5)
        print("rock")
        time.sleep(1)
        print("paper")
        time.sleep(1)
        print("scissors")
        time.sleep(.5)
        print("shoot")
        time.sleep(.25)
        if com == 3:
            print("Computer: Scissors")
        elif com == 2:
            print("Computer: Paper")
        else:
            print("Computer: Rock")
# all the IF statements to determine victor
        if rps == com:
            print("it was a tie")
            t += 1
        elif (rps == 1 or com == 1) and (rps == 2 or com == 2):
            if rps > com:
                print("Paper cover rock, you win!")
                w += 1
            else:
                print("I'm sorry to inform you that paper covers rock, you lose")
                cw += 1
            t += 1
        elif (rps == 2 or com == 2) and (rps == 3 or com == 3):
            if rps > com:
                print("Scissors cuts paper, you win!")
                w += 1
            else:
                print("I'm sorry to inform you that scissors cuts paper, you lose")
                cw += 1
            t += 1
        else:
            if rps < com:
                print("Rock smashes scissors, you win!")
                w += 1
            else:
                print("I'm sorry to inform you that rock smashes scissors, you lose")
                cw += 1
            t += 1
print("You played", t, "games and won", w, "of the those. Unfortunately, you lost", cw, "times and tied",
      t-w-cw, "times")
print("good bye")
