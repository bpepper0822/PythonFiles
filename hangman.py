import random, time

dots = "."
secretword = ''
cont = 1 #continue var

category = ["Household Objects", "Sports", "Foods", "Pokemon"]

cHousehold = ["Vacuum Cleaner", "Paper Towels", "Washing Machine", "Flashlight", "Microwave", "Coffee Table", "Trash Can", "Bookshelf", "Light Bulbs", "Laundry Hamper"]
cSports = ["Soccer Ball", "Touchdown", "Home Run", "First Down", "Outfield", "Ping Pong", "Pool Table", "Sidelines", "Curveball", "Hail Mary", "Quarterback", "Dribble", "Free Kick", "Goalkeeper", "Strike Three", "Overtime"]
cFoods = ["Cheeseburger", "Cheese Pizza", "Chicken Fingers", "Taco Salad", "Fries and Tots", "Chocolate Cake", "Chicken Fajita", "Pop Tarts", "Ice Cream Soup", "Oreo Blast", "Apple Fritter"]
cPokemon = ["Absol", "Aerodactyl", "Aggron", "Alakazam", "Arcanine", "Arceus", "Articuno", "Blastoise", "Blaziken", "Braviary", "Bulbasaur", "Celebi", "Charizard", "Charmander", "Charmeleon", "Cubone", "Cyndaquil", "Darkrai", "Deoxys", "Dialga", "Dragonair", "Dragonite", "Electabuzz", "Electivire", "Empoleon", "Entei", "Espeon", "Feraligatr", "Flareon", "Flygon", "Gabite", "Garchomp", "Gastly", "Gengar", "Giratina", "Glaceon", "Groudon", "Growlithe", "Gyarados", "Haunter", "Haxorus", "Hitmonlee", "Ho-Oh", "Houndoom", "Hydreigon", "Infernape", "Ivysaur", "Jolteon", "Kabutops", "Kadabra", "Kingdra", "Kyogre", "Kyurem", "Lapras", "Latias", "Latios", "Lucario", "Lugia", "Luxray", "Machamp", "Meganium", "Metagross", "Mew", "Mewtwo", "Milotic", "Moltres", "Nidoking", "Ninetales", "Onix", "Palkia", "Pidgeot", "Pikachu", "Quilava", "Raichu", "Raikou", "Rapidash", "Rayquaza", "Reshiram", "Rhydon", "Salamence", "Samurott", "Sceptile", "Scizor", "Scyther", "Serperior", "Snorlax", "Squirtle", "Steelix", "Suicune", "Swampert", "Torterra", "Typhlosion", "Tyranitar", "Umbreon", "Vaporeon", "Venusaur", "Wartortle", "Zapdos", "Zekrom", "Zoroark"]

randomCat = random.choice(category)
randomHouse = random.choice(cHousehold)
randomSport = random.choice(cSports)
randomFood = random.choice(cFoods)
randomPokemon = random.choice(cPokemon)

def animation():  
    n = 0

    while n < 50: #number of dots in animation
        print(dots * int(n))
        time.sleep(.03)
        n = n+1

    while n > 0:
        print(dots * int(n))
        time.sleep(.03)
        n = n-1

def randomize(): #provides secondary randomization when playing multiple games
    global randomCat, randomFood, randomHouse, randomPokemon, randomSport
    randomCat = random.choice(category)
    randomHouse = random.choice(cHousehold)
    randomSport = random.choice(cSports)
    randomFood = random.choice(cFoods)
    randomPokemon = random.choice(cPokemon)

def playFunction():
    turnsleft = 10
    guesses = ' '

    while turnsleft > 0:
        mystery = 0 #number of mystery letters left
        

        for char in secretword.casefold():
            if char in guesses.casefold():
                print(char, end = ' ')
            else:
                print("_", end =' ')
                mystery += 1
    
        if mystery == 0:
            print("\nCongratulations! You figured out the word!")
            break
        
        guess = input("\n\nGuess a letter\n")
        guesses += guess
        
        if guess not in secretword.casefold():
            turnsleft -= 1
            print("\n\n" + guess + " is not in the word.\n")
            print("You have " + str(turnsleft) + " guesses left. " + "Letters guessed: [" + guesses + " ]\n") #still need to prevent duplicate guesses
            #PLACE DRAWING HERE? IF 9, IF 8, IF 7...IF 1
            if turnsleft == 0:
                print("Sorry, you're out of guesses. The word was " + secretword + "!")
    
def onePlayer():
    global secretword
    if randomCat == "Household Objects":
        secretword = randomHouse
    elif randomCat == "Sports":
        secretword = randomSport
    elif randomCat == "Foods":
        secretword = randomFood
    elif randomCat == "Pokemon":
        secretword = randomPokemon
    
    playFunction()
    
def twoPlayer():
    global secretword
    secretword = input("Player 1: Enter a Secret Word\n")
    print("\n"*20)#REPLACE WITH ANIMATION
    animation()
    print("Your category is " + randomCat + "\n")
    print("Player 2:\n")
    playFunction()


while cont == 1:
    randomize()
    players = int(input("Let's play hangman! \n1 or 2 players?\n"))
    animation()#ANIMATION HERE
    print("Your category is " + randomCat + "\n")
    if players == 1:
        onePlayer()

    else:
        twoPlayer()

    print("---")
    playAgain = str(input("Play again? \n"))
    
    affirmative = ["yes", "Yes", "y", "Y"]
    if playAgain in affirmative:
        continue
    else:
        cont = cont - 1
        

