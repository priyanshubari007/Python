snackbox1 = {"Chips", "Fruits", "Drinks", "Biscuits", "Candies"}
snackbox2 = {"Chocolates", "Milkshake", "Candies"}
print("Snack box 1:", snackbox1)
print("Snack box 2:", snackbox2)

snackbox1.add("orange")
print("Snack box 1 after adding another item:", snackbox1)

common_snacks = snackbox1.intersection(snackbox2)
print("Snacks in both boxes:", common_snacks)

import array as arr
snack_counts = arr.array('i'[3, 5, 2, 4])
print("Snack counts:", snack_counts)

snack_counts.insert(0,1)
snack_counts.append(6)
print("Snack count after adding items:", snack_counts)

count_of_4 = snack_counts.count(4)
print("Number of times 4 appears:", count_of_4)

snack_counts.reverse()
print("Reversed fruit counts array:", snack_counts)


print("")
print("======== Snack Box Shack =========")
print("Snack box 1:", snackbox1) 
print("Snack box 2:", snackbox2)
print("Shared snacks:", common_snacks)
print("Snack counts:", snack_counts)
print("=======================================================================")