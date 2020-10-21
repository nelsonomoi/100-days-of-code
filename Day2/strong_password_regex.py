# a function to test if a password is strong
# should have atleast eight characters
# atleast one uppercase letter and one lowercase
# atleast one number
import re

def isStrongPassword(password):
    passwordRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})')
    mo = passwordRegex.match(password)
    if mo:
        return mo.group()
    else:
        return False
print(isStrongPassword('hellotheRe2?'))