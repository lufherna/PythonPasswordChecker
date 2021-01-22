# regex library import
import re

userPassword = input("Enter password! Must contain at least 1 letter, 1 number and be at least 8 characters long: ")

# iteration 1
class PassCheck1:
  # def __init__(self, password):
  #   self.password = password

  minimumChar = 8

  def regexSearch(password):

    noSpacesPassword = password.replace(" ", "")
    regexPattern = re.search("[A-Z][a-z][0-9]", noSpacesPassword)
    if regexPattern and len(password) >= 8:
      print("Password looks good!")
    else:
      print("Password is missing required characters")


firstUserCheck = PassCheck1.regexSearch(userPassword)