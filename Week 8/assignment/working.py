import re
import sys


def main():
    print(time_format(input("Hours: ")))
    # print(convert(input("Hours: ")))


def time_format(s):
    if match := re.search(r"^\d+(:\d{2})? {1}(AM|PM){1} {1}to{1} {1}\d+(:\d{2})? {1}(AM|PM){1}$",s):
        return True
    else:
        return False

def convert(s):
    match = re.search(r".*(\d+:+\d+ {1})(\w* {1}).*(\d+:+\d+ {1})(.*)", s)
    
    m1 = match.group(2).strip()
    m2 = match.group(4).strip()
    time1 = match.group(1)
    time2 = match.group(3)

    if m1 == "PM":
        hour, min = match.group(1).split(":")
        hour = int(hour)
        hour += 12
        hour = str(hour)
        time1 = hour + ":" + min
        print("hours", hour)
    if m2 == "PM":
        hour, min = match.group(3).split(":")
        hour = int(hour)
        hour += 12
        hour = str(hour)
        time2 = hour + ":" + min
        print("hours", hour)

    return f"{time1} to {time2}"

...


if __name__ == "__main__":
    main()