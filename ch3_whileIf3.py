from random import randrange

rngeRand = randrange(1, 20, 1)

while True:
    userGuess = int(input("Guess a number between 1 and 20: "))

    if userGuess == rngeRand:
        print("You guessed it")
        break
    elif userGuess < rngeRand:
        print("Too low!")
    else:
        print("Too high!")