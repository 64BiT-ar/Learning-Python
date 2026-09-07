import re

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Input like MM/DD/YYYY or September 8, 1998
def format_():
    while True:
        inp = input("Date: ").strip()
        try:
            if '/' in inp:
                month, day, year = inp.split("/")

                if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                    day = int(day)
                    month = int(month)
                    return f"{year}-{month:02}-{day:02}"
                else:
                    continue
            else:
                month, day, year = inp.split(" ")
                day = re.sub(r"\D", "", day)
                day = int(day)

                month_i = months.index(month) + 1

                if month in months and 1 <= month_i <= 12 and 1 <= int(day) <= 31:
                    return f"{year}-{month_i:02}-{day:02}"
                else:
                    continue
        except (ValueError, IndexError):
            pass


# Out put as YYYY-MM-DD

print(format_()) 
