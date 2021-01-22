# regex library import
import re

userRole = None
userPassword = None

while True:
  userRole = input("What role do you have? Type 'admin' or 'normal' to continue: ").lower().replace(" ", "")

  if userRole in ('admin', 'normal'):
    print("User role is accepted")
    userPassword = input("Enter password! Must contain at least 1 letter, 1 number and be at least 8 characters long: ").lower().replace(" ", "")
    break
  else:
    print("Incorrect user role :(")
    continue


# Password Check Class
class PassCheck1:
    def __init__(self, role, password):
        self.userRole = role
        self.password = password


    def normalUser(password):
        minimumChar = 8

        #  using re.search in order to make sure the given password has the necessary characters
        regexPattern = re.search("[a-z][0-9]", password)

        if len(password) < minimumChar:
            print("Password is too short! Needs to be at least 8 characters long.")
        elif password.isdigit():
            print("Your password needs at least one letter.")
        elif not regexPattern:
            print("Password is missing a number!")
        else:
            print("Password is accepted!")

    def adminUser(password):
        minimumChar = 13

        # added this in case the user adds spaces within their passwords
        noSpacesPassword = password.replace(" ", "")

        #  using re.search in order to make sure the given password has the necessary characters
        regexPattern = re.search("[a-z][0-9]", noSpacesPassword)

        if len(password) < minimumChar:
            print("Password is too short!")
        elif password.isdigit():
            print("Your password needs at least one letter. C'mon!")
        elif not regexPattern:
            print("Password is missing a number!")
        else:
            print("Password looks good!")




