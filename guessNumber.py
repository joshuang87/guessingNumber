# This is a simple game of guessing number program.
# This program will not allow player to customize the guessing number range.
# First, player execute the program. Program will ask player either they enter yes or else to continue or quit this program.
# This program have only set 3 chance for player to guess. If they not got it in those 3 chance, program will show the random number

import random

play = input("Do you want to play Guessing Number Game ? : ").lower()
randomNum = random.randint(0,100)
playCount = 0
playLimit = 3

if play == "yes":

    guessNum = int(input("Make a Guess : "))

    if guessNum == randomNum:

        print("Yes, you got it")

    else:

        while guessNum != randomNum and playCount < playLimit and playCount != 2:

            if guessNum > randomNum:

                print("smaller your guess number")
                playCount += 1
                chance = playLimit - playCount
                print("You have more " + str(chance) + " chance to guess")
                newGuessNum = int(input("Make a Guess Again : "))
                guessNum = newGuessNum

            elif guessNum < randomNum:

                print("greater your guess number")
                playCount += 1
                chance = playLimit - playCount
                print("You have more " + str(chance) + " chance to guess")
                newGuessNum = int(input("Make a Guess Again : "))
                guessNum = newGuessNum
            
            else:

                print("You got it")
        
        
        print("You not got it\nThe random number is " + str(randomNum))

else:

    quit()