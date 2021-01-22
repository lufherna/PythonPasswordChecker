# regex library import
import re

userRole = input("What role do you have? Type in 'admin' or 'normal' to continue ")
userPassword = input("Enter password! Must contain at least 1 letter, 1 number and be at least 8 characters long: ")


# iteration 1
class PassCheck1:
    # def __init__(self, password):
    #   self.password = password

    def regexSearch(password):
        minimumChar = 8

        # added this in case the user adds spaces within their passwords
        noSpacesPassword = password.replace(" ", "").lower()

        # by making all passwords lowercase makes it a bit easier to work with regex
        regexPattern = re.search("[a-z][0-9]", noSpacesPassword)

        if len(password) < minimumChar:
            print("Password is too short!")
        elif password.isdigit():
            print("Your password needs at least one letter. C'mon!")
        elif not regexPattern:
            print("Password is missing a number!")
        else:
            print("Password looks good!")


firstUserCheck = PassCheck1.regexSearch(userPassword)
