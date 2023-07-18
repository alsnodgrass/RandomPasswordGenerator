import secrets
import string
import random

lowerCase = string.ascii_lowercase
upperCase = string.ascii_uppercase
numbers = string.digits
specials = string.punctuation
allCharacters = lowerCase + upperCase + numbers + specials

try:
    passLength = int(input("How long does the password need to be at least? "))
except:
    passLength = int(input("Please input a valid number.\nHow long does the password need to be at least? "))

upperChoice = input("Does the password need upper case letters? Y/N: ")
while upperChoice != "Y" and upperChoice != "y" and upperChoice != "N" and upperChoice != "n":
    upperChoice = input("Please input a valid answer.\nDoes the password need upper case letters? Y/N: ")

if upperChoice == "Y" or upperChoice == "y":
    try:
        numberUpper = int(input("How many? "))
    except:
        numberUpper = int(input("Please input a valid number.\nHow many? "))
elif upperChoice == "N" or upperChoice == "n":
    numberUpper = 0


lowerChoice = input("Does the password need lower case letters? Y/N: ")
while lowerChoice != "Y" and lowerChoice != "y" and lowerChoice != "N" and lowerChoice != "n":
    lowerChoice = input("Please input a valid answer.\nDoes the password need lower case letters? Y/N: ")

if lowerChoice == "Y" or lowerChoice == "y":
    try:
        numberLower = int(input("How many? "))
    except:
        numberLower = int(input("Please input a valid number.\nHow many? "))
elif lowerChoice == "N" or lowerChoice == "n":
    numberLower = 0


numberChoice = input("Does the password need numbers? Y/N: ")
while numberChoice != "Y" and numberChoice != "y" and numberChoice != "N" and numberChoice != "n":
    numberChoice = input("Please input a valid answer.\nDoes the password need numbers? Y/N: ")

if numberChoice == "Y" or numberChoice == "y":
    try:
        numberNumber = int(input("How many? "))
    except:
        numberNumber = int(input("Please input a valid number.\nHow many? "))
elif numberChoice == "N" or numberChoice == "n":
    numberNumber = 0


specialChoice = input("Does the password need special characters? Y/N: ")
while specialChoice != "Y" and specialChoice != "y" and specialChoice != "N" and specialChoice != "n":
    specialChoice = input("Please input a valid answer.\nDoes the password need special characters? Y/N: ")

if specialChoice == "Y" or specialChoice == "y":
    try:
        numberSpecial = int(input("How many? "))
    except:
        numberSpecial = int(input("Please input a valid number.\nHow many? "))
elif specialChoice == "Y" or specialChoice == "y":
    numberSpecial = 0

password = ''

for i in range(numberUpper):
    password += ''.join(secrets.choice(upperCase))

for i in range(numberLower):
    password += ''.join(secrets.choice(lowerCase))

for i in range(numberNumber):
    password += ''.join(secrets.choice(numbers))

for i in range(numberSpecial):
    password += ''.join(secrets.choice(specials))

extraCharacters = int(passLength - len(password))

if extraCharacters > 0:
    for i in range(extraCharacters):
        password += ''.join(secrets.choice(allCharacters))

password = ''.join(random.sample(password, len(password)))
password = ''.join(random.sample(password, len(password)))
password = ''.join(random.sample(password, len(password)))
password = ''.join(random.sample(password, len(password)))

print("Password: ", password)