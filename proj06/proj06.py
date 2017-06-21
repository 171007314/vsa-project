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

def main():
    x = random.choice(wordlist)

    word = []
    for letter in x:
        word.append(letter)
    print "I am thinking of a " + str(len(word)), "letter word"
    life = 8
    a = len(x) * ["_"]
    while life > 0:
        player_input = raw_input("Input a single letter: ")
        player_guess = player_input[0]
        intersection = [el for el in word if el in player_guess]
        if intersection == []:
            print "Sorry, incorrect"
            life = life - 1
            print "You lost a life, Lives = " + str(life)
        elif intersection != []:
            for i in range(0, len(word)):
                if word[i] == player_guess:
                    a[i] = player_guess
                    print "Good Guess"
                    print "".join(a)

        if "".join(a) == x:
            print "Congratulations, you win"
            playAgain()
        if life == 0:
            print "Game Over"
            print "The word was",x
            playAgain()
    main()
def playAgain():
    again = raw_input("Would you like to play again? ")
    if again == 'yes':
        main()
    if again == 'no':
        print "This machine hates you"
    playAgain()
main()



