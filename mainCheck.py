# regex library import
import re

userRole = None
userPassword = None
normalUserMinimumChar = 10
adminUserMinimumChar = 13

while True:
  userRole = input("What role do you have? Type 'admin' or 'normal' to continue: ").lower().replace(" ", "")

  # compares the userRole to strings in the set
  if userRole in ('admin', 'normal'):
    print("User role is accepted")
    userPassword = input("Enter password! Must contain at least 1 letter, 1 number and be at least 8 characters long: ").lower().replace(" ", "")
    break
  else:
    print("Incorrect user role :(")
    continue

# Password Check Class
class PassCheck1:

    def normalUser(password):

        #  using re.search in order to make sure the given password has the necessary characters
        regexPattern = re.search("[a-z0-9]", password)

        if len(password) < normalUserMinimumChar:
            print("Password is too short! Needs to be at least 8 characters long.")
        elif password.isdigit():
            print("Your password needs at least one letter.")
        elif not regexPattern:
            print("Password is missing a number!")
        else:
            print("Password is accepted!")

    def adminUser(password):

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
        # checks if password is only numbers
        elif password.isdigit():
            print("Your password needs at least one letter!")
        elif not hasNumber:
            print("Your password needs at least one number!")
        elif specialCharCount < 3:
            print("Your password is missing some special characters. You need at least 3")
        elif not regexPattern:
            print("Password is missing a special character!")
        else:
            print("Password looks good!")

# conditional statement that'll call a method depending on the user role
if userRole == 'admin':
    adminUser = PassCheck1.adminUser(userPassword)

else:
    normalUser = PassCheck1.normalUser(userPassword)




