# importing random
from random import *

# taking input from user
user_gmail = input("SET PASS:")

# storing alphabet letter to use thm to crack password
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
            'w', 'x', 'y', 'z',]
 

# initializing an empty string
guess = ""



# using while loop to generate many passwords untill one of
# them does not matches user_gmail
while (guess != user_gmail):
    guess = ""
 # them does not matches user_gmail 
    for letter in range(len(user_gmail)):
        guess_letter = password[randint(0, 25)]
        guess = str(guess_letter) + str(guess)
    # printing guessed passwords
    print(guess)

# printing the matched password
print("Your password is:",guess)