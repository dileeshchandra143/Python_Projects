#!/User/Bin/ env python
# This is a guesser.py

def main():
    print("Guess a number between 1 and 100")
    RandomNumber = 35
    found = flase        #flags variable to see if they guessed it
   


    while not found:
        UserGuess = input("Your guess: ")
        if UserGuess == RandomNumber:
             print ("You Got it!!!!!!!!!!!")
        elif UserGuess > RandomNumber:
             print("Guess Lower!")
        else:
             print("Guess Higher!!!!!!!!!!")  