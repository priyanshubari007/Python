items = ["pencil", "eraser", "notebook", "sharpener", "glue"]
stock_counts = [12, 0, 8, 5, 3]

inventory = {item: count for item, count in zip(items, stock_counts)}
print("Full inventory:", inventory)

in_stock_item = [item for item in items if inventory[item] > 0]
print("Items in stock:", in_stock_item)

chosen_item = input("which item do you want to buy?")


if chosen_item not in inventory or inventory[chosen_item] == 0:
    print(chosen_item,"is out of stock! Stopping the checker.")
    exit()


prices = [10, 5, 40, 15, 20]
markup = int(input("Enter the markup amount to add to every price: "))

marked_up_price = list(map(lambda p: p + markup, prices))
print("Marked Up Prices:", marked_up_price)

item_index = items.index(chosen_item)
chosen_price = marked_up_price[item_index]
print("Price of", chosen_item, "after markup:", chosen_price)

inventory[chosen_item] = inventory[chosen_item] - 1
print(chosen_item, "purchased! Remaining stock:", inventory[chosen_item])

print("")
print("====================SCHOOL STORE INVENTORY CHECKER==================")
print("Item Bought:", chosen_item)
print("Price Paid:", chosen_price)
print("Updated Inventory:", inventory)
print("======================================================================")