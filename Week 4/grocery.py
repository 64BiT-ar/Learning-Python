grocery_list = {

}

while True:
    try:
        inp = input().upper()
        if inp in grocery_list:
            count = grocery_list[inp]
            count += 1
            grocery_list[inp] = count
        else:
            grocery_list[inp] = 1
    except KeyError:
        pass
    except EOFError:
        break

for item, count in sorted(grocery_list.items()):
    print(f"{count} {item}")


# By default, if you loop through a dictionary (like for item in menu:), Python only loops through the keys (the food names).
# If you want to access both the key and the value at the same time, Python provides built-in methods:

# menu.keys() gives you just the keys.
# menu.values() gives you just the values.
# menu.items() gives you both bundled together as pairs (tuples) so you can unpack them into two variables like for item, price in menu.items():.