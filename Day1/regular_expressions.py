import re

def isPhoneNumber(phone):
    phoneRegex = re.compile(r'((\d\d\d)|\(\d\d\d\))-(\d\d\d)-(\d\d\d\d)')
    # match object
    mo = phoneRegex.search(phone)
    if mo:
        return mo.group()
    return False

def isValidEmail(email):
    emailRegex = re.compile(r'([a-zA-Z0-9._%-])+@[a-zA-Z0-9.-]+(\.[a-zA-Z{2,4}])')
    # match object
    mo = emailRegex.search(email)
    if mo:
        return True
    return False
print(isPhoneNumber('415-555-4242'))
print(isValidEmail('rasugu@gmail.com'))