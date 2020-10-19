# Regular expressions
import re

def isPhoneNumber(string):
    PhoneRegex = r'(\d{3}|\(\d{3}\))?(\s|-|\.)?(\d{3})(\s|-|\.)(\d{4})'
    RegexTest = re.compile(PhoneRegex)
    return RegexTest.search(string)

print(isPhoneNumber('654-6574'))