import random
import time

cont = 1

while cont == 1:
    dots = "."
    listofdice = []

    numdice = int(input("How many dice do you want to roll?\n"))

    def animation():  
        n = 0

        while n < 12: #number of dots in animation
            print(dots * int(n))
            time.sleep(.05)
            n = n+1

        while n > 0:
            print(dots * int(n))
            time.sleep(.05)
            n = n-1

    #calling functions

    animation()

    while numdice > 0:
        die = random.randint(1,6)
        listofdice.append(die)
        numdice = numdice - 1

    time.sleep(.5)   
    print("\n") 
    print(listofdice)
    dicenum = len(listofdice) #number of dice inside the list

    if dicenum > 1:
        time.sleep(.75)
        print("TOTAL : " + str(sum(listofdice)))
        time.sleep(.75)
    
    print("---")
    playAgain = str(input("Roll again? \n"))
    
    affirmative = ["yes", "Yes", "y", "Y"]
    if playAgain in affirmative:
        continue
    else:
        cont = cont - 1







