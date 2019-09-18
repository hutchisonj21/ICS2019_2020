"""

This program is a HiLo game

@author Jayden Hutchison
@version 1.0
@since 9/11/19

"""

#These lines set up variables/import packages used later in the program
import random

playAgain = True



#This method is the meat and potatoes of the high low game
def hiLo(guess, answer, n):
	n -= 1
	
	if(n <= 0):
		if (guess == answer):
			print("Congratulations! " + str(guess) + " was correct!")
			return()
		else:
			print("Oh no! It looks like you ran out of guesses. The number was " + str(answer))
			return()
		
	
	if(guess > answer):
		print(str(guess) + " was too high. You have " + str(n) + " guesses left.")
		guess = int(input("What is your new guess?"))
		
	elif (guess < answer):
		print(str(guess) + " was too low. You have " + str(n) + " guesses left.")
		guess = int(input("What is your new guess?"))
		
	else:
		print("Congratulations! " + str(guess) + " was correct!")
		return()
	
	hiLo(guess, answer, n)



#This is where information is displayed to the user
print("Hello there! This is a High-Low game, I wish you luck!")


while(playAgain):
	guessNumber = 5
	
	print("\n\nI am thinking of a number between 1 and 50, try and guess it. You have 5 attempts.")
	
	answer = random.randint(1,50)
	
	guess = int(input("What is your guess?"))
	
	hiLo(guess, answer, guessNumber)
	
	
	#This is a "play again" feature
	understand = False
	
	while(not understand):
		choice = input("Would you like to play again? (yes or no)")
		
		if("no" in choice or "No" in choice):
			print("Thanks for playing!")
			playAgain = False
			understand = True
		elif("yes" in choice or "Yes" in choice):
			playAgain = True
			understand = True
		else:
			print("I'm sorry, I don't understand.")
