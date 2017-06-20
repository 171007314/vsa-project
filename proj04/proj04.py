# Name:
# Date:

"""
proj04

Asks the user for a string and prints out whether or not the string is a palindrome.

"""
def main():
    User_String = raw_input("Type a word or phrase: ").lower().replace(" ", "")
    opp_string = User_String[::-1].lower().replace(" ", "")
    if opp_string == User_String:
        print "Your phrase or word is a palindrome"
    else:
        print "Your prase or word is not a palindrome"
    replay = raw_input("Would you like to enter another word? ")
    if replay == "yes":
        main()
    if replay == "no":
        print "This machine hates you"
main()
