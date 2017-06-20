# Name:
# Date:
import random

""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
test = random.randint(1,9)
answer = 10
wrong_answer = 0
num_answers = int(raw_input("How many guesses do you want? ")) -1
while answer != test and wrong_answer <= 4:
    answer = int(raw_input("Guess a number between one and nine: "))
    if answer > test:
        print "You are too high"
        wrong_answer = wrong_answer + 1
    if answer < test:
        print "You are too low"
        wrong_answer = wrong_answer + 1
    if answer == test and wrong_answer != 1:
        print "You got it correct"
        print "You got",wrong_answer,"questions wrong"
        restart = raw_input("Would you like to play again? ")
        if restart == "yes":
            wrong_answer = 0
            answer = 10
            num_answers = int(raw_input("How many guesses do you want? ")) - 1
        if restart == "no":
            print "Game Over"
    if answer == test and wrong_answer == 1:
        print "You got it correct"
        print "You got",wrong_answer,"question wrong"
        restart = raw_input("Would you like to play again? ")
        if restart == "yes":
            wrong_answer = 0
            answer = 10
            num_answers = int(raw_input("How many guesses do you want? ")) - 1
        if restart == "no":
            print "Game Over"
    if wrong_answer > num_answers:
        print "You failed this game"
        restart = raw_input("Would you like to play again? ")
        if restart == "yes":
            wrong_answer = 0
            answer = 10
            num_answers = int(raw_input("How many guesses do you want? ")) - 1
        if restart == "no":
            print "Game Over"

