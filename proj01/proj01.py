# Name: Kayden
# Date: 6/19/17

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!
# I added the hundred years old feature, the movie feature, and the capital letter extension
User_Name = raw_input("Whsat is your name?")
z = "You will be one hundred years old in"
a = "You turned 100 in"
year = 2017
firstletter = User_Name[0]
capitalfirst = firstletter.upper()
otherpart = User_Name[1:].lower()
print "Your name is",capitalfirst + otherpart
User_Age = int(raw_input("What is your age"))
x = (100 - User_Age) + year
User_Birth = raw_input("Have you had your birthday this year?")
y = x
if (User_Birth == "no"): y = x - 1
if User_Age == 100 and User_Birth == "yes":
    z = a
if User_Age == 100 and User_Birth == "no":
    z = a
if User_Age > 100: z = a
print z,y
if (User_Age <=12):
    parent = raw_input("Do you have a parent with you?")
    if parent == "yes":
        print"You can see G and PG-13 movies"
    elif parent == "no":
        print"You can see G movies"
elif (User_Age <=16):
    print "You can see G, PG, and PG-13 movies"
else:
    print "You can see G, PG, PG-13, and R movies"

