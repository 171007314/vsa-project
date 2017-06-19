# Name:
# Date:

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!

name = raw_input("Enter your name: ")
age = int(raw_input("Enter your age: "))
birthday = raw_input("Has your birthday happened this year? Enter Y or N: ")

if birthday == "Y":
    year = 2017
    for var in range(age, 100):
        birth = year - age + var

else:
    year = 2017
    for var in range(age, 100):
        birth = year - age + var - 1
# Calculates the year that the user will be 100
# TO DO: Write for or while loop that adds one year to year each time and stops at the year that the user will be 100

print name, " will turn 100 in the year", birth, "."
