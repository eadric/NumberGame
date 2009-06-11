import random

guessCount      = 1
yourGuess       = 0
randNum         = int((random.random() * 100) + 1 )

def evalGuess():
        global guessCount
        global yourGuess
        global randNum
        if yourGuess > randNum:
                print "Too high, try again"
                guessCount += 1
                doGuess()
        elif yourGuess < randNum:
                print "Too low, try again"
                guessCount += 1
                doGuess()
        else:
                print "You got it, and it took ", guessCount, " tries!"

        

def doGuess():
        global guessCount
        global yourGuess
        global randNum
        yourGuess = input("Guess: ")
        evalGuess()

def main():
        global guessCount
        global yourGuess
        global randNum
        if guessCount == 1:
                print "I've thought of an integer between 1 - 100, can you guess it?"
                doGuess()
        else:
                print "Try again"
                doGuess()

main()
