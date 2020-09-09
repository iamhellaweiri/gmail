print ("HH            HH             AAAAA           cccccccccc    KK   / /  ")
print ("HH            HH            AA   AA          cccccccccc    KK  / /   ")
print ("HH            HH           AA     AA         cc            KK / /    ")
print ("HH            HH          AAAAAAAAAAA        cc            KK/ /     ")
print ("HHHHHHHHHHHHHHHH         AA         AA       cc            KK /      ")
print ("HH            HH        AA           AA      cc            KK\ \     ")
print ("HH            HH       AA             AA     cc            KK \ \    ")
print ("HH            HH      AA               AA    cc            KK  \ \   ")
print ("HH            HH     AA                 AA   cccccccccc    KK   \ \  ")
print ("HH            HH    AA                   AA  cccccccccc    KK    \ \ ")
print ("                                                    BY CHIN YI ZHE IDK")
# importing random
from random import *

# taking input from user
user_pass = input("[ROOT PASSWORD LOGIN]>>>")
user_pass = input("[BY CHIN YI ZHE IDK] SOCIAL MEDIA>>>")
user_pass = input("[TARGETS NAME]>>>")

# storing alphabet letter to use thm to crack password
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
            'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8',
            '9','0',]

# initializing an empty string
guess = ""


# using while loop to generate many passwords untill one of
# them does not matches user_pass
while (guess != user_pass):
    guess = ""
    # generating random passwords using for loop
    for letter in range(len(user_pass)):
        guess_letter = password[randint(0, 25)]
        guess = str(guess_letter) + str(guess)
    # printing guessed passwords
    print(guess)
    
# printing the matched password
print("TARGETS PASSWORD FOUND:goawaycorona12345",guess)
print("TARGET INFO:DEVICE IPHONE 6 STATUS:ONLINE LOCATION:CANADA")         
print("+++++++++++++#DONE#+++++++++++++")
