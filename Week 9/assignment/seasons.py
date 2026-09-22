from datetime import date
import sys
import inflect
import re

def get_dob():
    user_dob = input("Date of Birth (YYYY-MM-DD): ")
    try:
        return date.fromisoformat(user_dob)
    except ValueError:
        sys.exit("Invalid date format")

def convert(days):
    p = inflect.engine()
    return p.number_to_words(days, andword="") + " minutes"


def main():
    today = date.today()
    user_dob = get_dob()
    day = int((today - user_dob).days)*24*60
    
    print(convert(day))


if __name__ == "__main__":
    main()