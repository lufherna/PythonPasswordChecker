# regex library import
import re

userRole = None
userPassword = None

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
    # def __init__(self, role, password):
    #     self.userRole = role
    #     self.password = password

    def normalUser(password):
        minimumChar = 8

        #  using re.search in order to make sure the given password has the necessary characters
        regexPattern = re.search("[a-z0-9]", password)

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

        #  using re.search in order to make sure the given password has the necessary characters
        regexPattern = re.search("[a-z0-9][@!#$%^&*]", password)
        # used regex search to grab the specific info regarding numbers inside the password
        hasNumber = re.search(r'\d', password)

        # checks minimum length
        if len(password) < minimumChar:
            print("Password is too short! Needs to be at least 13 characters long")
        # checks if password is only numbers
        elif password.isdigit():
            print("Your password needs at least one letter!")
        elif not hasNumber:
            print("Your password needs at least one number!")
        elif not regexPattern:
            print("Password is missing a special character!")
        else:
            print("Password looks good!")

# conditional statement that'll call a method depending on the user role
if userRole == 'admin':
    adminUser = PassCheck1.adminUser(userPassword)

else:
    normalUser = PassCheck1.normalUser(userPassword)




