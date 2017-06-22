import random
WORDLIST_FILENAME = "words.txt"
n = 7
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

def load_words():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist
wordlist = load_words()

def display_hand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter
    print


def deal_hand(n):
    hand = {}
    num_vowels = n / 3
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
    print hand
    return hand
hand = deal_hand(n)
word = raw_input("Enter a word ")
def is_valid_word(word, hand, wordlist):
    x = []
    for letter in word:
        x.append(letter)
    y = "".join(x)
    print y
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """


is_valid_word(word, hand, wordlist)


