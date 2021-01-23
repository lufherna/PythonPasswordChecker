# regex library import
import re

userRole = None
userPassword = None
normalUserCorrectPassword = True
adminUserCorrectPassword = True
normalUserMinimumChar = 10
adminUserMinimumChar = 13

while True:
    userRole = input("What role do you have? Type 'admin' or 'normal' to continue: ").lower().replace(" ", "")

    # compares the userRole to strings in the set
    if userRole in ('admin', 'normal'):
        print("User role is accepted")
        userPassword = input(
            "Enter password! Must contain at least 1 letter, 1 number and be at least 8 characters long: ").lower().replace(
            " ", "")
        break

    else:
        print("Incorrect user role :(")
        continue


# Password Check Class
class PassCheck1:

    # method that will check a normal User's passwords only
    def normalUser(password):

        global normalUserCorrectPassword

        #  using re.search in order to make sure the given password has the necessary characters
        regexPattern = re.search("[a-z0-9]", password)

        if len(password) < normalUserMinimumChar:
            print("Password is too short! Needs to be at least 8 characters long.")
            normalUserCorrectPassword = False

        elif password.isdigit():
            print("Your password needs at least one letter.")
            normalUserCorrectPassword = False

        elif not regexPattern:
            print("Password is missing a number.")
            normalUserCorrectPassword = False

        else:
            print("Password is accepted!")
            normalUserCorrectPassword = True


    # method that runs if the user is an admin only
    def adminUser(password):

        global adminUserCorrectPassword

        specialCharCount = 0

        specialCharacters = ['@', '!', '#', '$', '%', '^', '&', '*']

        #  using re.search in order to make sure the given password has the necessary characters
        regexPattern = re.search("[a-z0-9][@!#$%^&*]", password)

        # used regex search to grab the specific info regarding numbers inside the password
        # \d returns a match where the string contains digits (numbers from 0-9)
        hasNumber = re.search(r'\d', password)

        # trying to iterate through the password to find and count the special characters
        for char in password:
            if char in specialCharacters:
                specialCharCount += 1

        # checks minimum length
        if len(password) < adminUserMinimumChar:
            print("Password is too short! Needs to be at least 13 characters long")
            adminUserCorrectPassword = False

        # checks if password is only numbers
        elif password.isdigit():
            print("Your password needs at least one letter")
            adminUserCorrectPassword = False

        elif not hasNumber:
            print("Your password needs at least one number")
            adminUserCorrectPassword = False

        elif specialCharCount < 3:
            print("Your password is missing some special characters. You need at least 3")
            adminUserCorrectPassword = False

        elif not regexPattern:
            print("Password needs at least one special character")
            adminUserCorrectPassword = False

        else:
            print("Password looks good!")
            adminUserCorrectPassword = True

"""
conditional statement that'll call a method depending on the user role
This runs the methods to  make sure the passwords are accurate but if they're wrong
it'll run the methods again but asking for the correct pw
"""


if userRole == 'admin':
    adminUser = PassCheck1.adminUser(userPassword)

    while not adminUserCorrectPassword:
        userPassword = input(
            "Your password seems to be missing some items. Please try again! ").lower().replace(
            " ", "")
        # runs the method again to double check the validity of the password
        adminUser = PassCheck1.adminUser(userPassword)
    else:
        print("Admin user password saved!")


elif userRole == 'normal':
    normalUser = PassCheck1.normalUser(userPassword)

    # runs if correctPassword is False
    while not normalUserCorrectPassword:
        userPassword = input(
            "Your password seems to be missing some items. Please try again! ").lower().replace(
            " ", "")
        # runs the method again to double check the validity of the password
        normalUser = PassCheck1.normalUser(userPassword)
    else:
        print("Normal User password saved!")

