def greet_customer():
    print("Welcome to the Art Supplies Shop ! ")
    print("Get your art supplies here!")
    greet_customer()



price_per_paintbox = float(input("Enter the price per paintbox in dollars : "))
paintboxes_sold = int(input("Enter the number of paintboxes sold : "))


def calculate_total(price, paintboxes):
    total = price * paintboxes
    return total


total_cost = calculate_total(price_per_paintbox, paintboxes_sold)

rounded_total = round(total_cost, 2)
print("Total Cost: ", rounded_total)


amount_paid = float(input("Enter the amount paid by the customer : "))

def calculate_change(paid,total):
    change = paid - total
    return change


change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)

def thank_you_message(paintboxes):
    if paintboxes >= 5:
        return "Wow, big order! Thanks so much for your support!"
    else:
        return "Thanks for stopping by the stand!"
    
closing_message = thank_you_message(paintboxes_sold)

print("")
print("=============ART SUPPLIES RECEIPT=================")
print("Price Per Paintbox:", price_per_paintbox)
print("Paintboxes Sold : ", paintboxes_sold)
print("Total Cost : ", rounded_total)
print("Amount Paid : ",amount_paid)
print("Change Due : ", rounded_change)
print(closing_message)
print("============================================================")




