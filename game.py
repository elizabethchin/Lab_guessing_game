"""A number-guessing game."""

# Put your code here
import random
name = input("Howdy, what's your name? >")
print(name)
print(name + ", " "I'm thinking of a number between 1 and 100. Try to guess my number.")

answer = (random.randint(0,100))
attempts = 0
guess = -1

while answer != guess:
	guess = int(input("What's your guess?"))
	if guess > answer:
		print("Your guess is too high, try again.")
		attempts = attempts + 1
	elif guess < answer: 
		print("Your guess is too low, try again")
		attempts = attempts + 1
	elif guess == answer:
		print("Well done, " + name + " You found my number in " + str(attempts) + " tries!")


