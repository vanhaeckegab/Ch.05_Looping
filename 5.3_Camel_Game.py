'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
import time

q = False
m = int(15)  # minutes remaining
direction = 0  # weather or not you have directions, += 2 everytime you get directions and -=1 if you find a corridor
rr = 20  # The remaining rooms you have to go through, find a good number that doesn't make it too easy or difficult
tb = False
tbm = False

print("Welcome to the poop games! \n By: Gabe Van Haecke \n")
inst = str(input("Would you like instructions? y/n "))
if inst == "y" or inst == "yes":
    print('''
    The plot is simple, you are a man in a meeting who realizes he really need to take a dump. In just 15 minutes you 
    need to make it to the bathroom in an unfamiliar place. Through a text menu make decisions that will help you reach 
    your goal of answering natures call. Each minute you will be able to select from 5 different options.

        A). Walk at a moderate speed (Goes at a normal pace but may not be fast enough)
        B). Run at a fast pace (Walks faster but risks decreasing your time)
        C). Get directions (Ask around for instructions, takes a minute but stops you from getting lost.)
        D). Grab a bible and pray (Sometimes all you can do is pray)
        E). Give in to natures calling (quit)
        
    Along the way, fate will may not be so kind to you, a taco bell dinner from the night before or an unmarked
    intersection could be your downfall. 
    
    Good luck, don't soil your pants.
    ''')
else:
    pass
while not q:
    time.sleep(1)
    if m <= 0:
        print("Unfortunately your time is up, you fall to your knees as the poop fills your pants. You couldn't make it"
              " this time, but tomorrow is another day.")
        break
    if rr == 0:
        print("Congratulations, you did it. You sit on the toilet and have the best time relieving yourself ever.")
        break
    m = round(m)
    print("it feels as if you have", m, "minutes left, what will you do?")

    print('''
A). Walk at a moderate speed
B). Run at a fast pace
C). Get directions
D). Grab a bible and pray
E). Give in to natures calling
    ''')
    if m <= 10:
        if not tb:
            if random.randint(1, 15) == 1:
                time.sleep(1)
                print("Uh oh")
                time.sleep(.5)
                print("*grumble*")
                time.sleep(.25)
                print("In your hurry, a memory of the previous night comes to haunt you. The Taco Bell you had the "
                      "previous night is not going to stay down as well as you thought. \n")
                m /= 2
                tb = True
                tbm = True
                continue
    choice = input("- ")
    if choice.upper() == "A" or choice.upper() == "B" or choice.lower() == "walk" or choice.lower() == "run":
        if direction == 0:
            if random.randint(1, 4) == 3:
                rr += 1
                c = random.randint(2, 4)
                print("you run into a corridor that opens into", c, "different pathways. Which corridor "
                                                                    "would you like to take? \n")
                print("( pick a number 1 through", c, ")")
                cc = input("- ")
                if cc == random.randint(1, c):
                    print("You sprint down the corridor, continuing your journey to reach the royal throne. \n")
                    rr += 2
                else:
                    print("The corridor you go down leads to nothing, you manage to backtrack but it takes a minute.\n")
                    m -= 1
        else:
            direction -= 1
        if choice.upper() == "A" or choice.lower() == "walk":  # If they choose run
            rr -= 1
            if random.randint(1, 5) == 1:
                print("Walking at normal pace you don't even feel any increase in urgency.\n")
            else:
                print("Not wanting to take the chance of it falling out as you run, you walk at a leisurely pace. \n")
                m -= 1
        else:  # If they choose run
            rr -= 3
            m -= random.randint(1, 2)
            print("Throwing caution into the wind, you race down the halls, caring more about speed carefulness.\n")
    elif choice.upper() == "C" or choice.lower() == "get directions":
        m -= 1
        p = random.randint(1, 1000)
        if p in range(1, 500):
            print("No luck, no one is around\n")
        elif p in range(500, 990):
            if random.randint(1, 2) == 1:
                print("You find a nice woman who gives you a lot of directions but you only actually catch some of it. "
                      "Back to running for your dignity\n")
            else:
                print("While asking around a man vaguely points down the hall then to the left, "
                      "it's not much but it's something.\n")
        elif p in range(990, 1000):
            print("You come across an elderly woman, but in trying to explain the situation you realise that he has no "
                  "clue where he is. Losing hope in the older generation, you move on.\n")
        else:
            print("An old man hobbles over to you. Without a word he hands you a wooden sword. You don't see any use to"
                  " this gift but you take it graciously.\n")
        direction += 2
    elif choice.upper() == "D" or choice.lower() == "pray" or choice.lower() == "bible":
        print("You reach into you pocket for your trusty pocket  bible, it's never failed you before, hopefully it'll"
              " help now.\n")
        if random.randint(1, 6969696969) == 69:
            print("The lord has taken pity on you and gave you a blessing. You no longer feel the need to relieve"
                  " yourself, thanks to the blessing from the lord you win!\n")
            break
        if tbm:
            if random.randint(1, 10) <= 6:
                print("As you put your hand on the bible you are filled with heavenly power. The effects of last nights"
                      " burrito adventure are reversed\n")
                tbm = False
                m *= 2
                m += 1
            else:
                print("The lord must be taking a different call right now, nothing happens and you continue onward.\n")
        else:
            if random.randint(1, 20) == 4:
                print("The lord sees you in pain and decides to ease your struggle.\n")
                m += 6
            else:
                print("You search for the holy one in your heart but feel nothing.")
        m -= 1
    elif choice.upper() == "E" or choice.lower() == "quit":
        print("You stand there in embarrassment as you choose to give up and willingly poop your pants.\n")
        q = True
    elif choice == "52":
        print("m =", m)
        print("rr = ", rr)
    else:
        print("please choose from one of the options \n")
print("goodbye")
