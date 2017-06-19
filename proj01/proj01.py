# Name: Kayden
# Date: 6/19/17

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!
User_Name = raw_input("What is your name?")
firstletter = User_Name[0]
capitalfirst = firstletter.upper()
otherpart = User_Name[1:].lower()
print "Your name is",capitalfirst + otherpart
User_Age = int(raw_input("What is your age"))
x = (100 - User_Age) + 2017
User_Birth = raw_input("Have you had your birthday this year?")
y = x
if (User_Birth == "no"): y = x - 1
print "You will be one hundred years old in",y
if (User_Age < 8): print "You can see G movies"
if (User_Age <=12): print "You can see G and PG movies"
if (User_Age >12): print "You can see G, PG, and PG-13 movies"
if (User_Age >= 17): print "You can see R movies"

