# SayMyName.py Prints the name of the user and that they rule.

# Ask the user for their name.
name = input("What is your name? ")

# Print their name 100 times.
for x in range(100):
    # Print their name followed by a space and not a new line.
    print(name, end = " rules! ")
