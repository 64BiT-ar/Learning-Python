# Breakfast between 7:00 and 8:00
# Lunch between 12:00 and 13:00
# Dinner between 18:00 and 19:00.

# Prompts the user for a time (formatted in 24-hour time)
def main():
    input_time = input("What time is it? ").strip()
    time = convert(input_time)

    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")
    else:
        ... # no output


def convert(time):
    hours, mins = time.split(':')
    hours = float(hours)
    mins = float(mins)
    
    if 0.0 <= hours <=24.0 and 0.0 <= mins <= 60:
        mins = mins / 60
        return hours + mins
    else:
        print("Not a valid time format, valid format = 00:00 - 24:00")
        return 0.0
    


# Outputs whether it’s breakfast time, lunch time, or dinner time
if __name__ == "__main__":
    main()