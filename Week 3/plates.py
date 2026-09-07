# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2 or s.isalnum() == False: # Pre check on len and numeric
        return False

    for i in range(2):
        if s[i].isalpha() == False:
            return False

    if s.isalpha():
            return True
    
    for i in range(len(s)):
        if s[i].isdecimal():
            if s[i:].isdecimal() and s[i] != '0':
                return True
            else:
                return False
            
    return False



main()