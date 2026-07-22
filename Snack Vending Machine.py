def calculate_change(paid,price):
    change = paid - price
    return change


snack_price = 25
print("=========SNACK VENDING MACHINE================")
print(f"This snack costs {snack_price} units.")
print("Accepted coins: 1, 5, 10, 25\n")


total_inserted = 0
coins_inserted = 0

while True:
    coins = int(input("Insert a coin(1, 5, 10, or 25): "))


    if coins != 1 and coins != 5 and coins !=10 and coins !=25:
        print("Invalid coin,try again\n")
        continue

    total_inserted +=coins
    coins_inserted +=1
    print(f"Inserted {coins}. Total so far: {total_inserted}\n")
    if total_inserted >= snack_price:
        print("Enough money inserted!\n")
        break


change_due = calculate_change(total_inserted, snack_price)


print("Dispensing your snack...")


if change_due == 0:
    pass
else:
    print("Here is your change: {change_due} units")


print("\n========  PURCHASE SUMMARY  ===========")
print("Snack price: ", snack_price)
print("Coins Inserted:", coins_inserted)
print("Total Paid: ",total_inserted)
print("Change Given: ", change_due)
print("==============================")
print("Thanks for your purchase!")
