# Regular expressions
import re


# re.compile(string) returns a regex pattern object
# phone numbers 415.555.4242 (415) 555-4242 415-555-4242
# \d stands for a digit character

def isPhoneNumber(string):
    PhoneRegex = r'(\d{3}|\(\d{3}\))?(\s|-|\.)?(\d{3})(\s|-|\.)(\d{4})'
    RegexTest = re.compile(PhoneRegex)
    return RegexTest.search(string).group()


print(isPhoneNumber('(654) 6574'))
