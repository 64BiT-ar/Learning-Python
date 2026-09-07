def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    df = d.replace("$","")
    df = round(float(df),1)
    return df


def percent_to_float(p):
    pf = float(p.replace("%",""))
    pf = round(pf/100,2)
    return pf


main()