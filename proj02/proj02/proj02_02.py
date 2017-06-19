# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""
pre = 1
new = 1
input = int(raw_input("How many Fibonacci numbers would you like to find?"))
for var in range(input):
    var = pre + new
    pre = new
    new = var
print pre



