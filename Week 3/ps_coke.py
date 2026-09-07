# Accepting coins - 25, 10, 5
# Coke price 50 cents

amount_due = 50
change_owed = 0

while True:
    
    print("Amount Due:", amount_due)
    insert_coin = int(input("Insert Coin: "))

    if insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
        amount_due -= insert_coin
        if amount_due <= 0:
            change_owed = amount_due * -1
            break
    else:
        continue

print(f"Change Owed: {change_owed}")