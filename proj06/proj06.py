# Name:
# Date:


# proj06: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()


# your code begins here!
x = random.choice(wordlist)

comp_word = []
for letter in x:
    comp_word.append(letter)
print "I am thinking of a " +str(len(comp_word)), "letter word"
print comp_word
def main():
    life = 8
    a = len(x) * "_"
    print a
    guesses_made = []
    while life > 0:
        user_guess = raw_input("Guess a letter: ")
        for o in user_guess:
            guesses_made.append(o)
        print "You have guessed these letters",guesses_made
        intersection = [el for el in comp_word if el in user_guess]
        if intersection == []:
            print "Incorrect Guess"
            life = life - 1
            print "You lost a life. Lives = ",life
        if intersection != []:
            print "Good Guess"
            a.replace("_", "user_guess")
        if life == 0:
            print "Game Over"
            print "The word was",x
            quit()

        set2 = set(guesses_made)
        answer = [el for el in comp_word if el in set2]
        print answer
        if answer == comp_word:
            print "You win"
            quit()
main()
main()



